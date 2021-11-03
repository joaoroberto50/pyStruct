

def _error_msg(msg):
    return f'ERRO: Theres a open {msg} with no close'

# Delimiters {} () "" ''
# Roles: 
# S -> {S} | (A) | "S" | 'S' | $
# A -> (A) | $
def check(text):
    pilha = ''
    for item in text:
        if item == '{':
            if not pilha or pilha[-1] == '{':
                pilha += '{'
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return _error_msg('(')
        if item == '(':
            if pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                pilha += '('
        if item == ')':
            if pilha[-1] == '(':
                pilha = pilha[:-1]
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return _error_msg()
        if item == '}':
            if pilha[-1] == '{':
                pilha = pilha[:-1]
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return 1
        if item == "'":
            if not pilha or pilha[-1] != "'" and pilha[-1] != '"':
                pilha += "'"
            elif pilha[-1] == "'":
                pilha = pilha[:-1]
        if item == '"':
            if not pilha or pilha[-1] != '"' and pilha[-1] != "'":
                pilha += '"'
            elif pilha[-1] == '"':
                pilha = pilha[:-1]
        print(item)
    return pilha