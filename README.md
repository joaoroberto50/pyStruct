![](img/logo_t.png)  


>Projeto final da disciplina de compiladores do semestre 2020.1

### Como executar:
```$ python ./src/setap.py <nome_do_arquivo>.pyst
```

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
func main(){
    int a, b, c= -3;
    flt x= -5.1, y = 1.1;
    a = 11 - 1;
    b = a + c;
    nome = 'COMPILADORES';
    while(c!= 0){
        show(nome);
        c++;    
    }
    show(b);
    if(a> c){
        show(a);
    }else{
        show(b);
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
