

def _error_msg(msg=''):
    if msg == '{' or msg == '(':
        return f'ERROR: Syntax error. Theres a open {msg} with no close'

    if msg == '}' or msg == ')':
        return f'ERROR: Syntax error. There is an {msg} with no opening.'
    
    if msg == "'" or msg == '"':
        return f'ERROR: Syntax error. There is quotation mark {msg} in open.'
    
    if msg == '':
        return f'ERROR: Syntax error \'{"{"}\'. Not allowed \'{"{ }"}\' inside \'( )\'.'


# Delimiters {} () "" ''
# Roles: 
# S -> {S} | (A) | "S" | 'S' | $
# A -> (A) | "A" | 'A' | $
def check(text):
    pilha = ''
    for item in text:
        if item == '{':
            if not pilha or pilha[-1] == '{':
                pilha += '{'
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return _error_msg()

        if item == '(':
            if pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                pilha += '('

        if item == ')':
            if pilha and pilha[-1] == '(':
                pilha = pilha[:-1]
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return _error_msg(item)

        if item == '}':
            if pilha and pilha[-1] == '{':
                pilha = pilha[:-1]
            elif pilha and (pilha[-1] == '"' or pilha[-1] == "'"):
                pass
            else:
                return _error_msg(item)

        if item == "'":
            if not pilha or pilha[-1] != "'" and pilha[-1] != '"':
                pilha += "'"
                print('entrou:' + pilha)
            elif pilha[-1] == "'":
                pilha = pilha[:-1]

        if item == '"':
            if not pilha or pilha[-1] != '"' and pilha[-1] != "'":
                pilha += '"'
            elif pilha[-1] == '"':
                pilha = pilha[:-1]
        print(item)
    
    # Verifica se ainda existem elementos na pilha.
    if pilha:
        return _error_msg(pilha[-1])
    else:
        return 0