#!/usr/bin/env python3
"""Distribui regras canónicas por PR, sem merge automático."""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"registry/repositorios-consumidores.json"
BRANCH="bot/sincronizar-regras-governanca"
REQUIRED={"CONSTITUICAO.md","ROADMAP-PADRAO-GOVERNANCA.md","CARTA-CONTRATO-PADRAO-ROADMAP.md","standards/status-e-percentual-de-conclusao.md","CABEÇALHO/NORMA-CABECALHO-PADRAO.md"}
def run(args,cwd=None,check=True): return subprocess.run(args,cwd=cwd,text=True,capture_output=True,check=check)
def load():
 d=json.loads(REGISTRY.read_text(encoding="utf-8"))
 if d.get("schema_version")!=1 or d.get("source_repository")!="carlos-andrade/GOVERNANCA" or d.get("policy")!="pull_request_only": raise ValueError("Esquema, origem ou política inválida")
 if not isinstance(d.get("published_files"),list) or set(d["published_files"])!=REQUIRED: raise ValueError("Allowlist de documentos divergente")
 for f in d["published_files"]:
  p=PurePosixPath(f)
  if p.is_absolute() or ".." in p.parts or not (ROOT/f).is_file(): raise ValueError("Caminho/documento inválido: "+f)
 names=[r.get("name") for r in d.get("repositories",[])]
 if len(names)!=len(set(names)): raise ValueError("Repositórios duplicados")
 for r in d.get("repositories",[]):
  if r.get("name","").count("/")!=1 or not isinstance(r.get("enabled"),bool): raise ValueError("Entrada inválida: "+str(r))
 return d
def publish(name,files,destroot,source_sha,dry):
 with tempfile.TemporaryDirectory(prefix="gov-sync-") as t:
  repo=Path(t)/"repo"; c=run(["gh","repo","clone",name,str(repo)],check=False)
  if c.returncode:return {"repository":name,"status":"ERROR","detail":(c.stderr or c.stdout).strip()}
  h=run(["git","symbolic-ref","refs/remotes/origin/HEAD"],cwd=repo,check=False); base=h.stdout.strip().split("/")[-1] if h.returncode==0 else "main"
  for args in [("checkout",base),("pull","--ff-only","origin",base),("checkout","-B",BRANCH,base)]: run(["git",*args],cwd=repo)
  dest=repo/destroot; dest.mkdir(parents=True,exist_ok=True); entries=[]
  for f in files:
   src=ROOT/f; target=dest.joinpath(*PurePosixPath(f).parts); target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(src,target)
   entries.append({"source_path":f,"destination_path":destroot+"/"+f,"sha256":hashlib.sha256(src.read_bytes()).hexdigest()})
  manifest={"schema_version":1,"source_repository":"carlos-andrade/GOVERNANCA","source_branch":"main","source_commit":source_sha,"generated_at_utc":datetime.now(timezone.utc).isoformat(timespec="seconds"),"distribution_policy":"pull_request_only","files":entries,"warning":"Espelho de regras; adoção local exige revisão e aprovação."}
  (dest/"UPSTREAM-MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
  run(["git","add","--",destroot],cwd=repo); changed=run(["git","diff","--cached","--quiet"],cwd=repo,check=False)
  if changed.returncode==0:return {"repository":name,"status":"NO_CHANGE"}
  if dry:return {"repository":name,"status":"WOULD_OPEN_PR"}
  run(["git","config","user.name","github-actions[bot]"],cwd=repo);run(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"],cwd=repo);run(["git","commit","-m","chore(governanca): atualizar espelho de regras canónicas"],cwd=repo)
  p=run(["git","push","--force","origin","HEAD:refs/heads/"+BRANCH],cwd=repo,check=False)
  if p.returncode:return {"repository":name,"status":"ERROR","detail":(p.stderr or p.stdout).strip()}
  q=run(["gh","pr","list","--repo",name,"--head",BRANCH,"--state","open","--json","url","--limit","1"],check=False)
  if q.returncode:return {"repository":name,"status":"ERROR","detail":(q.stderr or q.stdout).strip()}
  prs=json.loads(q.stdout or "[]")
  if prs:return {"repository":name,"status":"PR_UPDATED","url":prs[0]["url"]}
  body="Sincronização da cópia isolada das regras canónicas da GOVERNANCA.\n\nCommit de origem: `"+source_sha+"`. Destino: `"+destroot+"/`. Rever e aprovar segundo as regras locais; não há merge automático nem certificação implícita."
  q=run(["gh","pr","create","--repo",name,"--base",base,"--head",BRANCH,"--title","chore(governanca): sincronizar regras canónicas","--body",body],check=False)
  return {"repository":name,"status":"PR_CREATED","url":q.stdout.strip()} if q.returncode==0 else {"repository":name,"status":"ERROR","detail":(q.stderr or q.stdout).strip()}
def main():
 p=argparse.ArgumentParser();p.add_argument("--dry-run",action="store_true");p.add_argument("--repo");a=p.parse_args()
 try:d=load()
 except Exception as e: print(json.dumps({"status":"FAIL","error":str(e)},ensure_ascii=False));return 2
 if not (os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")): print("GH_TOKEN/GITHUB_TOKEN obrigatório",file=sys.stderr);return 2
 if run(["gh","auth","status"],check=False).returncode: print("Autenticação GitHub CLI inválida",file=sys.stderr);return 2
 setup=run(["gh","auth","setup-git"],check=False)
 if setup.returncode: print("Não foi possível configurar autenticação Git para push/clone",file=sys.stderr);return 2
 targets=[r for r in d["repositories"] if r["enabled"]]
 if a.repo:
  targets=[r for r in targets if r["name"].lower()==a.repo.lower()]
  if not targets: print("Repositório não registado/ativo: "+a.repo,file=sys.stderr);return 2
 sha=run(["git","rev-parse","HEAD"],cwd=ROOT).stdout.strip(); results=[publish(r["name"],d["published_files"],d["destination_root"],sha,a.dry_run) for r in targets]
 report={"source_commit":sha,"mode":"dry-run" if a.dry_run else "pull-request","total":len(results),"errors":sum(x["status"]=="ERROR" for x in results),"results":results}
 print(json.dumps(report,ensure_ascii=False,indent=2));return 1 if report["errors"] else 0
if __name__=="__main__": raise SystemExit(main())
