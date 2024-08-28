grammar LabeledExpr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   INT                         # int
    |   BOOL                        # bool
    |   ID                          # id
    |   '!' expr                    # Negation
    |   ID '++'                     # PostIncrement
    |   ID '--'                     # PostDecrement
    |   '++' ID                     # PreIncrement
    |   '--' ID                     # PreDecrement
    |   '-' expr                    # UnaryMinus
    |   '(' expr ')'                # parens
    ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
BOOL:   'true' | 'false' ; // match boolean values
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace

