# PVU - Farm Calculator

![texto](https://img.shields.io/static/v1?label=linguagem&message=vue3&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=netlify&color=orange&style=flat-square "linguagem")

![imagem](https://user-images.githubusercontent.com/46504678/135247688-6dd0dd04-758f-4e41-b431-a0b47bdc809f.png)


Projeto desenvolvido para auxiliar jogadores de plant vs undead a calcular uma estimativa de seus lucros. **Sem considerar o clima e corvos que aparecerão durante o periodo.**

Link da aplicação: https://pvu-farm-calculator.netlify.app/

# Número de visualizações do projeto

![imagem](https://user-images.githubusercontent.com/46504678/143089688-4237c5e8-9eb6-41d0-93f4-d887222dc8d7.png)



# :world_map: Conteúdo
1. [O que faz](#sparkles-o-que-faz)  
2. [Pré-requisitos](#warning-pré-requisitos)
5. [Como instalar](#cd-como-instalar)
3. [Como executar](#arrow_forward-como-executar)
6. [Desenvolvimento](#construction-desenvolvimento)

## :sparkles: O que faz

O que já existe:

:heavy_check_mark: Calcula o lucro, gasto, produzido e o faturamento no período de 7, 14 e 30 dias.

:heavy_check_mark: Adição de plantas de forma dinâmica. E também é possível adicionar utilizando o ID de uma planta NFT.

:heavy_check_mark: Possibilidade de adicionar uma planta sem a necessidade de ter um ID de NFT. Apenas colocando quanto a mesma produz e o seu custo.

:heavy_check_mark: Suporte para 3 idiomas: English :flag_us:  Português :flag_br: e Español: :flag_es:

:heavy_check_mark: Ultima cotação em USD da moeda PVU.

O que será implementado:

:wrench: Visualização de estimativa de quando as plantas serão colhidas. Utilizando um calendário 

## :warning: Pré-requisitos

- [Vue3](https://v3.vuejs.org) (obrigatório)

## :cd: Como instalar

No diretório do projeto, execute o seguinte comando:

```bash
npm install
```

## :arrow_forward: Como executar

Após ter instalados as dependências com o NPM, basta utilizar o seguinte comando para rodar o projeto:

```bash
npm run server
```

## :construction: Desenvolvimento

Todo o desenvolvimento pode ser realizado apenas com o NPM. A api em breve será exposta e terá sua branch para a manutenção/implementações.

### :green_apple: CI/CD

Todo o processo de CI/CD é executado utilizando o amplify. O mesmo cuida tanto do ambiente da branch main, quanto dos ambientes gerados nos pull requests. 
