# Generated from C:/Trans/Lab5/f.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .fParser import fParser
else:
    from fParser import fParser

# This class defines a complete generic visitor for a parse tree produced by fParser.

class fVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fParser#program.
    def visitProgram(self, ctx:fParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#statement.
    def visitStatement(self, ctx:fParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#varDecl.
    def visitVarDecl(self, ctx:fParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#ifStatement.
    def visitIfStatement(self, ctx:fParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#loopStatement.
    def visitLoopStatement(self, ctx:fParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#block.
    def visitBlock(self, ctx:fParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#simpleStmt.
    def visitSimpleStmt(self, ctx:fParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#input.
    def visitInput(self, ctx:fParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#output.
    def visitOutput(self, ctx:fParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#condition.
    def visitCondition(self, ctx:fParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#expression.
    def visitExpression(self, ctx:fParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#term.
    def visitTerm(self, ctx:fParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#power.
    def visitPower(self, ctx:fParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#factor.
    def visitFactor(self, ctx:fParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#assignmentOp.
    def visitAssignmentOp(self, ctx:fParser.AssignmentOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#incDecStmt.
    def visitIncDecStmt(self, ctx:fParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:fParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#signs.
    def visitSigns(self, ctx:fParser.SignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#type.
    def visitType(self, ctx:fParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#bool.
    def visitBool(self, ctx:fParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#ident.
    def visitIdent(self, ctx:fParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#number.
    def visitNumber(self, ctx:fParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#int.
    def visitInt(self, ctx:fParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fParser#float.
    def visitFloat(self, ctx:fParser.FloatContext):
        return self.visitChildren(ctx)



del fParser