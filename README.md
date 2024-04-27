# Instagram Content Strategy Automation

## Visão Geral

Este projeto tem o objetivo de automatizar a estratégia de conteúdo do Instagram, integrando pesquisa de mercado, planejamento estratégico de conteúdo, descrição visual, redação e compilação de relatórios para criar uma estratégia de conteúdo coesa e eficaz. Utiliza um framework de agentes para coordenar e executar tarefas específicas, culminando em um plano de conteúdo semanal que está alinhado com as tendências atuais e preferências do público.

## Instalação

Certifique-se de ter o Python >=3.10 <=3.13 instalado no seu sistema. Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciamento de dependências e manuseio de pacotes, oferecendo uma experiência de configuração e execução perfeita.

Primeiro, se ainda não o fez, instale o Poetry:

```bash
pip install poetry
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

Segundo, bloqueie as dependências e depois instale-as:
```bash
poetry lock
```
```bash
poetry install
```
### Personalizando

**Adicione sua `OPENAI_API_KEY` no arquivo  `.env`**
**Adicione sua `SERPER_API_KEY` no arquivo  `.env`**

## Funcionamento

O sistema é composto por quatro agentes principais:

- **Pesquisador de Mercado do Instagram**: Analisa tendências, atividades de concorrentes e hashtags populares no Instagram.
- **Estrategista de Conteúdo do Instagram**: Desenvolve um calendário de conteúdo semanal baseado em pesquisas.
- **Descritor Visual do Instagram**: Cria descrições detalhadas das imagens que correspondem à estratégia de conteúdo.
- **Redator do Instagram**: Escreve cópias envolventes para as postagens, seguindo a estratégia definida.

Estas etapas são concretizadas em tarefas definidas no arquivo `tasks.yaml` e executadas de acordo com a sequência programada no `crew.py`.

## Features

- **Automated Market Research**: Coleta dados em tempo real para revelar conteúdo de alto desempenho no Instagram.
- **Content Calendar Development**: Planeja o conteúdo visual e textual da semana.
- **Visual Content Description**: Gera prompts detalhados para criação de imagens via IA.
- **Copywriting**: Produz cópias alinhadas com a voz da marca e com SEO.
- **Comprehensive Reporting**: Compila um relatório detalhado da estratégia de conteúdo para a semana.

## Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute isto a partir da pasta raiz do seu projeto:

```bash
poetry run instagram
```

Este comando inicializa a equipe do Instagram, montando os agentes e atribuindo-lhes tarefas conforme definido na sua configuração.

Este exemplo criará uma pasta 'relatórios' com os relatórios das tarefas descritas anteriormente.

## License
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contact
Para quaisquer outras questões ou comentários, entre em contato pelo e-mail: [ricardo.jnf1@gmail.com].