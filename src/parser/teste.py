import re

symbols = [' ', '(', ')', '{', '}', ',', ';', '+', '-', '*', '/', '<', '>', '=']

words = ['int', 'str', 'flt', 'boo', 'if', 'while', 'else', 'print', 'NULL', 'false', 'true', 'func']

exemplo = "\nfunc main(){\n\tint a, b, c=3;\n\ta = 11 + 1;\n\tb = a + c;\n\tnome = 'joao';\n\twhile(c>0){\n\t\tprint(nome);\n\tc--;\n\t}\n\tprint(b);\n\tif(a>c){\n\t\tprint(a);\n\t}else{\n\t\tprint(b);\n\t}\n}\n"

# func main(){
#   int a, b, c=3;
#   a = 11 + 1;
#   b = a + c;
#   nome = 'joao'
# }

# claudionor print('a')

# functions = re.findall(r'\w+\(\w*\)|\w+\(\w+\>\w+\)', exemplo)

# variaveis = re.findall(r'\w+ \w+', exemplo)

# atribuicao = re.findall(r'\w+=\w+|\w+= \w+|\w+ = \w+', exemplo)


# print(functions)
for word in words:
  res=re.findall(word, exemplo)
  print(res)
