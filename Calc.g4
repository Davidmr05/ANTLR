grammar Calc;

calclist
    : /* nothing */
    | calclist exp EOL { print(f"= { $exp.value }\n> ", end="") }
    | calclist EOL { print("> ", end="") }
    ;

exp
    : factor                   # singleFactor
    | exp ADD exp              # addExp
    | exp SUB factor           # subExp
    | ABS exp ABS              # absExp
    ;

factor
    : term                     # singleTerm
    | factor MUL term          # mulFactor
    | factor DIV term          # divFactor
    ;

term
    : NUMBER                   { $value = int($NUMBER.text) }
    | OP exp CP                { $value = $exp.value }
    ;
    
NUMBER : [0-9]+;
ADD    : '+';
SUB    : '-';
MUL    : '*';
DIV    : '/';
ABS    : '|';
OP     : '(';
CP     : ')';
EOL    : '\r'? '\n' | '\r';
WS     : [ \t]+ -> skip;

