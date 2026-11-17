# --- 1. DADOS INICIAIS (VARIÁVEIS) ---
# Aqui guardamos as informações básicas do cliente e do ingresso.
base_price = 15          # Preço base do ingresso (número inteiro)
age = 21                 # Idade do usuário
seat_type = 'Gold'       # Tipo de assento escolhido (texto/string)
show_time = 'Evening'    # Horário da sessão ('Evening' = noite)


# --- 2. VERIFICAÇÕES BÁSICAS DE IDADE ---
# O 'if' testa se uma condição é verdadeira. Se for, roda o código indentado (recuado).
if age > 17:
    print('User is eligible to book a ticket')

# Aqui usamos 'if / else' (se / senão) para escolher entre dois caminhos possíveis.
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')


# --- 3. VARIÁVEIS BOOLEANAS (VERDADEIRO OU FALSO) ---
# Valores booleanos (True ou False) funcionam como interruptores de liga/desliga.
is_member = False        # O usuário é membro VIP? Não (False).
is_weekend = False       # A sessão é no fim de semana? Não (False).


# --- 4. CÁLCULO DE DESCONTO ---
discount = 0             # Começamos assumindo que o desconto é zero.

# O operador 'and' exige que AS DUAS condições sejam verdadeiras ao mesmo tempo.
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

# Esta linha não está recuada, então ela roda sempre, independente do if/else acima.
print('Discount:', discount)


# --- 5. CÁLCULO DE TAXAS EXTRAS ---
extra_charges = 0        # Começamos assumindo que não há taxas extras.

# O operador 'or' exige que PELO MENOS UMA das condições seja verdadeira.
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)


# --- 6. REGRA PRINCIPAL DE RESERVA E PREÇO FINAL ---
# Como o Python lê esta condição:
# Pode reservar se tiver 21+ anos OU (tiver 18+ anos E [não for à noite OU for membro]).
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Tudo abaixo está recuado dentro do 'if' principal: só roda se a reserva for permitida!
    service_charges = 0
    
    # 'if / elif / else' permite testar várias opções em sequência (uma após a outra).
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':        # 'elif' significa "senão, se..."
        service_charges = 3
    else:                            # Qualquer outro assento cai aqui
        service_charges = 1

    # O 'f' antes das aspas (f-string) permite inserir variáveis direto dentro das chaves { }.
    print(f'Service charges: {service_charges}')

    # Soma o preço base + taxas e subtrai o desconto para achar o valor final.
    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price}')

# Se a condição principal lá em cima falhar, o Python pula tudo e vem direto para cá:
else:
    print('Ticket booking failed due to restrictions')
