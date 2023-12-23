# Generated from C:/Trans/Lab5/f.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,5,0,52,8,0,10,0,12,
        0,55,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,87,8,4,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,104,8,6,1,7,1,7,1,7,1,7,1,7,5,7,111,8,7,
        10,7,12,7,114,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,124,8,8,10,
        8,12,8,127,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,137,8,9,1,10,
        1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,1,11,1,11,1,11,5,11,
        150,8,11,10,11,12,11,153,9,11,1,12,1,12,1,12,5,12,158,8,12,10,12,
        12,12,161,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,170,8,13,
        1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,
        1,19,1,19,1,20,1,20,5,20,189,8,20,10,20,12,20,192,9,20,1,21,1,21,
        3,21,196,8,21,1,22,3,22,199,8,22,1,22,4,22,202,8,22,11,22,12,22,
        203,1,23,3,23,207,8,23,1,23,4,23,210,8,23,11,23,12,23,211,1,23,1,
        23,4,23,216,8,23,11,23,12,23,217,1,23,0,0,24,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,8,1,0,13,14,1,
        0,15,17,1,0,19,25,1,0,26,27,1,0,29,34,1,0,35,37,1,0,38,39,1,0,42,
        43,222,0,48,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,72,1,0,0,0,8,79,
        1,0,0,0,10,88,1,0,0,0,12,103,1,0,0,0,14,105,1,0,0,0,16,118,1,0,0,
        0,18,136,1,0,0,0,20,138,1,0,0,0,22,146,1,0,0,0,24,154,1,0,0,0,26,
        169,1,0,0,0,28,171,1,0,0,0,30,173,1,0,0,0,32,176,1,0,0,0,34,180,
        1,0,0,0,36,182,1,0,0,0,38,184,1,0,0,0,40,186,1,0,0,0,42,195,1,0,
        0,0,44,201,1,0,0,0,46,209,1,0,0,0,48,49,5,1,0,0,49,53,5,2,0,0,50,
        52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,
        0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,3,0,0,57,58,5,0,0,1,58,1,1,
        0,0,0,59,67,3,4,2,0,60,67,3,6,3,0,61,67,3,8,4,0,62,67,3,12,6,0,63,
        67,3,14,7,0,64,67,3,16,8,0,65,67,5,41,0,0,66,59,1,0,0,0,66,60,1,
        0,0,0,66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,
        65,1,0,0,0,67,3,1,0,0,0,68,69,3,36,18,0,69,70,3,40,20,0,70,71,5,
        4,0,0,71,5,1,0,0,0,72,73,5,5,0,0,73,74,3,18,9,0,74,77,3,10,5,0,75,
        76,5,6,0,0,76,78,3,10,5,0,77,75,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,
        0,79,80,5,7,0,0,80,81,3,18,9,0,81,86,3,10,5,0,82,83,5,7,0,0,83,84,
        3,18,9,0,84,85,3,10,5,0,85,87,1,0,0,0,86,82,1,0,0,0,86,87,1,0,0,
        0,87,9,1,0,0,0,88,92,5,2,0,0,89,91,3,2,1,0,90,89,1,0,0,0,91,94,1,
        0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,
        96,5,3,0,0,96,11,1,0,0,0,97,98,3,40,20,0,98,99,3,28,14,0,99,100,
        3,20,10,0,100,101,5,4,0,0,101,104,1,0,0,0,102,104,3,30,15,0,103,
        97,1,0,0,0,103,102,1,0,0,0,104,13,1,0,0,0,105,106,5,8,0,0,106,107,
        5,9,0,0,107,112,3,40,20,0,108,109,5,10,0,0,109,111,3,40,20,0,110,
        108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        115,1,0,0,0,114,112,1,0,0,0,115,116,5,11,0,0,116,117,5,4,0,0,117,
        15,1,0,0,0,118,119,5,12,0,0,119,120,5,9,0,0,120,125,3,20,10,0,121,
        122,5,10,0,0,122,124,3,20,10,0,123,121,1,0,0,0,124,127,1,0,0,0,125,
        123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,
        129,5,11,0,0,129,130,5,4,0,0,130,17,1,0,0,0,131,137,3,20,10,0,132,
        133,3,20,10,0,133,134,3,34,17,0,134,135,3,20,10,0,135,137,1,0,0,
        0,136,131,1,0,0,0,136,132,1,0,0,0,137,19,1,0,0,0,138,143,3,22,11,
        0,139,140,7,0,0,0,140,142,3,22,11,0,141,139,1,0,0,0,142,145,1,0,
        0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,21,1,0,0,0,145,143,1,0,0,
        0,146,151,3,24,12,0,147,148,7,1,0,0,148,150,3,24,12,0,149,147,1,
        0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,23,1,0,
        0,0,153,151,1,0,0,0,154,159,3,26,13,0,155,156,5,18,0,0,156,158,3,
        24,12,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,25,1,0,0,0,161,159,1,0,0,0,162,170,3,40,20,0,163,170,
        3,42,21,0,164,165,5,9,0,0,165,166,3,20,10,0,166,167,5,11,0,0,167,
        170,1,0,0,0,168,170,3,38,19,0,169,162,1,0,0,0,169,163,1,0,0,0,169,
        164,1,0,0,0,169,168,1,0,0,0,170,27,1,0,0,0,171,172,7,2,0,0,172,29,
        1,0,0,0,173,174,3,40,20,0,174,175,7,3,0,0,175,31,1,0,0,0,176,177,
        3,40,20,0,177,178,5,28,0,0,178,179,3,20,10,0,179,33,1,0,0,0,180,
        181,7,4,0,0,181,35,1,0,0,0,182,183,7,5,0,0,183,37,1,0,0,0,184,185,
        7,6,0,0,185,39,1,0,0,0,186,190,5,42,0,0,187,189,7,7,0,0,188,187,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,41,1,
        0,0,0,192,190,1,0,0,0,193,196,3,44,22,0,194,196,3,46,23,0,195,193,
        1,0,0,0,195,194,1,0,0,0,196,43,1,0,0,0,197,199,5,14,0,0,198,197,
        1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,200,202,5,43,0,0,201,198,
        1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,45,1,
        0,0,0,205,207,5,14,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,
        0,0,0,208,210,5,43,0,0,209,206,1,0,0,0,210,211,1,0,0,0,211,209,1,
        0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,215,5,40,0,0,214,216,5,
        43,0,0,215,214,1,0,0,0,216,217,1,0,0,0,217,215,1,0,0,0,217,218,1,
        0,0,0,218,47,1,0,0,0,20,53,66,77,86,92,103,112,125,136,143,151,159,
        169,190,195,198,203,206,211,217
    ]

class fParser ( Parser ):

    grammarFileName = "f.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'{'", "'}'", "';'", "'if'", 
                     "'else'", "'while'", "'input'", "'('", "','", "')'", 
                     "'output'", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'^='", 
                     "'++'", "'--'", "':='", "'=='", "'!='", "'>'", "'<'", 
                     "'<='", "'>='", "'int'", "'float'", "'bool'", "'true'", 
                     "'false'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "Letter", "Digit", "WHITESPACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_ifStatement = 3
    RULE_loopStatement = 4
    RULE_block = 5
    RULE_simpleStmt = 6
    RULE_input = 7
    RULE_output = 8
    RULE_condition = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_power = 12
    RULE_factor = 13
    RULE_assignmentOp = 14
    RULE_incDecStmt = 15
    RULE_shortVarDecl = 16
    RULE_signs = 17
    RULE_type = 18
    RULE_bool = 19
    RULE_ident = 20
    RULE_number = 21
    RULE_int = 22
    RULE_float = 23

    ruleNames =  [ "program", "statement", "varDecl", "ifStatement", "loopStatement", 
                   "block", "simpleStmt", "input", "output", "condition", 
                   "expression", "term", "power", "factor", "assignmentOp", 
                   "incDecStmt", "shortVarDecl", "signs", "type", "bool", 
                   "ident", "number", "int", "float" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    COMMENT=41
    Letter=42
    Digit=43
    WHITESPACE=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(fParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.StatementContext)
            else:
                return self.getTypedRuleContext(fParser.StatementContext,i)


        def getRuleIndex(self):
            return fParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = fParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(fParser.T__0)
            self.state = 49
            self.match(fParser.T__1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6837587939744) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(fParser.T__2)
            self.state = 57
            self.match(fParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(fParser.VarDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(fParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(fParser.LoopStatementContext,0)


        def simpleStmt(self):
            return self.getTypedRuleContext(fParser.SimpleStmtContext,0)


        def input_(self):
            return self.getTypedRuleContext(fParser.InputContext,0)


        def output(self):
            return self.getTypedRuleContext(fParser.OutputContext,0)


        def COMMENT(self):
            return self.getToken(fParser.COMMENT, 0)

        def getRuleIndex(self):
            return fParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = fParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.varDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.loopStatement()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.simpleStmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.input_()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.output()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.match(fParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(fParser.TypeContext,0)


        def ident(self):
            return self.getTypedRuleContext(fParser.IdentContext,0)


        def getRuleIndex(self):
            return fParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = fParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.type_()
            self.state = 69
            self.ident()
            self.state = 70
            self.match(fParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(fParser.ConditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.BlockContext)
            else:
                return self.getTypedRuleContext(fParser.BlockContext,i)


        def getRuleIndex(self):
            return fParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = fParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(fParser.T__4)
            self.state = 73
            self.condition()
            self.state = 74
            self.block()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 75
                self.match(fParser.T__5)
                self.state = 76
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.ConditionContext)
            else:
                return self.getTypedRuleContext(fParser.ConditionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.BlockContext)
            else:
                return self.getTypedRuleContext(fParser.BlockContext,i)


        def getRuleIndex(self):
            return fParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = fParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(fParser.T__6)
            self.state = 80
            self.condition()
            self.state = 81
            self.block()
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(fParser.T__6)
                self.state = 83
                self.condition()
                self.state = 84
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.StatementContext)
            else:
                return self.getTypedRuleContext(fParser.StatementContext,i)


        def getRuleIndex(self):
            return fParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = fParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(fParser.T__1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6837587939744) != 0):
                self.state = 89
                self.statement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(fParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(fParser.IdentContext,0)


        def assignmentOp(self):
            return self.getTypedRuleContext(fParser.AssignmentOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(fParser.ExpressionContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(fParser.IncDecStmtContext,0)


        def getRuleIndex(self):
            return fParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = fParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simpleStmt)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.ident()
                self.state = 98
                self.assignmentOp()
                self.state = 99
                self.expression()
                self.state = 100
                self.match(fParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.incDecStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.IdentContext)
            else:
                return self.getTypedRuleContext(fParser.IdentContext,i)


        def getRuleIndex(self):
            return fParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = fParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(fParser.T__7)
            self.state = 106
            self.match(fParser.T__8)
            self.state = 107
            self.ident()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 108
                self.match(fParser.T__9)
                self.state = 109
                self.ident()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(fParser.T__10)
            self.state = 116
            self.match(fParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(fParser.ExpressionContext,i)


        def getRuleIndex(self):
            return fParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = fParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(fParser.T__11)
            self.state = 119
            self.match(fParser.T__8)
            self.state = 120
            self.expression()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 121
                self.match(fParser.T__9)
                self.state = 122
                self.expression()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(fParser.T__10)
            self.state = 129
            self.match(fParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(fParser.ExpressionContext,i)


        def signs(self):
            return self.getTypedRuleContext(fParser.SignsContext,0)


        def getRuleIndex(self):
            return fParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = fParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.expression()
                self.state = 133
                self.signs()
                self.state = 134
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.TermContext)
            else:
                return self.getTypedRuleContext(fParser.TermContext,i)


        def getRuleIndex(self):
            return fParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = fParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.term()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 139
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.term()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def power(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.PowerContext)
            else:
                return self.getTypedRuleContext(fParser.PowerContext,i)


        def getRuleIndex(self):
            return fParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = fParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.power()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0):
                self.state = 147
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.power()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(fParser.FactorContext,0)


        def power(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fParser.PowerContext)
            else:
                return self.getTypedRuleContext(fParser.PowerContext,i)


        def getRuleIndex(self):
            return fParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)




    def power(self):

        localctx = fParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_power)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.factor()
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.match(fParser.T__17)
                    self.state = 156
                    self.power() 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(fParser.IdentContext,0)


        def number(self):
            return self.getTypedRuleContext(fParser.NumberContext,0)


        def expression(self):
            return self.getTypedRuleContext(fParser.ExpressionContext,0)


        def bool_(self):
            return self.getTypedRuleContext(fParser.BoolContext,0)


        def getRuleIndex(self):
            return fParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = fParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.ident()
                pass
            elif token in [14, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.number()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(fParser.T__8)
                self.state = 165
                self.expression()
                self.state = 166
                self.match(fParser.T__10)
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fParser.RULE_assignmentOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOp" ):
                listener.enterAssignmentOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOp" ):
                listener.exitAssignmentOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOp" ):
                return visitor.visitAssignmentOp(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOp(self):

        localctx = fParser.AssignmentOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignmentOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66584576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(fParser.IdentContext,0)


        def getRuleIndex(self):
            return fParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecStmt" ):
                return visitor.visitIncDecStmt(self)
            else:
                return visitor.visitChildren(self)




    def incDecStmt(self):

        localctx = fParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_incDecStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.ident()
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(fParser.IdentContext,0)


        def expression(self):
            return self.getTypedRuleContext(fParser.ExpressionContext,0)


        def getRuleIndex(self):
            return fParser.RULE_shortVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortVarDecl" ):
                listener.enterShortVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortVarDecl" ):
                listener.exitShortVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortVarDecl" ):
                return visitor.visitShortVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def shortVarDecl(self):

        localctx = fParser.ShortVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_shortVarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.ident()
            self.state = 177
            self.match(fParser.T__27)
            self.state = 178
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fParser.RULE_signs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigns" ):
                listener.enterSigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigns" ):
                listener.exitSigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigns" ):
                return visitor.visitSigns(self)
            else:
                return visitor.visitChildren(self)




    def signs(self):

        localctx = fParser.SignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_signs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = fParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = fParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Letter(self, i:int=None):
            if i is None:
                return self.getTokens(fParser.Letter)
            else:
                return self.getToken(fParser.Letter, i)

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(fParser.Digit)
            else:
                return self.getToken(fParser.Digit, i)

        def getRuleIndex(self):
            return fParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = fParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(fParser.Letter)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42 or _la==43:
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(fParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(fParser.FloatContext,0)


        def getRuleIndex(self):
            return fParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = fParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_number)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.int_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.float_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(fParser.Digit)
            else:
                return self.getToken(fParser.Digit, i)

        def getRuleIndex(self):
            return fParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = fParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==14:
                        self.state = 197
                        self.match(fParser.T__13)


                    self.state = 200
                    self.match(fParser.Digit)

                else:
                    raise NoViableAltException(self)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(fParser.Digit)
            else:
                return self.getToken(fParser.Digit, i)

        def getRuleIndex(self):
            return fParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = fParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 205
                    self.match(fParser.T__13)


                self.state = 208
                self.match(fParser.Digit)
                self.state = 211 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14 or _la==43):
                    break

            self.state = 213
            self.match(fParser.T__39)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 214
                self.match(fParser.Digit)
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==43):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





