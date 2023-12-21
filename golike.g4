grammar golike;

program: statement* EOF;

statement: varDecl
         | ifStatement
         | forStatement
         | simpleStmt
         | input
         | output
         | COMMENT ;

varDecl: 'var' ident type ('=' expression)? ';';

ifStatement: 'if' condition block ('else' block)?;

forStatement: 'for' forClause block;

forClause: shortVarDecl ';' condition ';' incDecStmt;

simpleStmt: ident assignmentOp expression ';' | incDecStmt;

input: 'scan' '(' '&' ident (',' '&' ident)* ')' ';';

output: 'println' '(' expression (',' expression)* ')' ';';

COMMENT: '//' ~[\r\n]* -> skip;

condition: expression | expression signs expression;

block: '{' statement* '}';

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