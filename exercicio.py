entrada = input('Digite um número:')

try: 
    entrada = int(entrada)
    divisao = 1 / entrada

except ZeroDivisionError:
    print('Não é possível dividir por zero')

except ValueError:
    print('Você digitou uma string e não um número')

else:
    print(f'Resultado da divisão:{divisao}')