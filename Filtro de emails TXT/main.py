import pandas as pd

arq = "C:/Users/User/Downloads/Filtro de emails TXT/Filtro de emails TXT/TXT/filtro.txt"
arq_excel = input('Insira o caminho do documento excel desejado: ')
colunas = [input('Digite o nome da coluna como aparece no excel: ')]

lista_emails_retiradas = ["123@globo.com","123@gmail.com","12345@globo.com","123456@gamil.com",
                          "123456@gmail.com","123456@gmail.com","123456emillencamila@gmail.com","12345lay@globo.com",
                          "1234ana12santos@gmail.com","123binha@gmail.com","teste","nãotem@gmail.com","@.com","gmaail","123","sms",
                          "@email..lojasmm","@@",",","..com", "nãotem", "^"
                          ]

lista_emails_retiradas = [email.lower() for email in lista_emails_retiradas]


try:

    df_excel_sujo = pd.read_excel(arq_excel)
    conteudo_excel = df_excel_sujo.to_csv(index=False, header=True, columns=colunas).split("\n")

    with open(arq, 'w', encoding='utf-8') as a:
        for linha in conteudo_excel:
            a.writelines(linha)
    
    with open(arq, 'r', encoding='utf-8') as a:

        conteudo = a.readlines()
        
    with open(arq, 'w', encoding='utf-8') as a:
        for linha in conteudo:
            linha_minuscula = linha.lower()
            if any(email in linha_minuscula for email in lista_emails_retiradas) or not "@" in linha_minuscula:
                a.write("")
            else:
                a.write(linha)
    
    df_txt = pd.read_csv(arq, header=None)

    df_excel_tratado = pd.read_excel(arq_excel)

    df_excel_tratado[colunas] = df_txt          
        
    df_excel_tratado.to_excel(arq_excel, index=False)

    print('Tratamento concluído com sucesso')

except FileNotFoundError:
    print(f"O arquivo '{arq}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")