---
name: git-commit-origin
description: Quando acionada explicitamente para criar um commit e enviar ao origin, revisa as alterações da tarefa, executa os testes existentes relevantes e solicita uma única confirmação antes de preparar, criar ou enviar commits. Também permite revisar e enviar commits locais pendentes.
---

# Commit e envio ao origin

Use esta skill somente quando o usuário solicitar explicitamente seu fluxo de commit e envio. Menções para discutir ou editar a própria skill não iniciam esse fluxo. Responda em português.

## Revisão e testes

1. Identifique o repositório pelo contexto da tarefa, sem assumir que o diretório atual é o correto. Confira sua raiz, branch e URL de envio do `origin`. Se houver ambiguidade, pergunte; se faltar o remoto, houver HEAD destacado ou conflitos não resolvidos, pare e informe.
2. Na raiz do repositório, examine alterações preparadas, não preparadas e arquivos novos, incluindo o conteúdo relevante. Selecione somente alterações relacionadas à tarefa. Não use `git add .` nem altere arquivos para facilitar o commit. Se o contexto não permitir selecionar com segurança, pergunte.
3. Se houver alterações já preparadas fora da seleção, informe e peça uma decisão antes de continuar. Não as inclua, descarte ou retire da área de preparação automaticamente. Para arquivos com alterações misturadas, proponha somente os trechos da tarefa; se não for possível separá-los com segurança, pare e esclareça o escopo.
4. Consulte a branch de destino no `origin` com uma operação de leitura, como `git ls-remote`, e identifique todos os commits locais que o envio incluirá. Não trate referências locais possivelmente desatualizadas como confirmação do estado remoto. Se o histórico remoto necessário não estiver disponível localmente, houver divergência ou a consulta falhar, informe a limitação e pare para obter instruções; não faça fetch, pull, merge ou rebase automaticamente. Se a branch remota não existir, explicite sua criação e o histórico que será publicado.
5. Descubra os testes existentes relevantes nas instruções e configurações do repositório, considerando também os commits pendentes. Execute-os antes de solicitar confirmação e registre comando e resultado. Se não houver testes relevantes, continue. Se falharem ou não puderem ser executados, pare e relate; não corrija código, instale dependências ou ignore a falha automaticamente. Se os testes alterarem arquivos, reavalie a seleção antes de continuar.
6. Se não houver alterações nem commits pendentes, informe e encerre. Se houver apenas commits pendentes, siga com uma proposta de envio, sem criar commit vazio.

## Confirmação única

Antes de executar `git add`, `git commit` ou `git push`, apresente:

- Raiz do repositório, branch e URL de envio do `origin`.
- "Arquivos:" com uma lista de até seis caminhos selecionados, em ordem alfabética. Se houver mais, acrescente "+ N arquivos", substituindo N pela quantidade restante; o limite é somente de exibição, não da seleção para o commit. Esclareça trechos selecionados quando necessário e indique alterações fora do escopo somente quando existirem.
- "Mensagem :" com a mensagem completa do commit, em português, respeitando convenções do repositório: um título objetivo e um corpo em tópicos usando `-`, descrevendo o comportamento final, os principais ajustes e sua finalidade. Concentre o resumo das alterações nessa mensagem, sem repeti-lo em um bloco separado.

Não inclua os blocos "Alterações:", "Executarei, nesta ordem:", "Validação:" ou "Commits anteriores pendentes:", nem uma lista dos comandos a executar. Mantenha as verificações de testes e histórico no fluxo, sem apresentar seus resultados rotineiros na proposta. Relate falhas ou impedimentos quando ocorrerem. Se o envio incluir commits anteriores fora da tarefa atual, explicite esse conteúdo adicional com hashes e resumos antes de pedir confirmação; para uma proposta somente de envio, identifique os commits que serão publicados.

Encerre apenas com "Confirma o envio?", sem acrescentar explicações sobre a exigência de confirmação da skill. Uma resposta afirmativa, como "sim", "confirmo" ou "pode", autoriza preparar a seleção aprovada, criar o commit e concluir o envio; quando houver somente commits existentes, autoriza apenas seu envio. Execute até concluir sem pedir uma segunda confirmação se o plano aprovado continuar igual. Discutir a proposta ou aprovar apenas parte dela não autoriza as demais ações.

## Execução e resultado

1. Após a confirmação, confira novamente repositório, branch, remoto, commits pendentes e conteúdo selecionado. Se houver mudanças relevantes no conjunto aprovado, apresente uma proposta atualizada e solicite nova confirmação. Alterações fora do escopo não devem ser incluídas.
2. Prepare somente os arquivos ou trechos aprovados, usando caminhos explícitos a partir da raiz e `--` quando aplicável. Confira o diff preparado: ele deve corresponder integralmente à seleção aprovada. Se houver diferença, pare antes do commit e informe.
3. Crie o commit com a mensagem aprovada. Confira seu conteúdo e hash antes de enviar; não use `--no-verify` para contornar hooks. Se o commit falhar, pare e relate o estado atual, sem executar o push.
4. Execute `git push origin HEAD`. Se falhar ou for rejeitado, preserve o commit local e relate a causa. Não tente reconciliar o histórico automaticamente.
5. Confira o estado local e a referência da branch no `origin`. Informe hash curto, branch, resultado do envio e alterações restantes. Diferencie commit criado localmente de envio confirmado; se a verificação remota falhar, informe que não foi possível confirmar o estado remoto.

Nunca use `--force`, `--force-with-lease`, `commit --amend`, rebase, reset ou comandos que reescrevam o histórico. Não crie commits vazios nem descarte alterações do usuário.
