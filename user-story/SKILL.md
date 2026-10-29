---
name: user-story
description: Crie uma User Story em português a partir de documentos, transcrições, links, contexto informado ou código de uma branch. Use quando o usuário pedir para elaborar ou documentar uma história com narrativa de negócio, critérios de aceite, solução técnica e informações adicionais.
---

# User Story

Produza uma única User Story em Markdown, pronta para revisão e cópia. Responda em português. O usuário pode pedir ajustes ou uma divisão posterior; não divida a história por iniciativa própria.

## Levantamento do contexto

- Identifique o objetivo e as fontes indicadas. Leia os materiais acessíveis antes de escrever: texto da conversa, anexos, documentos, transcrições, links e, quando indicada, a branch relevante. Use as ferramentas disponíveis para cada fonte, respeitando acesso e autorização. Se uma fonte essencial não estiver acessível, peça o conteúdo ou o acesso necessário.
- Em uma branch, examine os arquivos e o diff relevantes para a funcionalidade. Diferencie o que o código comprova do que documentos ou falas apenas propõem. Para uma implementação já concluída, descreva o comportamento verificado, sem atribuir ao código requisitos que ele não demonstra.
- Compare regras, atores, objetivos e comportamento entre as fontes. Se houver divergência ou faltar uma decisão essencial para concluir a história, apresente a questão concreta ao usuário e espere a resposta. Faça apenas perguntas que a pesquisa disponível não resolve.
- Não invente regras de negócio, integrações, contratos, arquitetura ou comportamento. Se houver lacuna não essencial, registre-a de forma objetiva em **Informações Adicionais** como ponto a confirmar.

## Redação

Use um título curto seguido de exatamente estas quatro seções, nesta ordem:

```markdown
# Título da história

## Narrativa de Negócio

## Critérios de Aceite

## Solução Técnica

## Informações Adicionais
```

- **Narrativa de Negócio:** em um ou dois parágrafos, explique a necessidade, quem é beneficiado, o objetivo e o valor esperado. Quando útil, resuma a situação atual e a mudança pretendida. Mantenha regras detalhadas nos critérios de aceite.
- **Critérios de Aceite:** use tópicos para comportamentos e regras observáveis. Cada tópico deve permitir verificar se a funcionalidade atende ao esperado; inclua condições, resultados e exceções relevantes que as fontes sustentem. Evite transformar tarefas de implementação em critérios.
- **Solução Técnica:** descreva a arquitetura em nível geral, os sistemas ou componentes envolvidos e o fluxo principal. Cite detalhes técnicos específicos somente quando estiverem confirmados nas fontes e forem úteis para entender a solução. Para código já implementado, relate a solução encontrada; para trabalho futuro, descreva a abordagem definida, sem apresentar hipótese como decisão.
- **Informações Adicionais:** reúna premissas, dependências, contexto complementar, pontos não essenciais a confirmar e referências úteis às fontes consultadas. Use links, caminhos, commits ou trechos localizáveis quando disponíveis. Não crie seções separadas para esses itens e não polua os critérios com citações.

Antes de entregar, confira se há uma única história, se a narrativa tem no máximo dois parágrafos, se os critérios são verificáveis, se a solução técnica não extrapola as evidências e se aparecem apenas o título e as quatro seções combinadas.

Referência de elaboração: [Como criar uma User Story?](https://guilhermerodriguescosta.wordpress.com/2020/01/19/como-criar-uma-user-story/). Use a orientação sobre narrativa breve e critérios de aceite; o formato de saída desta skill prevalece sobre as seções adicionais do artigo.
