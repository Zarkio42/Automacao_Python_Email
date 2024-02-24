## Automação para tratamento de emails
Surgindo a necessidade de tratar emails que compõem a base de dados de automações de email que minha empresa utiliza, a fim de evitar banimentos ou bloqueios, criei esse código em python para facilitar o processo!

<p align="center">
  <img src="https://www.pngkit.com/png/full/940-9408119_explonksions-distorted-thinking-emoji-png.png" width="200"/>
</p>

### Introdução:
Essa automação usa a biblioteca do pandas para manipulação de dados em arquivos csv e xlsx.

Instale usando  o pip: *`pip install pandas`*
Instale também a dependencia openpyxl: *`pip install openpyxl`*

A ideia dessa automação é ler um arquivo excel de sua escolha, realizar algumas operações com os dados de detreminada coluna ou colunas (por exemplo, remover linhas que contém emails que possivelmente não existem), e depois atualizar essa planilha com as alterações necessárias.

Além disso ainda é gerado um log em TXT (fica na pasta TXT) para análise.

O código conta também com um executável localizado na pasta "dist" do projeto.

Caso você faça alguma alteração no código, o executável só estará levando em consideração suas modificações se você refizer-lo

### Utilize o seguinte código no cmd, dentro de sua pasta com o script.py:

*`pyinstaller --onefile --name meu_programa seu_script.py`*

Assim ele pode ser executado sem necessidade do Python instalado.

O script é dividido em 3 partes principais:

1) Leitura dos dados (em formato CSV e XLSX);
2) Tratamento dos dados;
3) Escrita dos dados de volta para a planilha base de uma automação de emails.
