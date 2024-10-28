## Mently API

## Pré-requisitos

- **Docker**
- **Docker compose**

## Setup
Necessário baixar os repositórios dos submodulos. Para isso:
- Rode 
```shell
git submodule update --init --recursive
```
- Em seguida, rode 
```shell
git submodule foreach --recursive 'git checkout main'
```

## Sincronizar submodules com a main
Rodar
```shell
git submodule foreach --recursive 'git checkout main'
git submodule update --remote --merge 
```

## Execução
Rode o projeto com 
```shell
docker-compose up
```