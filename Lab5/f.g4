grammar f;

program: 'program' name '{'statement*'}'EOF;

name: Letter (Letter)*;
statement: varDecl
         | ifStatement
         | loopStatement
         | simpleStmt
         | input
         | output
         | COMMENT ;

varDecl: type ident ';';

ifStatement: 'if' condition block ('else' block)?;

loopStatement: 'while' condition block ('while' condition block)?;

block: '{' statement* '}';

simpleStmt: ident assignmentOp expression ';' | incDecStmt;

input: 'input' '(' ident (',' ident)* ')' ';';

output: 'output' '(' expression (',' expression)* ')' ';';

COMMENT: '//' ~[\r\n]* -> skip;

condition: expression | expression signs expression;

expression: term (('+' | '-') term)*;

term: power (('*' | '/' | '%') power)*;

power: factor ('^' power)*;

factor: ident
      | number
      | '(' expression ')'
      | bool;

assignmentOp: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '^=';
incDecStmt: ident ('++' | '--');
shortVarDecl: ident ':=' expression;
signs: '==' | '!=' | '>' | '<' | '<=' | '>=';
type: 'int' | 'float' | 'bool';
bool: 'true' | 'false';
ident: Letter (Letter | Digit)*;
number: int | float;
int: ('-'? Digit)+;
float: ('-'? Digit)+ '.' Digit+;
Letter: [a-zA-Z_];
Digit: [0-9];
WHITESPACE: [ \t\r\n]+ -> skip;