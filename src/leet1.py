import re

FLAG = open('flag.txt').read()

inp = input('> ')

if re.findall("Hack3r$", txt) or eval(inp) != 1337:
    print('Nope')
else:
    print(FLAG)