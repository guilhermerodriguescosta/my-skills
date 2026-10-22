---
name: git-commit-push
description: >-
  Use esta skill EXCLUSIVAMENTE quando o usuário marcar ou mencionar explicitamente @git-commit-push (ou $git-commit-push).
  NÃO ative esta skill para pedidos genéricos de git, commit ou push que não incluam a menção explícita.
  Revisa o conteúdo a publicar, executa testes relevantes somente com --test e aceita --confirm para concluir o envio sem pergunta adicional.
---

# Commit e envio ao origin

Use esta skill única e exclusivamente quando o usuário marcar ou referenciar explicitamente `@git-commit-push` (ou `$git-commit-push`). Pedidos gerais de commit/push em texto sem a menção explícita à skill NÃO devem acionar este fluxo. Menções apenas para discutir ou editar a própria skill não iniciam esse fluxo. Responda em português.

## Parâmetros opcionais

- `--test`: executa os testes automatizados existentes relevantes antes do envio. Exemplo: `$git-commit-push --test`.
- `--confirm`: autoriza preparar, criar o commit e enviar sem pedir confirmação adicional. Inclui todas as alterações do repositório e os commits locais pendentes. Exemplo: `$git-commit-push --confirm`.
- Os parâmetros podem ser combinados: `$git-commit-push --test --confirm`.
- Sem `--test`, não descubra nem execute testes automatizados por iniciativa da skill. Preserve os hooks do repositório.

## Revisão e testes

1. Identifique o repositório pelo contexto da tarefa, sem assumir que o diretório atual é o correto. Confira sua raiz, branch e URL de envio do `origin`. Se houver ambiguidade, pergunte; se faltar o remoto, houver HEAD destacado ou conflitos não resolvidos, pare e informe.
2. Na raiz do repositório, examine alterações preparadas, não preparadas e arquivos novos, incluindo o conteúdo relevante. Sem `--confirm`, selecione somente alterações relacionadas à tarefa. Com `--confirm`, selecione todas as alterações do repositório, mesmo fora da tarefa. Não use `git add .` nem altere arquivos para facilitar o commit. Se não conseguir identificar com segurança o conteúdo selecionado, pare e informe.
3. Sem `--confirm`, se houver alterações já preparadas fora da seleção, informe e peça uma decisão antes de continuar. Não as inclua, descarte ou retire da área de preparação automaticamente. Para arquivos com alterações misturadas, proponha somente os trechos da tarefa; se não for possível separá-los com segurança, pare e esclareça o escopo. Com `--confirm`, as alterações já preparadas também integram a seleção.
4. Consulte a branch de destino no `origin` com uma operação de leitura, como `git ls-remote`, e identifique todos os commits locais que o envio incluirá. Não trate referências locais possivelmente desatualizadas como confirmação do estado remoto. Se o histórico remoto necessário não estiver disponível localmente, houver divergência ou a consulta falhar, informe a limitação e pare para obter instruções; não faça fetch, pull, merge ou rebase automaticamente. Se a branch remota não existir, explicite sua criação e o histórico que será publicado.
5. Somente se o usuário informar o parâmetro `--test` na solicitação do fluxo, descubra os testes automatizados existentes relevantes nas instruções e configurações do repositório, considerando também os commits pendentes. Execute-os antes da confirmação ou do envio e registre comando e resultado. Se não houver testes relevantes, continue. Se falharem ou não puderem ser executados, pare e relate; não corrija código, instale dependências ou ignore a falha automaticamente. Se os testes alterarem arquivos, reavalie a seleção antes de continuar.
6. Se não houver alterações nem commits pendentes, informe e encerre. Se houver apenas commits pendentes, siga com o envio, sem criar commit vazio.

## Autorização e apresentação

Sem `--confirm`, antes de executar `git add`, `git commit` ou `git push`, apresente:

- Raiz do repositório, branch e URL de envio do `origin`.
- "Arquivos:" com uma lista de até seis caminhos selecionados, em ordem alfabética. Se houver mais, acrescente "+ N arquivos", substituindo N pela quantidade restante; o limite é somente de exibição, não da seleção para o commit. Esclareça trechos selecionados quando necessário e indique alterações fora do escopo somente quando existirem.
- "Mensagem :" com a mensagem completa do commit, em português, respeitando convenções do repositório: um título objetivo e um corpo em tópicos usando `-`, descrevendo o comportamento final, os principais ajustes e sua finalidade. Concentre o resumo das alterações nessa mensagem, sem repeti-lo em um bloco separado.

Não inclua os blocos "Alterações:", "Executarei, nesta ordem:", "Validação:" ou "Commits anteriores pendentes:", nem uma lista dos comandos a executar. Mantenha a verificação de histórico e, quando `--test` for informado, as verificações de testes no fluxo, sem apresentar seus resultados rotineiros na proposta. Relate falhas ou impedimentos quando ocorrerem. Se o envio incluir commits anteriores fora da tarefa atual, explicite esse conteúdo adicional com hashes e resumos antes de pedir confirmação; para uma proposta somente de envio, identifique os commits que serão publicados.

Sem `--confirm`, encerre apenas com "Confirma o envio?", sem acrescentar explicações sobre a exigência de confirmação da skill. Uma resposta afirmativa, como "sim", "confirmo" ou "pode", autoriza preparar a seleção aprovada, criar o commit e concluir o envio; quando houver somente commits existentes, autoriza apenas seu envio. Execute até concluir sem pedir uma segunda confirmação se o plano aprovado continuar igual. Discutir a proposta ou aprovar apenas parte dela não autoriza as demais ações.

Com `--confirm`, a solicitação já autoriza o envio de toda a seleção revisada e dos commits locais pendentes. Não apresente a proposta nem pergunte "Confirma o envio?". Conclua o fluxo e mostre somente o resultado final no formato definido abaixo. Se houver impedimento, pare e informe-o. Não use a autorização para ignorar testes com falha, divergência remota ou outros impedimentos técnicos.

## Execução e resultado

1. Antes de preparar, confira novamente repositório, branch, remoto, commits pendentes e conteúdo selecionado. Sem `--confirm`, se houver mudanças relevantes no conjunto aprovado, apresente uma proposta atualizada e solicite nova confirmação. Com `--confirm`, revise novamente a seleção completa. Se não conseguir verificá-la com segurança, pare e informe.
2. Prepare somente os arquivos ou trechos selecionados, usando caminhos explícitos a partir da raiz e `--` quando aplicável. Confira o diff preparado: ele deve corresponder integralmente à seleção revisada. Se houver diferença, pare antes do commit e informe.
3. Crie o commit com a mensagem elaborada na revisão. Confira seu conteúdo e hash antes de enviar. Se o commit falhar, pare e relate o estado atual, sem executar o push.
4. Execute `git push origin HEAD`. Se falhar ou for rejeitado, preserve o commit local e relate a causa. Não tente reconciliar o histórico automaticamente.
5. Confira o estado local e a referência da branch no `origin`. Informe raiz do repositório, branch, URL de envio do `origin`, "Arquivos:" com até seis caminhos em ordem alfabética e "+ N arquivos" quando necessário, "Mensagem :" com a mensagem completa do novo commit (se houver), hash curto, resultado do envio e alterações restantes. Se apenas commits existentes forem enviados, identifique-os por hash e resumo. Com `--confirm`, apresente esses dados somente no resultado final. Diferencie commit criado localmente de envio confirmado; se a verificação remota falhar, informe que não foi possível confirmar o estado remoto.

Nunca use `--force`, `--force-with-lease`, `commit --amend`, rebase, reset ou comandos que reescrevam o histórico. Não crie commits vazios nem descarte alterações do usuário.
