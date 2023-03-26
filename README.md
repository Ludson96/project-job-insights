# Repositório do projeto Job Insights 📊

## Módulo: CIÊNCIA DA COMPUTAÇÃO

 Repositório possuí projeto desenvolvido no período que estive na **Trybe**, abordando a conceitos iniciais de `Python`, como: operações básicas, tipos de dados, estrutura condicionais, estrutura de repetição, funções, PEP 257, entrada e saída, manipulação de arquivos CSV, exceções e testes.

## Informações de aprendizados

- Este é um projeto desenvolvido para aprender `Python`;
- Primeiro projeto utilizando `Python`;
- Utilizei o `Pytest` para fazer meus testes.

## Linguagens e ferramentas usadas

[![Git][Git-logo]][Git-url]
[![Python][Python-logo]][Python-url]
[![Pytest][Pytest-logo]][Pytest-url]

## O que foi desenvolvido

Neste projeto, implementei análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com `Flask`. Também escrevi testes para a implementação de uma análise de dados. Por fim, como bônus, tive o desafio de escrever uma rota e view para um recurso novo usando Flask!.

## Habilidades trabalhadas

- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição.
- Utilizar funções built-in do Python.
- Utilizar tratamento de exceções.
- Realizar a manipulação de arquivos.
- Escrever funções.
- Escrever testes com Pytest.
- Escrever seus próprios módulos e importá-los em outros códigos.

## Instruções para instalar e rodar

1. Clone o repo:

    ```bash
    git clone git@github.com:Ludson96/project-job-insights.git
    ```

1. Entre na pasta do repositório que você acabou de clonar:

    ```bash
    cd project-job-insights
    ```

1. Caso não tenha instalado o python, pode usar o docker para utilizar:

    ```bash
    docker-compose up
    ```

1. Crie e ative o ambiente virtual:

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

1. Instale as dependências no ambiente virtual:

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

1. Após o passo acima inicie a aplicação flask:

    ```bash
    run flask
    ```

> `docker-compose.yml` e `html` fornecido pela trybe

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/
