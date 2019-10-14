from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


class ASTGeneration(MCVisitor):
    #program  : decl+ EOF;
    def visitProgram(self, ctx: MCParser.ProgramContext):
        return Program(
            i for x in ctx.decl() for i in self.visit(x)
        )

    #decl: vardecl | funcdecl;
    def visitDecl(self, ctx: MCParser.DeclContext):
        return self.visit(ctx.getChild(0))

    #mctype: primitivetype| VOIDTYPE| arraypointertype;
    def visitMctype(self, ctx: MCParser.MctypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        else:
            return self.visit(ctx.getChild(0))

    #primitivetype:  INTTYPE | FLOATTYPE | STRINGTYPE | BOOLEANTYPE;
    def visitPrimitivetype(self, ctx: MCParser.PrimitivetypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        else:
            return BoolType()

    # arraypointertype: primitivetype LSB RSB;
    def visitArraypointertype(self, ctx: MCParser.ArraypointertypeContext):
        return ArrayPointerType(self.visit(ctx.primitivetype()))

    #literal: BOOLEANLIT|INTLIT|STRINGLIT|FLOATLIT;
    def visitLiteral(self, ctx: MCParser.LiteralContext):
        if ctx.BOOLEANLIT():
            return BooleanLiteral(bool("1" if ctx.BOOLEANLIT().getText() == 'true' else ""))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return FloatLiteral(float(ctx.FLOATLIT().getText()))

    # vardecl: primitivetype variablelist SEMI;
    def visitVardecl(self, ctx: MCParser.VardeclContext):
        def create(item):
            if item[0] == 1:
                return VarDecl(
                    item[1],
                    self.visit(ctx.primitivetype())
                )
            elif item[0] == 2:
                return VarDecl(
                    item[1],
                    ArrayType(item[2], self.visit(ctx.primitivetype()),)
                )
            else:
                return VarDecl(
                    item[1],
                    ArrayPointerType(self.visit(ctx.primitivetype()),)
                )
        return list(map(
            create,
            self.visit(ctx.variablelist())
        ))

    # variablelist: variable (CM variable)*;
    def visitVariablelist(self, ctx: MCParser.VariablelistContext):
        return [self.visit(variable) for variable in ctx.variable()]

    # variable: ID (LSB INTLIT RSB)?;
    def visitVariable(self, ctx: MCParser.VariableContext):
        if ctx.getChildCount() == 1:
            return [1, (ctx.ID().getText())]
        elif ctx.getChildCount() == 4:
            return [2, (ctx.ID().getText()), int(ctx.INTLIT().getText())]
        elif ctx.getChildCount() == 3:
            return [3, (ctx.ID().getText())]

    # funcdecl: mctype funcname LB parameterlist? RB blockstatement;
    def visitFuncdecl(self, ctx: MCParser.FuncdeclContext):
        return [FuncDecl(
            Id(self.visit(ctx.funcname())),
            self.visit(ctx.parameterlist()) if ctx.parameterlist() else [],
            self.visit(ctx.mctype()),
            self.visit(ctx.blockstmt()),
        )]

    #funcname: ID;
    def visitFuncname(self, ctx: MCParser.FuncnameContext):
        return ctx.ID().getText()

    # parameterlist: parameter (CM parameter)* ;
    def visitParameterlist(self, ctx: MCParser.ParameterlistContext):
        return [ self.visit(parameter) for parameter in ctx.parameter() ]

    # parameter: primitivetype ID | primitivetype ID LSB RSB;
    def visitParameter(self, ctx: MCParser.ParameterContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(), self.visit(ctx.primitivetype()))
        else:
            return VarDecl(ctx.ID().getText(), 
                    ArrayPointerType(self.visit(ctx.primitivetype()))
                )

    def visitStmt(self, ctx: MCParser.ParameterContext):
        if ctx.ifstmt(): return self.visit(ctx.ifstmt())
        if ctx.expstmt(): return self.visit(ctx.expstmt())
        if ctx.dowhilestmt(): return self.visit(ctx.dowhilestmt())
        if ctx.forstmt(): return self.visit(ctx.forstmt())
        if ctx.returnstmt(): return self.visit(ctx.returnstmt())
        if ctx.continuestmt(): return self.visit(ctx.continuestmt())
        if ctx.breakstmt(): return self.visit(ctx.breakstmt())
        if ctx.blockstmt(): return self.visit(ctx.blockstmt())


    #ifstmt: IF LB expr RB stmt (ELSE stmt)?;      
    def visitIfstmt(self, ctx: MCParser.IfstmtContext):
        if ctx.getChildCount() == 7:
            return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        else:
            return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))

    #blockstmt: LP (stmt|vardecl)* RP;    
    def visitBlockstmt(self, ctx: MCParser.BlockstmtContext):
        return Block(
                [i for item in ctx.blockitem() for i in self.visit(item)]
            )

    def visitBlockitem(self, ctx: MCParser.BlockitemContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return [self.visit(ctx.stmt())]

    #dowhilestmt: DO (stmt)+ WHILE expr SEMI;
    def visitDowhilestmt(self, ctx: MCParser.DowhilestmtContext):
        return Dowhile([self.visit(stmt) for stmt in ctx.stmt()], self.visit(ctx.expr()))

    #forstmt: FOR LB expr SEMI expr SEMI expr RB stmt;
    def visitForstmt(self, ctx: MCParser.ForstmtContext):
        return For(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.expr(2)), self.visit(ctx.stmt()))

    #breakstmt: BREAK SEMI;
    def visitBreakstmt(self, ctx: MCParser.BreakstmtContext):
        return Break()

    #continuestmt: CONTINUE SEMI;
    def visitContinuestmt(self, ctx: MCParser.ContinuestmtContext):
        return Continue()

    #returnstmt: RETURN expr? SEMI;
    def visitReturnstmt(self, ctx: MCParser.ReturnstmtContext):
        return Return() if (not ctx.expr()) else Return(self.visit(ctx.expr()))

    #expstmt: expr SEMI;
    def visitExpstmt(self, ctx: MCParser.ExpstmtContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MCParser#expr.
    #expr: expr1 ASSIGN expr | expr1;
    def visitExpr(self, ctx: MCParser.ExprContext):
        
        return self.visit(ctx.expr1()) if ctx.getChildCount() == 1 else BinaryOp(ctx.ASSIGN().getText(), self.visit(ctx.expr1()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MCParser#expr1.
    #expr1: expr1 OR expr2 | expr2;
    def visitExpr1(self, ctx: MCParser.Expr1Context):
        return self.visit(ctx.expr2()) if ctx.getChildCount() == 1 else BinaryOp(ctx.OR().getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2()))

    # Visit a parse tree produced by MCParser#expr2.
    #expr2: expr2 AND expr3 | expr3;
    def visitExpr2(self, ctx: MCParser.Expr2Context):
        return self.visit(ctx.expr3()) if ctx.getChildCount() == 1 else BinaryOp(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    # Visit a parse tree produced by MCParser#expr3.
    #expr3: expr4 (EQ|NEQ) expr4 | expr4;
    def visitExpr3(self, ctx: MCParser.Expr3Context):
        return self.visitExpr4(ctx.expr4(0)) if ctx.getChildCount() == 1 else BinaryOp(ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText(), self.visit(ctx.expr4(0)), self.visit(ctx.expr4(1)))
    
    # Visit a parse tree produced by MCParser#expr4.
    #expr4: expr5 (LESS|LESSEQ|GREATEREQ|GREATER) expr5 | expr5;
    def visitExpr4(self, ctx: MCParser.Expr4Context):
        def getOp(ctx):
            if (ctx.LESS()):
                return ctx.LESS().getText()
            if (ctx.LESSEQ()):
                return ctx.LESSEQ().getText()
            if (ctx.GREATER()):
                return ctx.GREATER().getText()
            if (ctx.GREATEREQ()):
                return ctx.GREATEREQ().getText()

        return self.visit(ctx.expr5(0)) if ctx.getChildCount() == 1 else BinaryOp(getOp(ctx), self.visit(ctx.expr5(0)), self.visit(ctx.expr5(1)))

    # Visit a parse tree produced by MCParser#expr5.
    #expr5: expr5 (ADD|SUB) expr6 | expr6;
    def visitExpr5(self, ctx: MCParser.Expr5Context):
        def getOp(ctx):
            if (ctx.ADD()):
                return ctx.ADD().getText()
            if (ctx.SUB()):
                return ctx.SUB().getText()

        return self.visit(ctx.expr6()) if ctx.getChildCount() == 1 else BinaryOp(getOp(ctx), self.visit(ctx.expr5()), self.visit(ctx.expr6()))


    # Visit a parse tree produced by MCParser#expr6.
    #expr6: expr6 (DIV|MUL|MOD) expr7 | expr7;
    def visitExpr6(self, ctx: MCParser.Expr6Context):
        def getOp(ctx):
            if (ctx.DIV()):
                return ctx.DIV().getText()
            if (ctx.MUL()):
                return ctx.MUL().getText()
            if (ctx.MOD()):
                return ctx.MOD().getText()

        return self.visit(ctx.expr7()) if ctx.getChildCount() == 1 else BinaryOp(getOp(ctx), self.visit(ctx.expr6()), self.visit(ctx.expr7()))

    # Visit a parse tree produced by MCParser#expr7.
    #expr7: (NOT|SUB) expr7 | expr8;
    def visitExpr7(self, ctx: MCParser.Expr7Context):
        def getOp(ctx):
            if (ctx.NOT()):
                return ctx.NOT().getText()
            if (ctx.SUB()):
                return ctx.SUB().getText()

        return self.visit(ctx.expr8()) if ctx.getChildCount() == 1 else UnaryOp(getOp(ctx), self.visit(ctx.expr7()))

    # Visit a parse tree produced by MCParser#expr8.
    #expr8: operands LSB expr RSB | operands;
    def visitExpr8(self, ctx: MCParser.Expr8Context):
        return self.visit(ctx.operands()) if ctx.getChildCount() == 1 else ArrayCell(self.visit(ctx.operands()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MCParser#operands.
    #operands: funcall | literal | ID | LB expr RB ;
    def visitOperands(self, ctx: MCParser.OperandsContext):
        if (ctx.ID()): return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0)) if ctx.getChildCount() == 1 else self.visit(ctx.expr())

    # Visit a parse tree produced by MCParser#funcall.
    #funcall: ID LB (expr (CM expr)*)? RB;
    def visitFuncall(self, ctx: MCParser.FuncallContext):
        return CallExpr(
            Id(ctx.ID().getText()), 
            [ self.visit(expr) for expr in ctx.expr()]
        )