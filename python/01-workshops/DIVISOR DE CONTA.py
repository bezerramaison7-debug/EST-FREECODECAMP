running_total = 0  # Inicializando o valor total da conta em zero.
num_of_friends = 4  # Definindo a quantidade de amigos que irão dividir a conta.

appetizers = 37.89  # Valor gasto com entradas.
main_courses = 57.34  # Valor gasto com pratos principais.
desserts = 39.39  # Valor gasto com sobremesas.
drinks = 64.21  # Valor gasto com bebidas.

running_total += appetizers + main_courses + desserts + drinks  # Somando todas as despesas ao valor total da conta.
print(f"Total bill so far: {running_total}")  # Exibindo o valor total da conta antes da gorjeta.

tip = running_total * 0.25  # Calculando a gorjeta de 25% sobre o valor total da conta.
print(f"Tip amount: {tip}")  # Exibindo o valor calculado da gorjeta.

running_total += tip  # Adicionando o valor da gorjeta ao total da conta.
print(f"Total with tip: {running_total}")  # Exibindo o valor total da conta com a gorjeta incluída.

final_bill = running_total / num_of_friends  # Dividindo o valor total da conta igualmente entre os quatro amigos.
print(f"Bill per person: {final_bill}")  # Exibindo o valor que cada amigo deverá pagar antes do arredondamento.

each_pays = round(final_bill, 2)  # Arredondando o valor individual para duas casas decimais.
print(f"Each person pays: {each_pays}")  # Exibindo o valor final arredondado que cada amigo deverá pagar.
