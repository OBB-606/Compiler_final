grammar kia;

program : PROGRAM ID SEMICOLON declarations subDeclarations comStatement DOT;

declarations : VAR identifierList COLON type (declarations)*;

identifierList : ID
               | identifierList COMMA ID;


type : INT
     | REAL;

subDeclarations : (subHead declarations comStatement)*;

subHead : FUNC ID args RETURN type SEMICOLON
        | PROC ID args SEMICOLON;

args : (OPEN_PAREN paramList CLOSE_PAREN)*;

paramList : identifierList COLON type
          | paramList SEMICOLON identifierList COLON type;

comStatement : BEGIN optionalStatements END SEMICOLON?;

comStatementWBC : BEGIN optionalStatementsWBC END;

optionalStatements : (statementList)*;

optionalStatementsWBC : (statementListWBC)*;

statementList : statement
                | statementList SEMICOLON statement;

statementListWBC : statementWBC
                    |  statementListWBC SEMICOLON statementWBC;

statement : variable ASSIGN expression
                | PRINT OPEN_PAREN string CLOSE_PAREN
                | PRINT OPEN_PAREN ID CLOSE_PAREN
                | READ OPEN_PAREN string CLOSE_PAREN
                | ID OPEN_PAREN expressionListProc CLOSE_PAREN
                | comStatement
                | IF expression THEN comStatement
                | WHILE expression DO statement;

statementWBC : statement
                    | brCon;

brCon : BREAK
            | CONTINUE;

string : STR;

variable : ID;

expressionListProc : (expressionList)*;

expressionList : expression
                        | expressionList COMMA expression;

expression : simpleExpression
                    | simpleExpression COMPARE simpleExpression
                    | simpleExpression EQUAL simpleExpression
                    | simpleExpression AND simpleExpression
                    | simpleExpression OR simpleExpression;

simpleExpression : term
                        | sign term
                        | simpleExpression PLUSMINUS term;

term : factor
            | term MULTIPLE factor
            | term DIV factor
            | term MOD factor
            | term DIVIDE factor;

factor : ID
                | ID OPEN_PAREN expressionList CLOSE_PAREN
                | NUM
                | REALNUM
                | OPEN_PAREN expression CLOSE_PAREN
                | NOT factor;

sign : PLUSMINUS;

RETURN : 'return';
PROGRAM : 'program';
ASSIGN : '=';
IF : 'if';
WHILE : 'while';
THEN : 'then';
DO : 'do';
PRINT : 'print';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
READ : 'read';
FUNC : 'func';
PROC : 'proc';
BEGIN : 'begin';
END : 'end';
DOT : '.';
VAR : 'var';
INT : 'integer';
REAL : 'real';
SEMICOLON : ';';
COLON : ':';
NOT : 'not';
MULTIPLE : '*';
DIV : 'div';
MOD : 'mod';
DIVIDE : '/';
PLUSMINUS : '+'|'-';
OR : 'or';
COMPARE : '>='|'<='|'>'|'<'|'<>';
EQUAL : '==';
AND : 'and';
COMMA : ',';
BREAK : 'break';
CONTINUE : 'continue';
REALNUM : [0-9]+'.'[0-9]+;
NUM : [0-9]+;
STR : '"'[a-zA-Z0-9]+(' '[a-zA-Z0-9]+)*'"';
ID : [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \t\r\n] -> skip;


