# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitivetype.
    def visitPrimitivetype(self, ctx:MCParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variablelist.
    def visitVariablelist(self, ctx:MCParser.VariablelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcname.
    def visitFuncname(self, ctx:MCParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameterlist.
    def visitParameterlist(self, ctx:MCParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter.
    def visitParameter(self, ctx:MCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockitem.
    def visitBlockitem(self, ctx:MCParser.BlockitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expstmt.
    def visitExpstmt(self, ctx:MCParser.ExpstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)



del MCParser