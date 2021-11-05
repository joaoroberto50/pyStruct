![](img/logo_t.png)  


>Projeto final da disciplina de compiladores do semestre 2020.1

### Como executar:
```$ python ./src/setap.py <nome_do_arquivo>.pyst```

### Operadores:  

```
+ 
- 
* 
/ 
^ 
++ 
-- 
= 
==
!=  
< 
> 
>= 
<= 
&& 
||
```

### Palavras e símbolos reservados:
```
while
if
else
func
print
{
}
(
)
[
]
;
,
""
''
/*
*/
//
int
str
flt
boo
NULL
true
false
```
### Exemplo de código
```
func main() {
    int var1, var2;
    var1 = 10;
    var2 = 5;
    str text = 'pyStruct';
    if (var1 < 100){
        print(var1);
    }else{
        print(var2);
    }
    while(var2 > 0){
        print(text);
        var2--;
    }
}
```

### Gramática:
```
<digit> ::= 0|1|2|3|4|5|6|7|8|9
<letter> ::= a|...|z|A|...|Z
<type> ::= int|str|flt|boo
<id> :: (_|<letter>){ <leter>|<digit> }
<program> ::= func main() { <declarations> <comands> }
<declarations> ::= { <declaration> }
<declaration> ::= <type> <id> [  ] { ,<id> } ;
<comands> ::= { <comand> }
<comand> ::= <bloc>|<att>|<op>|<if>|<while>
<bloc> ::= { <comands> }
<att> ::= <id> = <exp>
<if> ::= if(<exp>) { <declarations> <comands> } { else { <declarations> <comands> } }
```
