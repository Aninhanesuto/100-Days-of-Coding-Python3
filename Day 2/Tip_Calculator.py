print('Welcome to the tip calculator!')
gorjeta = float(input('What was the total bill? $'))
porcentagem = int(input('How much tip would you like to give? 10, 12, or 15? '))
pessoas = int(input('How many people to split the bill? '))
calc = (gorjeta * (porcentagem/100 + 1)) / pessoas
# aproximado = round(calc, 2)
aproximado = "{:.2f}".format(calc)
print(f"Each person should pay: $ {aproximado}")

