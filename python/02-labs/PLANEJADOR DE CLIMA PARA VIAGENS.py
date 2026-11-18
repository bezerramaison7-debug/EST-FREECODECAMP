# 1. DEFINIÇÃO DAS VARIÁVEIS (Os dados da nossa viagem)
# Aqui guardamos as informações que o programa vai analisar.
distance_mi = 6            # Distância em milhas (número inteiro ou decimal)
is_raining = False         # Está chovendo? (True = Sim, False = Não)
has_bike = True            # Tem bicicleta? (True = Sim, False = Não)
has_car = True             # Tem carro? (True = Sim, False = Não)
has_ride_share_app = True  # Tem app de carona, tipo Uber? (True = Sim, False = Não)


# 2. VERIFICAÇÃO DE VALOR VÁLIDO (Truthy vs Falsy)
# Em Python, o número 0 ou None são considerados "falsy" (falsos).
# Este primeiro 'if' garante que a viagem só seja avaliada se houver uma distância real (diferente de 0).
if distance_mi:

    # FAIXA 1: Viagens curtas (até 1 milha)
    # Verifica se a distância é menor ou igual a 1 E ('and') se NÃO ('not') está chovendo.
    # Como a distância é curta, dá para ir a pé se o tempo estiver seco.
    if distance_mi <= 1 and not is_raining:
        print(True)

    # FAIXA 2: Viagens médias (mais de 1 milha até 6 milhas)
    # O 'elif' (abreviação de "else if") só é testado se a condição de cima for falsa.
    # Exige 4 coisas ao mesmo tempo ('and'):
    # 1. Distância maior que 1
    # 2. Distância menor ou igual a 6
    # 3. Ter uma bicicleta (has_bike)
    # 4. Não estar chovendo (not is_raining)
    elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
        print(True)

    # FAIXA 3: Viagens longas (mais de 6 milhas)
    # Exige que a distância seja maior que 6 E ('and') que tenha carro OU ('or') app de carona.
    # Os parênteses () são obrigatórios aqui para o Python resolver o 'or' antes do 'and'.
    # Repare que aqui não importa se está chovendo, pois você estará dentro de um veículo!
    elif distance_mi > 6 and (has_car or has_ride_share_app):
        print(True)

    # CASO NENHUMA CONDIÇÃO ACIMA SEJA ATENDIDA
    # Se a distância for válida, mas você não tiver o meio de transporte adequado
    # ou o clima impedir o trajeto, o programa cai aqui.
    else:
        print(False)

# 3. CASO A DISTÂNCIA SEJA FALSY (ex: 0 milhas)
# Este 'else' pertence lá ao primeiro 'if distance_mi:'.
# Se a distância for 0, o programa pula tudo lá de cima e vem direto para cá.
else:
    print(False)
