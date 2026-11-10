email = "alice.johnson@company.com"  # Exemplo de email
print(f"Email: {email}")

at_position = email.find("@")  # Encontrando a posição do caractere "@" no email.
print(f"Position of @: {at_position}")

username = email[:at_position]  # Extraindo nome de usuário de email.
print(f"Username: {username}")

has_at = "@" in email  # Verificando se o email contém o caractere "@".
print(
    f"Has @ symbol: {has_at}"
)  # Retorna True se o email contém o caractere "@" e False caso contrário.

has_com = ".com" in email  # Verificando se o email contém o domínio ".com".
print(
    f"Has .com: {has_com}"
)  # Retorna True se o email contém o domínio ".com" e False caso contrário.

messy_name = "  sARah dAVis  "  # Exemplo de nome com espacos, letras maiúsculas e minúsculas misturadas.
print(f"Original name: '{messy_name}'")

clean_name = (
    messy_name.strip().title()
)  # Removendo espaços em branco e convertendo para o formato de título.
print(f"Clean name: '{clean_name}'")

messy_email = "  SARAH.DAVIS@COMPANY.COM  "  # Exemplo de email com letras maiúsculas.
clean_email = (
    messy_email.strip().lower()
)  # Removendo espaços em branco e convertendo para letras minúsculas.
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

name_badge = clean_name.upper()  # Convertendo o nome limpo para letras maiúsculas.
print(f"Name badge: {name_badge}")

at_pos = clean_email.find("@")  # Encontrando a posição do caractere "@" no email limpo.
email_user = clean_email[:at_pos]  # Extraindo o nome de usuário do email limpo.
print(f"Email: {clean_email}")
print(f"Username: {email_user}")

display_name = email_user.replace(
    ".", " "
).title()  # Substituindo pontos por espaços e convertendo para o formato de título.
print(f"Display name: {display_name}")

phone = "123-456-7890"
phone_clean = phone.replace("-", "")  # Removendo os traços do número de telefone.
print(f"Phone with dashes: {phone}")
print(f"Phone without dashes: {phone_clean}")

full_address = "123 Main Street, Sprinfield, IL"
address_parts = full_address.split(",")  # Dividindo o endereço completo em partes.
print(f"Address parts: {address_parts}")

rejoined = " | ".join(
    address_parts
)  # Reunindo as partes do endereço com um separador personalizado.
print(f"Rejoined: {rejoined}")

employee_code = 'EMP-2024-SD'  # Exemplo de código de identificação de funcionário.
starts_with_emp = employee_code.startswith('EMP')  # Verificando se o código começa com "EMP".

ends_with_com = clean_email.endswith('.com')  # Verificando se o email limpo termina com ".com".

print(f"Code: {employee_code}")
print(f"Starts with EMP: {starts_with_emp}")
print(f"Clean email: {clean_email}")
print(f"Ends with .com: {ends_with_com}")

dot_count = clean_email.count('.')  # Contando quantas vezes o caractere "." aparece no email limpo.
dash_count = employee_code.count('-')  # Contando quantas vezes o caractere "-" aparece no código do funcionário.
print(f"Dots in email: {dot_count}")
print(f"Dashes in code: {dash_count}")
