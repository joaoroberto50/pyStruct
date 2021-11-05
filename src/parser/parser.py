import re
from tradutor import Tradutor

symbols = [' ', '(', ')', '{', '}', ',', ';', '+', '-', '*', '/', '<', '>', '=', '&', '|', '^']

digts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

tyype = ['int', 'str', 'flt', 'boo']

boo = ['false', 'true']

words = ['int', 'str', 'flt', 'boo', 'if', 'while', 'else', 'show', 'NULL', 'false', 'true', 'func']

opers = ['+', '-', '/', '*', '++', '==', '&&', '||', '<', '>', '<=', '>=', '--', '^']

exemplo = "\nfunc main(){\n\tint a, b, c= -3;\n\tflt x= -5.1, y = 1.1;\n\ta = 11 - 1;\n\tb = a + c;\n\tnome = 'joao';\n\twhile(c== 0){\n\t\tshow(nome);\n\tc--;\n\t}\n\tprint(b);\n\tif(a>c){\n\t\tprint(a);\n\t}else{\n\t\tprint(b);\n\t}\n}\n"
ex2 = "show('Emidios');"

trans = Tradutor()

exemplo = exemplo.split('\n')
exemplo = ''.join(exemplo)
exemplo = exemplo.split('\t')
exemplo = ''.join(exemplo)


def is_id(token):
    return bool(re.match('^[_a-zA-Z]', token))


def is_str(token):
    return bool(re.match('^["\']', token))


def is_flt(token):
    token = token.split('.')
    if len(token) == 2:
        if (token[0][1:].isdigit() or token[0].isdigit()) and token[1].isdigit():
            return True
    return False


def is_int(token):
    if token[0] == '-':
        token = token[1:]
    if token.isdigit():
        return True
    return False


# print(exemplo)


def tokenize(text):
    pilha = ''
    op = ''
    for i in text:
        if op == '-' and i.isdigit():
            pilha += op
            op = ''
        if op:
            if i in symbols and i != ' ' and i != '(':
                op += i
                # i = ' '
            if op in opers:
                trans.replaces(op, 'OP')
                print(f'OP:{op}')
                i = ' '
            if op == '=':
                trans.apply('=', '=')
            op = ''
        if i not in symbols:
            pilha+=i
        else:
            if pilha:
                if pilha in words:
                    if pilha in tyype:
                        trans.type_role(pilha)
                    elif pilha in boo:
                        trans.type(pilha, 'boo')
                    else:
                        trans.replaces(pilha)
                elif is_id(pilha):
                    trans.apply(pilha, 'ID')
                elif is_str(pilha):
                    trans.apply(pilha, 'str')
                elif is_int(pilha):
                    trans.apply(pilha, 'int')
                elif is_flt(pilha):
                    trans.apply(pilha, 'flt')
            pilha = ''
            if i == ';':
                trans.semicolon(';')
            elif(i=='{' or i=='}'):
                trans.braces(i)
            elif(i=='(' or i==')'):
                trans.apply(i)
            elif i == ',':
                trans.apply(i, ',')
            op += i
    


tokenize(exemplo)
print(trans.out_text)