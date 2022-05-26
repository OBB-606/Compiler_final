from Lexer import tokens
import ply.yacc as yacc

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

    scope = 'global'


def p_program(p):
    '''program : PROGRAM ID SEMICOLON declarations local_declarations body DOT'''
    p[0] = Node('Program', [p[4], p[5], p[6]])


def p_declarations(p):  # DECLARATIONS
    '''declarations :
                    | declarations VAR identList COLON type'''
    if len(p) == 1:
        p[0] = Node('Var', [], )
    else:
        p[0] = p[1].add_parts([p[3], p[5]])


def p_identList(p):  # DECLARATIONS / IdentifierList
    '''identList : ID
                        | identList COMMA ID'''
    if len(p) == 2:
        p[0] = Node('ID', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_type(p):  # DECLARATIONS / Type
    '''type : INT
            | REAL
            | STRI'''
    if len(p) == 2:
        p[0] = Node('Type', [p[1]])

# ________________________________________________________________________________________________________

def p_local_declarations(p):  # SUBDECLARATIONS
    '''local_declarations :
                        | local_declarations local_declaration SEMICOLON'''
    if len(p) == 1:
        p[0] = Node('SubDeclare', [])
    else:
        p[0] = p[1].add_parts([p[2]])


def p_local_declaration(p):  # SUBDECLARATIONS / SubDeclaration
    '''local_declaration : subHead declarations body'''
    p[0] = Node('SubDeclaration', [p[1], p[2], p[3]])
    p[2].scope = p[1].scope


def p_subHead(p):  # SUBDECLARATIONS / SubDeclaration / subHead
    '''subHead : FUNC ID args RETURN type SEMICOLON
                | PROC ID args SEMICOLON '''
    if len(p) == 7:
        p[0] = Node(p[1] + ' ' + p[2], [p[3], p[5]])
    else:
        p[0] = Node(p[1] + ' ' + p[2], [p[3]])
    scope = p[2]
    p[3].scope = p[2]
    p[0].scope = p[2]


def p_args(p):  # SUBDECLARATIONS / SubDeclaration / subHead / args
    '''args :
            | OPEN_PAREN paramList CLOSE_PAREN'''
    if len(p) == 1:
        p[0] = Node('Ar',[])
    else:
        p[0] = p[2]
        p[2].scope = p[0].scope


def p_paramList(p):  # SUBDECLARATIONS / SubDeclaration / subHead / args / paramList
    '''paramList : identList COLON type
                | paramList SEMICOLON identList COLON type'''
    if len(p) == 4:
        p[0] = Node('Arguments', [p[1], p[3]])
        p[1].scope = p[0].scope
    else:
        p[0] = p[1].add_parts([p[3], p[5]])
        p[3].scope = p[0].scope

# ________________________________________________________________________________________________________

def p_body(p):  # COMPOUNDSTATEMENT
    '''body : BEGIN optionalStatements END'''
    p[0] = Node('Compound statement', [p[2]])


def p_bodyWBC(p):
    '''bodyWBC : BEGIN optionalStatementsWBC END'''
    p[0] = Node('Compound statement', [p[2]])


def p_optionalStatements(p):  # COMPOUNDSTATEMENT / OptionalStatements
    '''optionalStatements :
                          | statementList'''
    if len(p) == 1:
        p[0] = Node('Optional statements', [])
    else:
        p[0] = Node('Optional statements', [p[1]])


def p_optionalStatementsWBC(p):  # COMPOUNDSTATEMENTWBC / OptionalStatementsWBC
    '''optionalStatementsWBC :
                             | statementListWBC'''
    if len(p) == 1:
        p[0] = Node('Optional statements', [])
    else:
        p[0] = Node('Optional statements', [p[1]])


def p_statementList(p):  # COMPOUNDSTATEMENT / OptionalStatements / statementList
    '''statementList : statement
                    |  statementList SEMICOLON statement'''
    if len(p) == 2:
        p[0] = Node('Statement List', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_statementListWBC(p):  # COMPOUNDSTATEMENTWBC / OptionalStatementsWBC / statementListWBC
    '''statementListWBC : statementWBC
                        |  statementListWBC SEMICOLON statementWBC'''
    if len(p) == 2:
        p[0] = Node('Statement List', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_statement(p):  # COMPOUNDSTATEMENT / OptionalStatements / statementList / statement
    '''statement : variable ASSIGN expression
                | PRINT OPEN_PAREN string CLOSE_PAREN
                | PRINT OPEN_PAREN ID CLOSE_PAREN
                | READ OPEN_PAREN string CLOSE_PAREN
                | ID OPEN_PAREN expressionListProc CLOSE_PAREN
                | body
                | IF expression THEN bodyWBC
                | WHILE expression DO statement
                '''
    if len(p) == 2 :
        p[0] = Node('Statement', [p[1]])
    elif len(p) == 2 :
        p[0] = Node('Call procedure', [p[1]])
    elif len(p) == 4:
        p[0] = Node('Assign', [p[1], p[3]])

    elif p[1] == 'if' :
        p[0] = Node('If clause', [p[2], p[4]])
    elif p[1] == 'while':
        p[0] = Node('While clause', [p[2], p[4]])
    elif len(p) == 5 and p[1] != 'print':
        p[0] = Node('Call proc', [p[1],p[3]])
    elif len(p) == 5:
        p[0] = Node(p[1], [p[3]])


def p_statementWBC(p):
    '''statementWBC : statement
                    | brCon'''
    p[0] = Node('Statement', [p[1]])


def p_brCon(p):
    '''brCon : BREAK
            | CONTINUE'''
    p[0] = Node('BR', [p[1]])


def p_string(p):
    '''string : STRING STR STRING'''
    p[0] = Node('Strings', [p[2]])


def p_variable(p):  # COMPOUNDSTATEMENT / OptionalStatements / statementList / statement / variable
    '''variable : ID'''
    p[0] = Node('Variable', [p[1]])


def p_procedureStatement(p):  # COMPOUNDSTATEMENT / OptionalStatements / statementList / statement / procedureStatement
    '''expressionListProc :
                            | expressionList '''
    if len(p) == 1:
        p[0] = Node('Empty', [])
    else:
        p[0] = Node('Expressions', [p[1]])



def p_expressionList(p):  # COMPOUNDSTATEMENT / OptionalStatements / statementList / statement / procedureStatement / expressionList
    '''expressionList : expression
                        | expressionList COMMA expression'''
    if len(p) == 2:
        p[0] = Node('ExpressionList', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_expression(p):
    '''expression : simpleExpression
                    | simpleExpression COMPARE simpleExpression
                    | simpleExpression EQUAL simpleExpression
                    | simpleExpression AND simpleExpression
                    | simpleExpression OR simpleExpression'''
    if len(p) == 2:
        p[0] = Node('Expression', [p[1]])
    else:
        p[0] = Node(p[2], [p[1], p[3]])


def p_simpleExpression(p):
    '''simpleExpression : term
                        | sign term
                        | simpleExpression PLUSMINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = Node('Sign', [p[1], p[2]])
    else:
        p[0] = Node(p[2], [p[1], p[3]])


def p_term(p):
    '''term : factor
            | term MULTIPLE factor
            | term DIV factor
            | term MOD factor
            | term DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])


def p_factor(p):
    '''factor : ID
                | ID OPEN_PAREN expressionList CLOSE_PAREN
                | INT_DIGIT
                | REAL_DIGIT
                | OPEN_PAREN expression CLOSE_PAREN
                | NOT factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = Node('Not', [p[2]])
    elif len(p) == 4:
        p[0] = Node('Expression in parentheses', [p[2]])
    else:
        p[0] = Node('Func', [p[1],p[3]])


def p_sign(p):
    '''sign : PLUSMINUS'''
    p[0] = p[1]


def p_error(p):
    print('Unexpected token:', p)


parser = yacc.yacc()


def build_tree(code):
    return parser.parse(code)
def find(tree , tableOfValues):
    if (type(tree) != str):
        for part in tree.parts:

            if (type(part) != str):
                variable = []
                if (part.type.startswith('func')):
                    variable.append(part.parts[1].parts[0])
                    #variable.append('Null')
                    tableOfValues[part.type[5:]] = {}
                    tableOfValues[part.type[5:]][part.type[5:]] = variable

                if (part.type.startswith('proc')):
                    tableOfValues[part.type[5:]] = {}

                if (part.type == 'Arguments'):
                    if (len(part.parts)) != 0:
                        for idvars in range(0, len(part.parts), 2):
                            if len(part.parts[idvars].parts) > 1:
                                id = part.parts[idvars]
                                for i in range(len(id.parts)):
                                    variable.append(part.parts[idvars + 1].parts[0])
                                    #variable.append('Null')
                                    tableOfValues[part.scope][id.parts[i]] = variable
                                    variable = []

                            elif len(part.parts[idvars].parts) == 1:
                                variable.append(part.parts[idvars + 1].parts[0])
                                #variable.append('Null')
                                tableOfValues[part.scope][part.parts[idvars].parts[0]] = variable
                                variable = []
                if (part.type == 'Var'):
                    if (len(part.parts)) != 0:
                        for idvars in range(0, len(part.parts), 2):

                            if len(part.parts[idvars].parts) >= 1:
                                id = part.parts[idvars]
                                for i in range(len(id.parts)):
                                    variable.append(part.parts[idvars + 1].parts[0])
                                    #variable.append('Null')
                                    tableOfValues[part.scope][id.parts[i]] = variable
                                    variable = []

                            elif len(part.parts[idvars].parts) == 1:
                                variable.append(part.parts[idvars].parts[0])
                                variable.append(part.parts[idvars + 1].parts[0])
                                variable.append(part.scope)
                                variable = []
            find(part , tableOfValues)

def getTable(code):
    tableOfValues = {}
    tableOfValues['global'] = {}
    find(code , tableOfValues)
    return tableOfValues




def main():
    data = '''
    program Factorials;
    var a,b,c : integer
    var h : real

    func factorial (a: integer) return integer;
       var num,c,d,e : integer
       begin
           num = 1;
           e = 1;
           while ( e < a ) do
           begin
                num = num * e;
                e = e + 1
           end;
           factorial = num
       end;

    begin
        print("the first b factorials.kia");
        b = 10;
        a = 1;
        while ( a <= b) do
        begin
            c = factorial(a);
            print(c);
            a = a+1
        end
    end.
        '''

    print(build_tree(data))

if __name__ == '__main__':
    main()

