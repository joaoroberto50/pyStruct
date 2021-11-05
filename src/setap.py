from parser.parser import tokenize
from parser.structer import check
import sys


def main():
    name = sys.argv[1]
    print(name)
    text_file = []
    with open(name) as fp:
        for i in fp:
            text_file.append(i)
    text_file = ''.join(text_file)
    print(type(text_file))
    valid = check(text_file)
    print(valid)
    if valid == 0:
        text_out = tokenize(text_file)
    else:
        print(valid)
        return
    text_out += 'if __name__ == "__main__":'
    text_out += chr(10)
    text_out += chr(9)
    text_out += 'main()'
    text_out += chr(10)
    with open('out.py', 'w') as fp:
        fp.write(text_out)
    print("Transplation OK!")



if __name__ == "__main__":
    main()