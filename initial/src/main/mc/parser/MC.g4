grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk == self.STRINGLIT:
        result = super().emit()
        result.text = result.text[1:-1]
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : decl+ EOF;

    decl: vardecl 
        | funcdecl;

mctype: primitivetype
                | VOIDTYPE
                | arraypointertype;

    arraypointertype: primitivetype LSB RSB;

primitivetype:  INTTYPE 
                | FLOATTYPE 
                | STRINGTYPE 
                | BOOLEANTYPE;

literal: BOOLEANLIT|INTLIT|STRINGLIT|FLOATLIT;

//variable declare
vardecl: primitivetype variablelist SEMI;
    variablelist: variable (CM variable)*;
    variable: ID (LSB INTLIT RSB)?;


//function declare
funcdecl: mctype funcname LB parameterlist? RB blockstmt;
    funcname: ID;
    parameterlist: parameter (CM parameter)* ;
    parameter: primitivetype ID 
            | primitivetype ID LSB RSB;

//stmt

stmt: ifstmt 
    | expstmt
    | dowhilestmt
    | forstmt
    | returnstmt
    | continuestmt
    | breakstmt    
    | blockstmt; 

ifstmt: IF LB expr RB stmt (ELSE stmt)?;      
 
blockstmt: LP blockitem* RP;    
blockitem: (stmt|vardecl);

dowhilestmt: DO (stmt)+ WHILE expr SEMI;


forstmt: FOR LB expr SEMI expr SEMI expr RB stmt;

breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr? SEMI;
expstmt: expr SEMI;


///Expression
expr: expr1 ASSIGN expr | expr1;
expr1: expr1 OR expr2 | expr2;
expr2: expr2 AND expr3 | expr3;
expr3: expr4 (EQ|NEQ) expr4 | expr4;
expr4: expr5 (LESS|LESSEQ|GREATEREQ|GREATER) expr5 | expr5;
expr5: expr5 (ADD|SUB) expr6 | expr6;
expr6: expr6 (DIV|MUL|MOD) expr7 | expr7;
expr7: (NOT|SUB) expr7 | expr8;
expr8: operands LSB expr RSB | operands;

operands: funcall              
        |literal        
        |ID
        |LB expr RB ;
funcall: ID LB (expr (CM expr)*)? RB;
///typesd


//Lexical specification
VOIDTYPE: 'void' ;
INTTYPE: 'int';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
BOOLEANTYPE: 'boolean';

IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
RETURN: 'return';
BREAK: 'break';
FOR: 'for';
CONTINUE: 'continue';

/*KEYWORD: ('boolean' | 'break' | 'continue' | 'else' | 'for' | 'float' | 'if' | 'int' | 'return' |
'void' | 'do' | 'while' | 'true' | 'false' | 'string')*;*/


fragment DIGIT: [0-9];

INTLIT: DIGIT+;
BOOLEANLIT: 'true' | 'false';

FLOATLIT: FRACTION EX?;
fragment EX: [eE] '-'? INTLIT+;
fragment FRACTION:  DIGIT+ ('.' DIGIT*)? 
                    | DIGIT* '.' DIGIT+; 



STRINGLIT: '"' ( '\\' [btnfr"\\] | ~[\r\n\\"] )*? '"';

///#
BLOCKCOMMENT: '/*' (.)*? '*/' -> skip;
LINECOMMENT: '//' (~[\r\n])* -> skip;
///#

LB: '(' ; 
RB: ')' ;

LP: '{';
RP: '}';

LSB: '[';
RSB: ']';

SEMI: ';' ;
CM : ',';

///
ASSIGN : '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: '!';
OR: '||';
AND: '&&';
NEQ: '!=';
EQ: '==';
LESS: '<';
LESSEQ: '<=' ;
GREATER: '>' ;
GREATEREQ: '>=';
ID: [a-zA-Z_]+[a-zA-Z0-9_]*;
// BOOLEANOP: NOT|OR|AND|NEQ|EQ|LESS|LESSEQ|GREATER|GREATEREQ;

///
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' ( '\\' [btnfr"\\] | ~[\r\n\\"] )*;
ILLEGAL_ESCAPE: '"' ( '\\' [btnfr"\\] | ~[\r\n\\"] )*? ('\\' (~[btnfr\\"]|EOF)) ;
ERROR_CHAR: .;
