grammar Expr;		
prog      : (statement NEWLINE)* ;
statement : dec=decl | func=funcDef | fnCall=funcCall | printcall=printc;
decl      : ident=ID '=' right=expr ;
funcDef   : FN ident=ID ' (' params=paramList ') ' bl=block ;
paramList : ident=ID (split=', ' ident2=ID)*;
block     : OPEN_SCOPE NEWLINE (TAB (statement | retrn)  NEWLINE)+ CLOSE_SCOPE ;
retrn     : RET value=(ID|INT) ;
funcCall  : ident=ID '(' params=paramList ')' ;
expr      :	left=expr op=(TIMES|DIVIDE) right=expr
          |	left=expr op=(PLUS|MINUS) right=expr
          |	number=INT
          |	ident=ID
          |	'(' sub=expr ')'
          | call=funcCall
          ;
printc    : 'print(' ident=ID ')' ;
ID          : [a-zA-Z_$][a-zA-Z_$0-9]* ;
NEWLINE     : [\r\n]+ ;
INT         : [0-9]+ ;
PLUS        : '+' ;
MINUS       : '-' ;
TIMES       : '*' ;
DIVIDE      : '/' ;
TAB         : '    ' ;
FN          : 'fn ' ;
OPEN_SCOPE  : '[' ;
CLOSE_SCOPE : ']' ;
RET         : 'ret ' ;