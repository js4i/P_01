# P_01

> O propósito deste template é ter uma estrutura e agilizar o processo de criação das APIs.

## Estrutura do Projeto
``` 
├── P_01
|   ├── app
|   |   ├── config
|   |   |  ├── settings.py
|   |   |  ├── security.py
|   |   ├── models
|   |   ├── schemas
|   |   ├── services
|   |   ├── views
|   |   |   ├── v1
|   |   |   |   ├── endpoints
|   |   |   |         ├── users.py
|   |   |   |    ├── api.py          
|   |   ├── db.py
|   |   ├── main.py
|   ├── tests
|   |   ├── conftest.py
|   |   ├── endpoints
|   |   |   ├── test_users.py
|   |   |   |...
|   ├── README.md
|   ├── requirements.txt
└── ...

```

### Criando um ambiente Virtual e Instalando os requirements

```
$ python3 -m venv venv

$ source venv/bin/activate

$ pip3 install --upgrade pip

$ pip3 install -r requirements.txt

```

### Como rodar?

```
$ uvicorn app.main:app --reload

```
#### testes ?

```
$ pytest