# ScanPortTest

[![Maintainability](https://api.codeclimate.com/v1/badges/05b6e4d246c1227567d9/maintainability)](https://codeclimate.com/github/werdelesmarcio/ScanPort/maintainability) 
[![Build status](https://ci.appveyor.com/api/projects/status/3g3behook0t51ehd?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/scanport) 
[![Django CI](https://github.com/werdelesmarcio/ScanPort/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/werdelesmarcio/ScanPort/actions/workflows/django.yml)
[![CodeQL](https://github.com/werdelesmarcio/ScanPort/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/werdelesmarcio/ScanPort/actions/workflows/codeql-analysis.yml)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_ScanPort&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_ScanPort)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_ScanPort&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_ScanPort)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_ScanPort&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_ScanPort)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_ScanPort&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_ScanPort)
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/ScanPort"> 
<img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/ScanPort"> 

_Repositório para a aplicação ScanPortTest._

## ScanPortTest
É uma aplicação escrita em linguagem **Python** que tem como finalidade fazer um escaneamento
em determinado host-alvo, obedecendo um range de portas que é definido pelo usuário afim de
verificar as portas que estão abertas dentro desse range.

Os argumentos devem ser passados em linha na sequência _aplicação > host-alvo > porta inicial > porta final._

**OBS.: Se sua meta é de escanear apenas uma porta, repita o mesmo valor para porta inicial e final.**

## Começando
Estas são as instruções para que você tenha uma cópia do **ScanPortTest** em sua maquina para fins 
de desenvolvimento e teste.

## Pré-requisitos:
* Funciona em qualquer sistema operacional que esteja com Python na versão 3+ e o pip3;
* Instalar a lib **colorama** usando pip3 install colorama.

## Instalando:
```
git clone https://github.com/werdelesmarcio/ScanPort.git
cd ScanPort
pip3 install -r requirements.txt
python3 scan.py <host-alvo> [init_port] [end_port]
```

Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial
e a porta final. Ele irá verificar quais portas estão com o Status Open.

_OBS.: (Para usuários linux) Para usar como executável, lembrar de dar permissão de execução_
**sudo chmod +x pytcpscan.py**

_Exemplo de resposta obtida na execução_

![image](https://user-images.githubusercontent.com/36682515/156290045-a725fabe-138d-4228-9c91-4b5811582fc1.png)

A aplicação está na versão [1.0.31](https://github.com/werdelesmarcio/ScanPort/releases/tag/1.0.31) _(beta)_. 

## Autor:
* **Werdeles Marcio de C. Soares** - _Desenvolvedor_

## Licença: 
***Este projeto está sob Licença GPL-3.0.***
Consulte o arquivo [de Licença](https://github.com/werdelesmarcio/ScanPort/blob/main/LICENSE) para obter mais detalhes.

## Agradecimentos:
* Obrigado à todos os que apoiam o projeto de alguma forma.

## Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/ScanPort?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/ScanPort?style=for-the-badge">

<img src = "https://www.seekpng.com/png/full/70-701896_python-transparent-background-graphic-design.png?raw=true" width =130 align="Right">
<img src = "https://br.pillbanana.com/wp-content/uploads/2018/07/gpl_generalpubliclicense_logo.png?raw=true" width =230 align="Right">
