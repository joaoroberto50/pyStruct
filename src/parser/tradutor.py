


out_text = ""

meaning = {'func': 'def', 'show': 'print', 'NULL': 'None', 'false': 'False', 'true':'True', '&&': 'and', '||': 'or'}


class Tradutor(object):
    def __init__(self):
        self.meaning = {'while':'while','if':'if','else':'else','func': 'def', 'show': 'print', 'NULL': 'None', 'false': 'False', 'true':'True', '&&': 'and', '||': 'or', '++':'+=1', '--':'-=1', '^':'**'}
        self.same_ops = ['+', '-', '/', '*', '==', '<=', '>=', '<', '>']
        self.ident = ''
        self.out_text = ''
        self.pilha = ''
        self.expected = []


    def replaces(self, token, flag=''):
        if not flag:
            print(token)
            self.out_text += self.meaning[token]
        elif flag == 'OP':
            if token in self.same_ops:
                self.out_text += token
            else:
                self.apply(token)
        else:
            self.out_text += self.meaning[token]


    def patern_type(self):
        if self.pilha == 'int':
            self.out_text += '=0'
            self.semicolon()
            return
        if self.pilha == 'flt':
            self.out_text += '=0.0'
            self.semicolon()
            return
        if self.pilha == 'srt':
            self.out_text += '="python"'
            self.semicolon()
            return
        if self.pilha == 'boo':
            self.out_text += '=True'
            self.semicolon()
            return
        

    def apply(self, token, tyype=''):
        if self.expected and tyype in self.expected:
            #self.out_text += token
            #if tyype == 'ID':
             #   self.expected = [',', '=']
            if tyype == ',':
                self.patern_type()
                self.expected = ['ID']
            elif tyype == '=':
                self.out_text += token
                self.expected['ID', self.pilha]
            if tyype == self.pilha or tyype == 'ID':
                self.out_text += token
                self.semicolon()
                self.expected = ['ID', ',']
        else:
            if token != ',' and not self.pilha:
                self.out_text += token


    def type_role(self, token):
        self.pilha = token
        self.expected = ['ID']


    def braces(self, token):
        if token == '{':
            self.out_text += ':'
            self.ident += chr(9)
            self.semicolon()
        else:
            self.ident = self.ident[:-1]
            self.semicolon()


    def semicolon(self, symble=''):
        self.out_text += chr(10)
        self.out_text += self.ident
        if symble == ';':
            self.expected = []
            self.pilha = ''
