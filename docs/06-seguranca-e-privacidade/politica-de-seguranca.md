# Política-base de segurança

Proteger confidencialidade, integridade, disponibilidade e rastreabilidade dentro de um modelo de ameaça definido.

Controlos proporcionais: inventário; menor privilégio; autenticação robusta; revisão de acessos; separação de ambientes; credenciais por finalidade e prazo; cofre de segredos e rotação; correções priorizadas por exposição; análise de dependências e configurações; backups protegidos e testados; logs úteis sem segredos; canal de reporte de vulnerabilidades; resposta a incidentes; revogação no encerramento.

Antes de publicar código, verificar histórico por segredos, direitos, dados e configurações de produção. Apagar o segredo num commit novo não apaga as cópias históricas; revogar e rodar credenciais é prioritário. Notificações externas dependem do caso e da obrigação aplicável.