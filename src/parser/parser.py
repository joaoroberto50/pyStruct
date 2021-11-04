import re

symbols = [' ', '(', ')', '{', '}', ',', ';', '+', '-', '*', '/', '<', '>', '=']

words = ['int', 'str', 'flt', 'boo', 'if', 'while', 'else', 'print', 'NULL', 'false', 'true', 'func']

exemplo = "\nfunc main(){\n\tint a, b, c=3;\n\ta = 11 + 1;\n\tb = a + c;\n\tnome = 'joao';\n\twhile(c>0){\n\t\tprint(nome);\n\tc--;\n\t}\n\tprint(b);\n\tif(a>c){\n\t\tprint(a);\n\t}else{\n\t\tprint(b);\n\t}\n}\n"

['']

exemplo = exemplo.split('\n')
exemplo = ''.join(exemplo)
exemplo = exemplo.split('\t')
exemplo = ''.join(exemplo)


pilha = ''
for i in exemplo:
    if i not in symbols:
        pilha+=i
    else:
        if pilha:
            if pilha in words:
                print(f'R: {pilha}')
            else:
                print(pilha)
        pilha = ''