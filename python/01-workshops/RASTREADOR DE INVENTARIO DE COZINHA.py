# Quantidade inicial de ingredientes disponíveis na cozinha.
available_eggs = 1
available_flour = 2
available_sugar = 3


# Define uma função que consulta e exibe o estoque da cozinha.
def check_kitchen_stock():

    # Soma as quantidades dos três ingredientes.
    # Estas variáveis foram declaradas fora da função.
    total_items = available_eggs + available_flour + available_sugar

    # Exibe o total de itens disponíveis.
    print(f"The kitchen has {total_items} total items:")

    # Exibe a quantidade de cada ingrediente.
    print(f"- {available_eggs} eggs")
    print(f"- {available_flour} flour")
    print(f"- {available_sugar} sugar")


# Chama a função para mostrar o estoque inicial.
check_kitchen_stock()


# Define uma função que tenta utilizar determinada quantidade de ovos.
#
# Parâmetros:
# available_eggs: quantidade disponível recebida pela função.
# eggs_to_use: quantidade que desejamos utilizar.
def use_eggs(available_eggs, eggs_to_use):

    # Verifica se a quantidade solicitada é maior
    # que a quantidade disponível.
    if eggs_to_use > available_eggs:

        # Informa que não existem ovos suficientes.
        print("The kitchen does not have enough eggs.")

        # Retorna a quantidade original, sem descontar ovos.
        return available_eggs

    # Executado quando existe quantidade suficiente.
    print(f"{eggs_to_use} egg(s) used out of {available_eggs} available.")

    # Calcula e retorna a quantidade restante.
    # IMPORTANTE: return não altera automaticamente
    # a variável available_eggs declarada fora da função.
    return available_eggs - eggs_to_use


# Chama use_eggs(), passando:
# 1º argumento: quantidade disponível (1).
# 2º argumento: quantidade a utilizar (1).
#
# A função retorna 0, mas o resultado NÃO é armazenado.
use_eggs(available_eggs, 1)

# Exibe a variável externa, que continua valendo 1.
print(available_eggs)


# Define uma função responsável por preparar um ovo frito.
#
# O parâmetro available_eggs recebe a quantidade disponível
# no momento em que a função é chamada.
def make_fried_egg(available_eggs):

    # Verifica se existe pelo menos um ovo disponível.
    # A comparação produz True ou False.
    has_enough_eggs = available_eggs >= 1

    # Se existir pelo menos um ovo, executa este bloco.
    if has_enough_eggs:

        # Chama use_eggs() para utilizar um ovo.
        #
        # A função devolve a quantidade restante.
        # Esse valor é atribuído ao parâmetro local
        # available_eggs, substituindo o valor anterior.
        available_eggs = use_eggs(available_eggs, 1)

        # Informa que o ovo frito foi preparado.
        print("Made a fried egg. Yummy!")

    # Caso não exista nenhum ovo disponível:
    else:
        print("Could not make a fried egg. Not enough eggs!")

    # Devolve a quantidade atual de ovos.
    return available_eggs


# Chama make_fried_egg(), passando a quantidade atual.
#
# A função retorna a quantidade restante.
# Agora SIM esse resultado é armazenado na variável
# available_eggs declarada fora da função.
available_eggs = make_fried_egg(available_eggs)


# Consulta novamente o estoque.
# Agora a variável externa available_eggs vale 0.
check_kitchen_stock()
