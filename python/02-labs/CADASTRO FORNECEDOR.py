nome = "  mARIA oLIVEIRA  "
email = "  MARIA.OLIVEIRA@FORNECEDORA.COM  "
telefone = "(16) 98888-1234"
codigo = "FOR-2026-MO"

nome_corrigido = nome.strip().title() # .strip() para remover espaços do inicio e fim da string, .title() para cada palavra na string comece com letra maiuscula.
email_corrigido = email.strip().lower() #.lower() para que toda a string seja convertida em minuscula.
user = email_corrigido.find('@') # .find() para achar um caracter especifico
usuario = email_corrigido[:user] # [:] metodo de fatiamento [start : stop]
telefone_corrigido = telefone.replace("-", "").replace("(", "").replace(")", "").replace(" ", "") # .replace substitui uma ocorrencia (caractere) especifica por outra.
cod_for = codigo[4:8]
term_com = email_corrigido.endswith('.com') # .endswith() verifica se o final da string possui a ocorrencia indicada

print(f"Nome: {nome_corrigido}")
print(f"Email: {email_corrigido}")
print(f"Usuario: {usuario}")
print(f"Telefone: {telefone_corrigido}")
print(f"Ano: {cod_for}")
print(f"Email termina com .com: {term_com}")
