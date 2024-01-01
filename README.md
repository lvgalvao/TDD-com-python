# TDD com Python

Repositório com o projeto do livro **TDD com Python**

## Programar é como puxar um balde de água de um poço

Em última análise, programar é difícil. Com frequência, somos inteligentes, portanto somos bem-sucedidos. O TDD existe para nos ajudar quando não somos assim tão inteligentes. Kent Beck (que basicamente inventou o TDD) utiliza a metáfora de puxar um balde de água de um poço com uma corda: quando o poço não é muito profundo e o balde não está muito cheio, é fácil. E até mesmo puxar um balde cheio no início é bem fácil. Depois de um tempo, porém, você ficará cansado.

O TDD é como ter uma chave-catraca que permite interromper o seu professo, fazer uma pausa e garantir que não haja retrocessos. Assim, você não precisará ser inteligente o temo todo.

O TDD é uma disciplina, e isso significa que não é algo que surge naturalmente; como muitas das compensações não são imediatas, mas só aparecem no longo prazo, você precisará se forçar a segui-lo no momento. 

## Como executar a aplicação

Utilizamos o Django para construir uma aplicação de 'To-do'

1) Clonar o repositório
```bash
git clone tdd-com-python
cd tdd-com-python
```

2) Configurar ambiente virtual com versão do Python e bibliotecas do projeto
```bash
pyenv install 3.6.15
pyven use 3.6.15
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3) Para executar a aplicação utilizar o comando
```bash
python superlists/manage.py runserver
```

## Como testar a aplicação

### Teste funcional

Nesse projeto utilizamos o Selenium para testar interações com o usuário

Para executar o testes utilizar o comando

```bash
python tests/functional_tests.py
```

## Requisitos do projeto

- Firefox
- Geckodriver