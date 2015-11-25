grammar Expr;		
prog      : (statement NEWLINE)* ;
statement : dec=decl | struct=ctrlStruct | func=funcDef | fnCall=funcCall | printcall=printc ;
decl      : ident=ID '=' right=expr ;
funcDef   : FN ident=ID '(' params=paramList ')' bl=block ;
paramList : ident=ID (split=', ' ident2=ID)* ;
paramCallList : ident=(ID|INT) (split=',' ident2=(ID|INT))* ;
block     : OPEN_SCOPE NEWLINE ((statement | retrn)  NEWLINE)+ CLOSE_SCOPE ;
retrn     : RET value=(ID|INT) ;
ctrlStruct: whileStr=whileStruct | ifStr=ifStruct ;
whileStruct: WHILE '(' cond=condition  ')' bl=block ;
ifStruct  : IF '(' cond=condition  ')' bl=block ELSE bl2=block ;
funcCall  : ident=ID '(' params=paramCallList ')' ;
condition : left=ID op=(LT|LTEQ|EQ|NEQ|GTEQ|GT) right=(ID|INT) ;
expr      :	left=expr op=(TIMES|DIVIDE) right=expr
          |	left=expr op=(PLUS|MINUS) right=expr
          |	number=INT
          |	ident=ID
          |	'(' sub=expr ')'
          | call=funcCall
          ;
printc    : 'print(' ident=ID ')' ;

IF          : 'if' ;
WHILE       : 'while' ;
ELSE        : 'else' ;
ID          : [a-zA-Z_$][a-zA-Z_$0-9]* ;
NEWLINE     : [\r\n]+ ;
INT         : [0-9]+ ;
PLUS        : '+' ;
MINUS       : '-' ;
TIMES       : '*' ;
DIVIDE      : '/' ;
FN          : 'fn ' ;
OPEN_SCOPE  : '[' ;
CLOSE_SCOPE : ']' ;
RET         : 'ret ' ;

LT          : '<' ;
GT          : '>' ;
EQ          : '==' ;
NEQ         : '!=' ;
LTEQ        : '<=' ;
GTEQ        : '>=' ;

WS : (' '|'\t')+ -> skip ;