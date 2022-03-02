# ScanPortTest

[![Maintainability](https://api.codeclimate.com/v1/badges/05b6e4d246c1227567d9/maintainability)](https://codeclimate.com/github/werdelesmarcio/ScanPort/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/05b6e4d246c1227567d9/test_coverage)](https://codeclimate.com/github/werdelesmarcio/ScanPort/test_coverage) 
[![Build status](https://ci.appveyor.com/api/projects/status/3g3behook0t51ehd?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/scanport) 
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_PyTCPScan) 
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/PyTCPScan"> 
<img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/PyTCPScan"> 
<img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

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
_Não é necessário instalar o ScanPortTest (apenas os requisitos citados acima)_

---

_OBS.: (Para usuários linux) Para usar como executável, lembrar de dar permissão de execução_
**sudo chmod +x pytcpscan.py**

---

## Execução 
Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial
e a porta final. Ele irá verificar quais portas estão com o Status Open.

**./scan.py  [target] [init_port] [final_port]**

_Exemplo de resposta obtida na execução_

![image](https://user-images.githubusercontent.com/36682515/156290045-a725fabe-138d-4228-9c91-4b5811582fc1.png)

Está em sua versão 1.0.0 _(beta)_ e ainda está em fase de desenvolvimento.

## Autor:
* **Werdeles Marcio de C. Soares** - _Desenvolvedor_

## Licença: 
***Este projeto está sob Licença GPL-3.0.***
Consulte o arquivo [de Licença](https://github.com/werdelesmarcio/ScanPort/blob/master/Archives/LICENSE) para obter mais detalhes.

## Agradecimentos:
* Obrigado à todos os que apoiam o projeto de alguma forma.

## Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan?style=for-the-badge">

<img src = "https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/SoftwareLivre.png?raw=true" width =130 align="Right">
<img src = "https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/PoweredByLinux.png?raw=true" width =80 align="Right">
