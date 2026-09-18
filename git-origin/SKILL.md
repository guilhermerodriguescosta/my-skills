---
name: git-origin
description: Ao ser invocada explicitamente, commita todas as alteracoes locais e envia o branch atual para origin, sem executar testes.
---

# Git Origin

A invocacao explicita desta skill autoriza o fluxo completo no repositorio atual, sem executar testes:

1. Verifique se ha alteracoes e se o remoto `origin` existe.
2. Se nao houver alteracoes, informe isso e encerre sem criar commit vazio.
3. Execute `git add .`.
4. Crie um commit com mensagem curta e descritiva das alteracoes.
5. Execute `git push origin HEAD`.
6. Informe o hash curto do commit, o branch e o resultado do push.

Nunca use `--force`, `--force-with-lease`, `commit --amend`, rebase, reset ou qualquer comando que reescreva historico. Se o push for rejeitado, mantenha o commit local e informe a causa sem fazer pull, merge ou rebase automaticamente.