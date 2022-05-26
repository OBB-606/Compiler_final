
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BEGIN BREAK CLOSE_PAREN COLON COMMA COMPARE CONTINUE DIV DIVIDE DO DOT END EQUAL FUNC ID IF INT INT_DIGIT MOD MULTIPLE NOT OPEN_PAREN OR PLUSMINUS PRINT PROC PROGRAM READ REAL REAL_DIGIT RETURN SEMICOLON STR STRI STRING THEN VAR WHILEprogram : PROGRAM ID SEMICOLON declarations local_declarations body DOTdeclarations :\n                    | declarations VAR identList COLON typeidentList : ID\n                        | identList COMMA IDtype : INT\n            | REAL\n            | STRIlocal_declarations :\n                        | local_declarations local_declaration SEMICOLONlocal_declaration : subHead declarations bodysubHead : FUNC ID args RETURN type SEMICOLON\n                | PROC ID args SEMICOLON args :\n            | OPEN_PAREN paramList CLOSE_PARENparamList : identList COLON type\n                | paramList SEMICOLON identList COLON typebody : BEGIN optionalStatements ENDbodyWBC : BEGIN optionalStatementsWBC ENDoptionalStatements :\n                          | statementListoptionalStatementsWBC :\n                             | statementListWBCstatementList : statement\n                    |  statementList SEMICOLON statementstatementListWBC : statementWBC\n                        |  statementListWBC SEMICOLON statementWBCstatement : variable ASSIGN expression\n                | PRINT OPEN_PAREN string CLOSE_PAREN\n                | PRINT OPEN_PAREN ID CLOSE_PAREN\n                | READ OPEN_PAREN string CLOSE_PAREN\n                | ID OPEN_PAREN expressionListProc CLOSE_PAREN\n                | body\n                | IF expression THEN bodyWBC\n                | WHILE expression DO statement\n                statementWBC : statement\n                    | brConbrCon : BREAK\n            | CONTINUEstring : STRING STR STRINGvariable : IDexpressionListProc :\n                            | expressionList expressionList : expression\n                        | expressionList COMMA expressionexpression : simpleExpression\n                    | simpleExpression COMPARE simpleExpression\n                    | simpleExpression EQUAL simpleExpression\n                    | simpleExpression AND simpleExpression\n                    | simpleExpression OR simpleExpressionsimpleExpression : term\n                        | sign term\n                        | simpleExpression PLUSMINUS termterm : factor\n            | term MULTIPLE factor\n            | term DIV factor\n            | term MOD factor\n            | term DIVIDE factorfactor : ID\n                | ID OPEN_PAREN expressionList CLOSE_PAREN\n                | INT_DIGIT\n                | REAL_DIGIT\n                | OPEN_PAREN expression CLOSE_PAREN\n                | NOT factorsign : PLUSMINUS'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,16,],[0,-1,]),'ID':([2,7,10,12,13,26,27,32,34,35,36,37,42,43,46,49,53,70,71,72,73,74,75,76,77,78,80,83,92,95,110,126,],[3,15,23,29,30,45,45,59,23,45,63,45,45,-65,45,45,15,45,45,45,45,45,45,45,45,45,45,23,45,23,15,23,]),'SEMICOLON':([3,9,19,20,25,30,33,40,41,44,45,47,48,51,54,56,57,58,60,61,79,82,85,88,89,91,93,94,96,97,98,99,100,101,102,103,104,106,107,108,109,115,116,117,118,119,120,121,124,125,128,129,],[4,17,34,-24,-33,-14,-18,-46,-51,-54,-59,-61,-62,-11,87,-6,-7,-8,-25,-28,-52,-64,110,-29,-30,-32,-31,-34,-47,-48,-49,-50,-53,-55,-56,-57,-58,-63,-35,122,-15,126,-26,-36,-37,-38,-39,-60,-16,-19,-27,-17,]),'VAR':([4,5,11,28,55,56,57,58,87,122,],[-2,7,-2,7,-3,-6,-7,-8,-13,-12,]),'BEGIN':([4,5,6,10,11,17,28,34,55,56,57,58,69,83,87,95,122,126,],[-2,-9,10,10,-2,-10,10,10,-3,-6,-7,-8,95,10,-13,10,-12,10,]),'FUNC':([4,5,6,17,55,56,57,58,],[-2,-9,12,-10,-3,-6,-7,-8,]),'PROC':([4,5,6,17,55,56,57,58,],[-2,-9,13,-10,-3,-6,-7,-8,]),'DOT':([8,33,],[16,-18,]),'END':([10,18,19,20,25,33,40,41,44,45,47,48,60,61,79,82,88,89,91,93,94,95,96,97,98,99,100,101,102,103,104,106,107,114,115,116,117,118,119,120,121,125,128,],[-20,33,-21,-24,-33,-18,-46,-51,-54,-59,-61,-62,-25,-28,-52,-64,-29,-30,-32,-31,-34,-22,-47,-48,-49,-50,-53,-55,-56,-57,-58,-63,-35,125,-23,-26,-36,-37,-38,-39,-60,-19,-27,]),'PRINT':([10,34,83,95,126,],[22,22,22,22,22,]),'READ':([10,34,83,95,126,],[24,24,24,24,24,]),'IF':([10,34,83,95,126,],[26,26,26,26,26,]),'WHILE':([10,34,83,95,126,],[27,27,27,27,27,]),'COLON':([14,15,59,86,123,],[31,-4,-5,111,127,]),'COMMA':([14,15,40,41,44,45,47,48,59,66,67,79,82,86,96,97,98,99,100,101,102,103,104,105,106,113,121,123,],[32,-4,-46,-51,-54,-59,-61,-62,-5,92,-44,-52,-64,32,-47,-48,-49,-50,-53,-55,-56,-57,-58,92,-63,-45,-60,32,]),'ASSIGN':([21,23,],[35,-41,]),'OPEN_PAREN':([22,23,24,26,27,29,30,35,37,42,43,45,46,49,70,71,72,73,74,75,76,77,78,80,92,],[36,37,38,46,46,53,53,46,46,46,-65,80,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'PLUSMINUS':([26,27,35,37,40,41,44,45,46,47,48,70,71,72,73,79,80,82,92,96,97,98,99,100,101,102,103,104,106,121,],[43,43,43,43,74,-51,-54,-59,43,-61,-62,43,43,43,43,-52,43,-64,43,74,74,74,74,-53,-55,-56,-57,-58,-63,-60,]),'INT_DIGIT':([26,27,35,37,42,43,46,49,70,71,72,73,74,75,76,77,78,80,92,],[47,47,47,47,47,-65,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'REAL_DIGIT':([26,27,35,37,42,43,46,49,70,71,72,73,74,75,76,77,78,80,92,],[48,48,48,48,48,-65,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'NOT':([26,27,35,37,42,43,46,49,70,71,72,73,74,75,76,77,78,80,92,],[49,49,49,49,49,-65,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'RETURN':([29,52,109,],[-14,84,-15,]),'INT':([31,84,111,127,],[56,56,56,56,]),'REAL':([31,84,111,127,],[57,57,57,57,]),'STRI':([31,84,111,127,],[58,58,58,58,]),'STRING':([36,38,90,],[64,64,112,]),'CLOSE_PAREN':([37,40,41,44,45,47,48,56,57,58,62,63,65,66,67,68,79,81,82,85,96,97,98,99,100,101,102,103,104,105,106,112,113,121,124,129,],[-42,-46,-51,-54,-59,-61,-62,-6,-7,-8,88,89,91,-43,-44,93,-52,106,-64,109,-47,-48,-49,-50,-53,-55,-56,-57,-58,121,-63,-40,-45,-60,-16,-17,]),'THEN':([39,40,41,44,45,47,48,79,82,96,97,98,99,100,101,102,103,104,106,121,],[69,-46,-51,-54,-59,-61,-62,-52,-64,-47,-48,-49,-50,-53,-55,-56,-57,-58,-63,-60,]),'DO':([40,41,44,45,47,48,50,79,82,96,97,98,99,100,101,102,103,104,106,121,],[-46,-51,-54,-59,-61,-62,83,-52,-64,-47,-48,-49,-50,-53,-55,-56,-57,-58,-63,-60,]),'COMPARE':([40,41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[70,-51,-54,-59,-61,-62,-52,-64,-53,-55,-56,-57,-58,-63,-60,]),'EQUAL':([40,41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[71,-51,-54,-59,-61,-62,-52,-64,-53,-55,-56,-57,-58,-63,-60,]),'AND':([40,41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[72,-51,-54,-59,-61,-62,-52,-64,-53,-55,-56,-57,-58,-63,-60,]),'OR':([40,41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[73,-51,-54,-59,-61,-62,-52,-64,-53,-55,-56,-57,-58,-63,-60,]),'MULTIPLE':([41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[75,-54,-59,-61,-62,75,-64,75,-55,-56,-57,-58,-63,-60,]),'DIV':([41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[76,-54,-59,-61,-62,76,-64,76,-55,-56,-57,-58,-63,-60,]),'MOD':([41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[77,-54,-59,-61,-62,77,-64,77,-55,-56,-57,-58,-63,-60,]),'DIVIDE':([41,44,45,47,48,79,82,100,101,102,103,104,106,121,],[78,-54,-59,-61,-62,78,-64,78,-55,-56,-57,-58,-63,-60,]),'STR':([64,],[90,]),'BREAK':([95,126,],[119,119,]),'CONTINUE':([95,126,],[120,120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([4,11,],[5,28,]),'local_declarations':([5,],[6,]),'body':([6,10,28,34,83,95,126,],[8,25,51,25,25,25,25,]),'local_declaration':([6,],[9,]),'subHead':([6,],[11,]),'identList':([7,53,110,],[14,86,123,]),'optionalStatements':([10,],[18,]),'statementList':([10,],[19,]),'statement':([10,34,83,95,126,],[20,60,107,117,117,]),'variable':([10,34,83,95,126,],[21,21,21,21,21,]),'expression':([26,27,35,37,46,80,92,],[39,50,61,67,81,67,113,]),'simpleExpression':([26,27,35,37,46,70,71,72,73,80,92,],[40,40,40,40,40,96,97,98,99,40,40,]),'term':([26,27,35,37,42,46,70,71,72,73,74,80,92,],[41,41,41,41,79,41,41,41,41,41,100,41,41,]),'sign':([26,27,35,37,46,70,71,72,73,80,92,],[42,42,42,42,42,42,42,42,42,42,42,]),'factor':([26,27,35,37,42,46,49,70,71,72,73,74,75,76,77,78,80,92,],[44,44,44,44,44,44,82,44,44,44,44,44,101,102,103,104,44,44,]),'args':([29,30,],[52,54,]),'type':([31,84,111,127,],[55,108,124,129,]),'string':([36,38,],[62,68,]),'expressionListProc':([37,],[65,]),'expressionList':([37,80,],[66,105,]),'paramList':([53,],[85,]),'bodyWBC':([69,],[94,]),'optionalStatementsWBC':([95,],[114,]),'statementListWBC':([95,],[115,]),'statementWBC':([95,126,],[116,128,]),'brCon':([95,126,],[118,118,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON declarations local_declarations body DOT','program',7,'p_program','Parser.py',26),
  ('declarations -> <empty>','declarations',0,'p_declarations','Parser.py',31),
  ('declarations -> declarations VAR identList COLON type','declarations',5,'p_declarations','Parser.py',32),
  ('identList -> ID','identList',1,'p_identList','Parser.py',40),
  ('identList -> identList COMMA ID','identList',3,'p_identList','Parser.py',41),
  ('type -> INT','type',1,'p_type','Parser.py',49),
  ('type -> REAL','type',1,'p_type','Parser.py',50),
  ('type -> STRI','type',1,'p_type','Parser.py',51),
  ('local_declarations -> <empty>','local_declarations',0,'p_local_declarations','Parser.py',58),
  ('local_declarations -> local_declarations local_declaration SEMICOLON','local_declarations',3,'p_local_declarations','Parser.py',59),
  ('local_declaration -> subHead declarations body','local_declaration',3,'p_local_declaration','Parser.py',67),
  ('subHead -> FUNC ID args RETURN type SEMICOLON','subHead',6,'p_subHead','Parser.py',73),
  ('subHead -> PROC ID args SEMICOLON','subHead',4,'p_subHead','Parser.py',74),
  ('args -> <empty>','args',0,'p_args','Parser.py',85),
  ('args -> OPEN_PAREN paramList CLOSE_PAREN','args',3,'p_args','Parser.py',86),
  ('paramList -> identList COLON type','paramList',3,'p_paramList','Parser.py',95),
  ('paramList -> paramList SEMICOLON identList COLON type','paramList',5,'p_paramList','Parser.py',96),
  ('body -> BEGIN optionalStatements END','body',3,'p_body','Parser.py',107),
  ('bodyWBC -> BEGIN optionalStatementsWBC END','bodyWBC',3,'p_bodyWBC','Parser.py',112),
  ('optionalStatements -> <empty>','optionalStatements',0,'p_optionalStatements','Parser.py',117),
  ('optionalStatements -> statementList','optionalStatements',1,'p_optionalStatements','Parser.py',118),
  ('optionalStatementsWBC -> <empty>','optionalStatementsWBC',0,'p_optionalStatementsWBC','Parser.py',126),
  ('optionalStatementsWBC -> statementListWBC','optionalStatementsWBC',1,'p_optionalStatementsWBC','Parser.py',127),
  ('statementList -> statement','statementList',1,'p_statementList','Parser.py',135),
  ('statementList -> statementList SEMICOLON statement','statementList',3,'p_statementList','Parser.py',136),
  ('statementListWBC -> statementWBC','statementListWBC',1,'p_statementListWBC','Parser.py',144),
  ('statementListWBC -> statementListWBC SEMICOLON statementWBC','statementListWBC',3,'p_statementListWBC','Parser.py',145),
  ('statement -> variable ASSIGN expression','statement',3,'p_statement','Parser.py',153),
  ('statement -> PRINT OPEN_PAREN string CLOSE_PAREN','statement',4,'p_statement','Parser.py',154),
  ('statement -> PRINT OPEN_PAREN ID CLOSE_PAREN','statement',4,'p_statement','Parser.py',155),
  ('statement -> READ OPEN_PAREN string CLOSE_PAREN','statement',4,'p_statement','Parser.py',156),
  ('statement -> ID OPEN_PAREN expressionListProc CLOSE_PAREN','statement',4,'p_statement','Parser.py',157),
  ('statement -> body','statement',1,'p_statement','Parser.py',158),
  ('statement -> IF expression THEN bodyWBC','statement',4,'p_statement','Parser.py',159),
  ('statement -> WHILE expression DO statement','statement',4,'p_statement','Parser.py',160),
  ('statementWBC -> statement','statementWBC',1,'p_statementWBC','Parser.py',180),
  ('statementWBC -> brCon','statementWBC',1,'p_statementWBC','Parser.py',181),
  ('brCon -> BREAK','brCon',1,'p_brCon','Parser.py',186),
  ('brCon -> CONTINUE','brCon',1,'p_brCon','Parser.py',187),
  ('string -> STRING STR STRING','string',3,'p_string','Parser.py',192),
  ('variable -> ID','variable',1,'p_variable','Parser.py',197),
  ('expressionListProc -> <empty>','expressionListProc',0,'p_procedureStatement','Parser.py',202),
  ('expressionListProc -> expressionList','expressionListProc',1,'p_procedureStatement','Parser.py',203),
  ('expressionList -> expression','expressionList',1,'p_expressionList','Parser.py',212),
  ('expressionList -> expressionList COMMA expression','expressionList',3,'p_expressionList','Parser.py',213),
  ('expression -> simpleExpression','expression',1,'p_expression','Parser.py',221),
  ('expression -> simpleExpression COMPARE simpleExpression','expression',3,'p_expression','Parser.py',222),
  ('expression -> simpleExpression EQUAL simpleExpression','expression',3,'p_expression','Parser.py',223),
  ('expression -> simpleExpression AND simpleExpression','expression',3,'p_expression','Parser.py',224),
  ('expression -> simpleExpression OR simpleExpression','expression',3,'p_expression','Parser.py',225),
  ('simpleExpression -> term','simpleExpression',1,'p_simpleExpression','Parser.py',233),
  ('simpleExpression -> sign term','simpleExpression',2,'p_simpleExpression','Parser.py',234),
  ('simpleExpression -> simpleExpression PLUSMINUS term','simpleExpression',3,'p_simpleExpression','Parser.py',235),
  ('term -> factor','term',1,'p_term','Parser.py',245),
  ('term -> term MULTIPLE factor','term',3,'p_term','Parser.py',246),
  ('term -> term DIV factor','term',3,'p_term','Parser.py',247),
  ('term -> term MOD factor','term',3,'p_term','Parser.py',248),
  ('term -> term DIVIDE factor','term',3,'p_term','Parser.py',249),
  ('factor -> ID','factor',1,'p_factor','Parser.py',257),
  ('factor -> ID OPEN_PAREN expressionList CLOSE_PAREN','factor',4,'p_factor','Parser.py',258),
  ('factor -> INT_DIGIT','factor',1,'p_factor','Parser.py',259),
  ('factor -> REAL_DIGIT','factor',1,'p_factor','Parser.py',260),
  ('factor -> OPEN_PAREN expression CLOSE_PAREN','factor',3,'p_factor','Parser.py',261),
  ('factor -> NOT factor','factor',2,'p_factor','Parser.py',262),
  ('sign -> PLUSMINUS','sign',1,'p_sign','Parser.py',274),
]
