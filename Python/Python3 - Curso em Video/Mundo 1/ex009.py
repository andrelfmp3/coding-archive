# Cores em terminal via ansi

# style: 0 = none, 1 = bold, 4 = underline, 7 = negative
# text: 30 até 37
# back: 40 até 41
    # white, red, green, yellow, blue, purple. cyan, gray

print('\033[1;35;44mTeste\033[m')

print('\033[1;31;40mNegativo\033[m')

print('\033[1;30;42mPositivo\033[m')

nome = "André"
print("Olá {}{}{}, tudo bem?".format('\033[4;35m', nome, '\033[m'))
print('\033[1;37;46mTeste2\033[m')
