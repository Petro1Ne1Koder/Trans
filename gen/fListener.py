# Generated from C:/Trans/Lab5/f.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .fParser import fParser
else:
    from fParser import fParser

# This class defines a complete listener for a parse tree produced by fParser.
class fListener(ParseTreeListener):

    # Enter a parse tree produced by fParser#program.
    def enterProgram(self, ctx:fParser.ProgramContext):
        pass

    # Exit a parse tree produced by fParser#program.
    def exitProgram(self, ctx:fParser.ProgramContext):
        pass


    # Enter a parse tree produced by fParser#name.
    def enterName(self, ctx:fParser.NameContext):
        pass

    # Exit a parse tree produced by fParser#name.
    def exitName(self, ctx:fParser.NameContext):
        pass


    # Enter a parse tree produced by fParser#statement.
    def enterStatement(self, ctx:fParser.StatementContext):
        pass

    # Exit a parse tree produced by fParser#statement.
    def exitStatement(self, ctx:fParser.StatementContext):
        pass


    # Enter a parse tree produced by fParser#varDecl.
    def enterVarDecl(self, ctx:fParser.VarDeclContext):
        pass

    # Exit a parse tree produced by fParser#varDecl.
    def exitVarDecl(self, ctx:fParser.VarDeclContext):
        pass


    # Enter a parse tree produced by fParser#ifStatement.
    def enterIfStatement(self, ctx:fParser.IfStatementContext):
        pass

    # Exit a parse tree produced by fParser#ifStatement.
    def exitIfStatement(self, ctx:fParser.IfStatementContext):
        pass


    # Enter a parse tree produced by fParser#loopStatement.
    def enterLoopStatement(self, ctx:fParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by fParser#loopStatement.
    def exitLoopStatement(self, ctx:fParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by fParser#block.
    def enterBlock(self, ctx:fParser.BlockContext):
        pass

    # Exit a parse tree produced by fParser#block.
    def exitBlock(self, ctx:fParser.BlockContext):
        pass


    # Enter a parse tree produced by fParser#simpleStmt.
    def enterSimpleStmt(self, ctx:fParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by fParser#simpleStmt.
    def exitSimpleStmt(self, ctx:fParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by fParser#input.
    def enterInput(self, ctx:fParser.InputContext):
        pass

    # Exit a parse tree produced by fParser#input.
    def exitInput(self, ctx:fParser.InputContext):
        pass


    # Enter a parse tree produced by fParser#output.
    def enterOutput(self, ctx:fParser.OutputContext):
        pass

    # Exit a parse tree produced by fParser#output.
    def exitOutput(self, ctx:fParser.OutputContext):
        pass


    # Enter a parse tree produced by fParser#condition.
    def enterCondition(self, ctx:fParser.ConditionContext):
        pass

    # Exit a parse tree produced by fParser#condition.
    def exitCondition(self, ctx:fParser.ConditionContext):
        pass


    # Enter a parse tree produced by fParser#expression.
    def enterExpression(self, ctx:fParser.ExpressionContext):
        pass

    # Exit a parse tree produced by fParser#expression.
    def exitExpression(self, ctx:fParser.ExpressionContext):
        pass


    # Enter a parse tree produced by fParser#term.
    def enterTerm(self, ctx:fParser.TermContext):
        pass

    # Exit a parse tree produced by fParser#term.
    def exitTerm(self, ctx:fParser.TermContext):
        pass


    # Enter a parse tree produced by fParser#power.
    def enterPower(self, ctx:fParser.PowerContext):
        pass

    # Exit a parse tree produced by fParser#power.
    def exitPower(self, ctx:fParser.PowerContext):
        pass


    # Enter a parse tree produced by fParser#factor.
    def enterFactor(self, ctx:fParser.FactorContext):
        pass

    # Exit a parse tree produced by fParser#factor.
    def exitFactor(self, ctx:fParser.FactorContext):
        pass


    # Enter a parse tree produced by fParser#assignmentOp.
    def enterAssignmentOp(self, ctx:fParser.AssignmentOpContext):
        pass

    # Exit a parse tree produced by fParser#assignmentOp.
    def exitAssignmentOp(self, ctx:fParser.AssignmentOpContext):
        pass


    # Enter a parse tree produced by fParser#incDecStmt.
    def enterIncDecStmt(self, ctx:fParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by fParser#incDecStmt.
    def exitIncDecStmt(self, ctx:fParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by fParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:fParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by fParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:fParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by fParser#signs.
    def enterSigns(self, ctx:fParser.SignsContext):
        pass

    # Exit a parse tree produced by fParser#signs.
    def exitSigns(self, ctx:fParser.SignsContext):
        pass


    # Enter a parse tree produced by fParser#type.
    def enterType(self, ctx:fParser.TypeContext):
        pass

    # Exit a parse tree produced by fParser#type.
    def exitType(self, ctx:fParser.TypeContext):
        pass


    # Enter a parse tree produced by fParser#bool.
    def enterBool(self, ctx:fParser.BoolContext):
        pass

    # Exit a parse tree produced by fParser#bool.
    def exitBool(self, ctx:fParser.BoolContext):
        pass


    # Enter a parse tree produced by fParser#ident.
    def enterIdent(self, ctx:fParser.IdentContext):
        pass

    # Exit a parse tree produced by fParser#ident.
    def exitIdent(self, ctx:fParser.IdentContext):
        pass


    # Enter a parse tree produced by fParser#number.
    def enterNumber(self, ctx:fParser.NumberContext):
        pass

    # Exit a parse tree produced by fParser#number.
    def exitNumber(self, ctx:fParser.NumberContext):
        pass


    # Enter a parse tree produced by fParser#int.
    def enterInt(self, ctx:fParser.IntContext):
        pass

    # Exit a parse tree produced by fParser#int.
    def exitInt(self, ctx:fParser.IntContext):
        pass


    # Enter a parse tree produced by fParser#float.
    def enterFloat(self, ctx:fParser.FloatContext):
        pass

    # Exit a parse tree produced by fParser#float.
    def exitFloat(self, ctx:fParser.FloatContext):
        pass



del fParser