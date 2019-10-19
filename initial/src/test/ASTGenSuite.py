# 1712657
# Đặng Hoàng Phúc

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_1(self):
        input = """int i;"""
        expect = str(
            Program([
                VarDecl('i', IntType())
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    
    def test_var_decl_2(self):
        input = '''
        int i;
        string str;
        '''
        expect = str(
            Program([
                VarDecl('i', IntType()),
                VarDecl('str', StringType())
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_var_decl_3(self):
        input = '''
        int a,b;
        '''
        expect = str(
            Program([
                VarDecl('a', IntType()),
                VarDecl('b', IntType())
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_var_decl_4(self):
        input = '''
        int i[2];
        '''
        expect = str(
            Program([
                VarDecl('i', ArrayType(2, IntType()))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_var_decl_5(self):
        input = '''
        float x[3], y[0];
        string a[3];
        '''
        expect = str(
            Program([
                VarDecl('x', ArrayType(3,FloatType())),
                VarDecl('y', ArrayType(0, FloatType())),
                VarDecl('a', ArrayType(3, StringType()))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_func_declare_1(self):
        input = '''
        int main() {

        }
        '''
        expect = str(
            Program([FuncDecl(Id('main'),[],IntType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_func_declare_2(self):
        input = '''
        int[] a() {
        }
        '''
        expect = str(
            Program([
                FuncDecl(
                    Id('a'),
                    [],
                    ArrayPointerType(IntType()),
                    Block([])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_func_declare_3(self):
        input = '''
        int a(int b[]) {

        }
        '''
        expect = str(
            Program([
                FuncDecl(
                    Id('a'),
                    [VarDecl('b',ArrayPointerType(IntType()))],
                    IntType(),
                    Block([])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_func_declare_4(self):
        input = '''
        void main() {
            int a, b, c[9];
        }
        '''
        expect = str(
            Program([
                FuncDecl(
                    Id('main'),
                    [],
                    VoidType(),
                    Block([
                        VarDecl('a',IntType()),
                        VarDecl('b',IntType()),
                        VarDecl('c',ArrayType(9,IntType()))
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_fucn_decl_5(self):
        input = """
        float z(){
            int c,d;
        }
        void ui3() {

        }
        int[] main(int a){
            return;
        }
        """
        expect = str(Program([FuncDecl(Id("z"),[],FloatType(),Block([VarDecl("c",IntType()),VarDecl("d",IntType())])),FuncDecl(Id("ui3"),[],VoidType(),Block([])),FuncDecl(Id("main"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_fucn_decl_6(self):
        input = """
        int[] main(int a[]){
            return;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_fucn_decl_7(self):
        input = """
        void main() {}
        float a() {
            {}
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("a"),[],FloatType(),Block([Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_fucn_decl_8(self):
        input = """
        int[] main(int a){
            return;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_fucn_decl_9(self):
        input = """
        float[] main(){}
        int a() {}
        """
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("a"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_fucn_decl_10(self):
        input = """
        void main    (int argc, int argv)
        {        }
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",IntType()),VarDecl("argv",IntType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_fucn_decl_11(self):
        input = """
        int intlit(int c, int b[]){
        }
        """
        expect = str(Program([FuncDecl(Id("intlit"),[VarDecl("c",IntType()),VarDecl("b",ArrayPointerType(IntType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_fucn_decl_12(self):
        input = """
        int[] main(int a){
            return;
        }
        boolean[] intint(){}
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([Return()])),FuncDecl(Id("intint"),[],ArrayPointerType(BoolType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_if_stmt_1(self):
        input = """
        int main(){
            if (true) a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BooleanLiteral(True),Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
        
    def test_if_stmt_2(self):
        input = """
        int main(){
            if (!a) 1+1;
            if (false) {}
         }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(UnaryOp('!',Id('a')),BinaryOp('+',IntLiteral(1),IntLiteral(1))),If(BooleanLiteral(False),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

       
    def test_if_stmt_3(self):
        input = """
        int main(){
            if (1+1==2) if (true) return;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('==',BinaryOp('+',IntLiteral(1),IntLiteral(1)),IntLiteral(2)),If(BooleanLiteral(True),Return()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
        
    def test_if_stmt_4(self):
        input = """
        int main(){
            if (!!a) if (b) foo(2); else foo1();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(UnaryOp('!',UnaryOp('!',Id('a'))),If(Id('b'),CallExpr(Id('foo'),[IntLiteral(2)]),CallExpr(Id('foo1'),[])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
        
           
    def test_if_stmt_5(self):
        input = """
        int main(){
            if (foo() && true) 
            if (ui) if (0) if (isValid()) foo1();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('&&',CallExpr(Id('foo'),[]),BooleanLiteral(True)),If(Id('ui'),If(IntLiteral(0),If(CallExpr(Id('isValid'),[]),CallExpr(Id('foo1'),[])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
        
    def test_if_stmt_6(self):
        input = """
        float main(){
            if( anhiuem ) if ( anhgiau ) emlayanh(); else emthichanh(); else cutmemdi();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],FloatType(),Block([If(Id('anhiuem'),If(Id('anhgiau'),CallExpr(Id('emlayanh'),[]),CallExpr(Id('emthichanh'),[])),CallExpr(Id('cutmemdi'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
        
           
    def test_if_stmt_7(self):
        input = """
        int main(){
            if (true) {
                if (true) return true;
                else if(false) return 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BooleanLiteral(True),Return(BooleanLiteral(True)),If(BooleanLiteral(False),Return(IntLiteral(1))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
        
    def test_if_stmt_8(self):
        input = """
        void main(int argc, int argv){
            if (12) 90; else 12;
        }   
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',IntType())],VoidType(),Block([If(IntLiteral(12),IntLiteral(90),IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
        
           
    def test_while_stmt_1(self):
        input = """
        int main(){
            do foo();
            while (1+1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([CallExpr(Id('foo'),[])],BinaryOp('+',IntLiteral(1),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
        
    def test_while_stmt_2(self):
        input = """
        int main(){
            do do {} while true; while true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
        
           
    def test_while_stmt_3(self):
        input = """
        int main(){
            do 1-2; while (foo(2));
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('-',IntLiteral(1),IntLiteral(2))],CallExpr(Id('foo'),[IntLiteral(2)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
        
    def test_while_stmt_4(self):
        input = """
        int main(int argc, float argv){
            do 
                3;
                12;
            while true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',FloatType())],IntType(),Block([Dowhile([IntLiteral(3),IntLiteral(12)],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
        
           
    def test_while_stmt_5(self):
        input = """
        int main(){
            do {}
                3;
                12;
                do {}
                3;
                12;
            while (1+2);
            while true;

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([]),IntLiteral(3),IntLiteral(12),Dowhile([Block([]),IntLiteral(3),IntLiteral(12)],BinaryOp('+',IntLiteral(1),IntLiteral(2)))],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
        
    def test_while_stmt_6(self):
        input = """
        int main(){
            do {{{}}} while a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([Block([Block([])])])],Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
        
           
    def test_while_stmt_7(self):
        input = """
        int main(){
            do {
                foo();
                1+1=2;
                if (true) return 12;
            }
            while i!=3;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([CallExpr(Id('foo'),[]),BinaryOp('=',BinaryOp('+',IntLiteral(1),IntLiteral(1)),IntLiteral(2)),If(BooleanLiteral(True),Return(IntLiteral(12)))])],BinaryOp('!=',Id('i'),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
        
    def test_while_stmt_8(self):
        input = """
        int main(){
            do 
                do
                    do
                        do
                            print("Hello World!");
                        while a;
                    while a;
                while a;
            while a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([CallExpr(Id('print'),[StringLiteral('Hello World!')])],Id('a'))],Id('a'))],Id('a'))],Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
        
           
    def test_while_stmt_9(self):
        input = """
        int main(){
            do int a,b,c;
            while true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Id('a'),Id('b'),Id('c')],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
        
    def test_while_stmt_10(self):
        input = """
        int main(){
            do foo (); {
                sayhaha();
            }
            while i();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([CallExpr(Id('foo'),[]),Block([CallExpr(Id('sayhaha'),[])])],CallExpr(Id('i'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
        
           
    def test_for_stmt_1(self):
        input = """
        int main(){
            for (a;a;a) {
                i=i+2;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('a'),Id('a'),Id('a'),Block([BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
        
    def test_for_stmt_2(self):
        input = """
        int main(){
            for (a=1;a<2;a=a+1) 
                for (i;i<2;i+2) return false;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(2)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),For(Id('i'),BinaryOp('<',Id('i'),IntLiteral(2)),BinaryOp('+',Id('i'),IntLiteral(2)),Return(BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
        
           
    def test_for_stmt_3(self):
        input = """
        int main(){
            for (a=1;a<2;a=a+1) 
            for (i;i<2;i+2) 
            for (a=1;a<2;a=a+1) 
            for (i;i<2;i+2) printf("a",b);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(2)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),For(Id('i'),BinaryOp('<',Id('i'),IntLiteral(2)),BinaryOp('+',Id('i'),IntLiteral(2)),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(2)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),For(Id('i'),BinaryOp('<',Id('i'),IntLiteral(2)),BinaryOp('+',Id('i'),IntLiteral(2)),CallExpr(Id('printf'),[StringLiteral('a'),Id('b')])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
        
    def test_for_stmt_4(self):
        input = """
        int main(){
            {
                for(foo();in();12+3) true;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Block([For(CallExpr(Id('foo'),[]),CallExpr(Id('in'),[]),BinaryOp('+',IntLiteral(12),IntLiteral(3)),BooleanLiteral(True))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
        
           
    def test_for_stmt_5(self):
        input = """
        int main(){
            for (i;i<=3;i=i+1) {
                for (x; 2; x+2) i=i+3;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('i'),BinaryOp('<=',Id('i'),IntLiteral(3)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([For(Id('x'),IntLiteral(2),BinaryOp('+',Id('x'),IntLiteral(2)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(3))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
        
    def test_for_stmt_6(self):
        input = """
        int main(){
            for (true; a; k) {
                {
                    int n, i[2];
                    if (i<2) a[2] + 8;
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BooleanLiteral(True),Id('a'),Id('k'),Block([Block([VarDecl('n',IntType()),VarDecl('i',ArrayType(2,IntType())),If(BinaryOp('<',Id('i'),IntLiteral(2)),BinaryOp('+',ArrayCell(Id('a'),IntLiteral(2)),IntLiteral(8)))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
        
           
    def test_for_stmt_7(self):
        input = """
        int main(){
            int a,b,i[2];
            foo(12,3,4+5,"as");
            for (a;b;c) printf(a,b,c);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('i',ArrayType(2,IntType())),CallExpr(Id('foo'),[IntLiteral(12),IntLiteral(3),BinaryOp('+',IntLiteral(4),IntLiteral(5)),StringLiteral('as')]),For(Id('a'),Id('b'),Id('c'),CallExpr(Id('printf'),[Id('a'),Id('b'),Id('c')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
        
    def test_for_stmt_8(self):
        input = """
        int main(){
            if ((1-2)!=3) for (a;b;c) i();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('!=',BinaryOp('-',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),For(Id('a'),Id('b'),Id('c'),CallExpr(Id('i'),[])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
        
           
    def test_for_stmt_9(self):
        input = """
        int main(){
            for (i;i;i) i=i+2;
            {
                {x=3;}
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('i'),Id('i'),Id('i'),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2)))),Block([Block([BinaryOp('=',Id('x'),IntLiteral(3))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
        
    def test_for_stmt_10(self):
        input = """
        int main(){
            for (i;i;i) i=i+2;
            {
                for (i;i;i) i=i+2; {x=3;}
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('i'),Id('i'),Id('i'),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2)))),Block([For(Id('i'),Id('i'),Id('i'),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2)))),Block([BinaryOp('=',Id('x'),IntLiteral(3))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
        
           
    def test_expr_1(self):
        input = """
        int main(){
            int value;
            value;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('value',IntType()),Id('value')]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
        
    def test_expr_2(self):
        input = """
        int main(){
            test_expr_1(1,2,3,"thisisstring!@#$%^&");
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('test_expr_1'),[IntLiteral(1),IntLiteral(2),IntLiteral(3),StringLiteral('thisisstring!@#$%^&')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
        
           
    def test_expr_3(self):
        input = """
        int main(){
            int callback;
            callback("2") + 3/4 - 5;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('callback',IntType()),BinaryOp('-',BinaryOp('+',CallExpr(Id('callback'),[StringLiteral('2')]),BinaryOp('/',IntLiteral(3),IntLiteral(4))),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
        
    def test_expr_4(self):
        input = """
        int b;
        boolean foo(int a) {
            if (a==2) return true;
        }
        int main(){
            foo(1)*2==3;
        }
        """
        expect = str(Program([VarDecl('b',IntType()),FuncDecl(Id('foo'),[VarDecl('a',IntType())],BoolType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(2)),Return(BooleanLiteral(True)))])),FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('==',BinaryOp('*',CallExpr(Id('foo'),[IntLiteral(1)]),IntLiteral(2)),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
        
           
    def test_expr_5(self):
        input = """
        int main(){
            string str;
            str = "1+2/3*4" + "23";
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('str',StringType()),BinaryOp('=',Id('str'),BinaryOp('+',StringLiteral('1+2/3*4'),StringLiteral('23')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
        
    def test_expr_6(self):
        input = """
        int main(){
            !i+ -!j==2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('==',BinaryOp('+',UnaryOp('!',Id('i')),UnaryOp('-',UnaryOp('!',Id('j')))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
        
    ## 2 error
    def test_expr_7(self):
        input = """
        int main(){
            int value;
            value = ((a));
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('value',IntType()),BinaryOp('=',Id('value'),Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
        
    def test_expr_8(self):
        input = """
        int main(){
            float f;
            f = 1.23e4 + 9/2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('f',FloatType()),BinaryOp('=',Id('f'),BinaryOp('+',FloatLiteral(12300.0),BinaryOp('/',IntLiteral(9),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
        
           
    def test_expr_9(self):
        input = """
        int main(){
            float f, a[2];
            f = (1.23e4 + 9)/2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('f',FloatType()),VarDecl('a',ArrayType(2,FloatType())),BinaryOp('=',Id('f'),BinaryOp('/',BinaryOp('+',FloatLiteral(12300.0),IntLiteral(9)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
        
    def test_expr_10(self):
        input = """
        int main(){
            a = (1+2)*3/(5+4) - 12 || 5;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('-',BinaryOp('/',BinaryOp('*',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp('+',IntLiteral(5),IntLiteral(4))),IntLiteral(12)),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
        
           
    def test_expr_11(self):
        input = """
        int main(){
            a[2]+foo(2)[3];
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',ArrayCell(Id('a'),IntLiteral(2)),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
        
    def test_expr_12(self):
        input = """
        int main(){
            (foo(a(12)[9]))[2] + 3;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',ArrayCell(CallExpr(Id('foo'),[ArrayCell(CallExpr(Id('a'),[IntLiteral(12)]),IntLiteral(9))]),IntLiteral(2)),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
        
    def test_expr_13(self):
        input = """
        int main(){
            "12376aKLASHD" + "hello World__" == 3;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('==',BinaryOp('+',StringLiteral('12376aKLASHD'),StringLiteral('hello World__')),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
        
    def test_expr_14(self):
        input = """
        int main(){
           !!-profe(a[12+3+a])*8;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('*',UnaryOp('!',UnaryOp('!',UnaryOp('-',CallExpr(Id('profe'),[ArrayCell(Id('a'),BinaryOp('+',BinaryOp('+',IntLiteral(12),IntLiteral(3)),Id('a')))])))),IntLiteral(8))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
        
    def test_expr_15(self):
        input = """
        int main(){
            -------a + ---------b + (c);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',BinaryOp('+',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',Id('a')))))))),UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',Id('b'))))))))))),Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
        
    def test_expr_16(self):
        input = """
        int main(){
            ---a[2+a[3]] + b + (c);        
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',BinaryOp('+',UnaryOp('-',UnaryOp('-',UnaryOp('-',ArrayCell(Id('a'),BinaryOp('+',IntLiteral(2),ArrayCell(Id('a'),IntLiteral(3))))))),Id('b')),Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
        
           
    def test_expr_17(self):
        input = """
        int main(){
            a=(((((((((a))))))))+2);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
        
    def test_expr_18(self):
        input = """
        int main(){
            a[12+a[a[a[a[2]]]]];
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([ArrayCell(Id('a'),BinaryOp('+',IntLiteral(12),ArrayCell(Id('a'),ArrayCell(Id('a'),ArrayCell(Id('a'),ArrayCell(Id('a'),IntLiteral(2)))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
        
           
    def test_expr_19(self):
        input = """
        int main(){
            1 && 2 && 3 && 4;
        }
        int a(int c, int b) {}
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4))])),FuncDecl(Id('a'),[VarDecl('c',IntType()),VarDecl('b',IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
        
    def test_expr_20(self):
        input = """
        int main(){
            ___ + ____ * _________;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',Id('___'),BinaryOp('*',Id('____'),Id('_________')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
        
           
    def test_expr_21(self):
        input = """
        float[] foo(int a[]) {
            a = a[a[foo(a)]*(b+c)];
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(IntType()))],ArrayPointerType(FloatType()),Block([BinaryOp('=',Id('a'),ArrayCell(Id('a'),BinaryOp('*',ArrayCell(Id('a'),CallExpr(Id('foo'),[Id('a')])),BinaryOp('+',Id('b'),Id('c')))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
        
    def test_expr_22(self):
        input = """
        float foo() {
            value = ((sqrt(value)));
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],FloatType(),Block([BinaryOp('=',Id('value'),CallExpr(Id('sqrt'),[Id('value')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
        
           
    def test_return_stmt1(self):
        input = """
        float foo() {
            {
                value = 10;
            }
            return 1+2;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],FloatType(),Block([Block([BinaryOp('=',Id('value'),IntLiteral(10))]),Return(BinaryOp('+',IntLiteral(1),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
        
    def test_return_stmt2(self):
        input = """
        float foo() {
            return (____a+___b)[2];
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],FloatType(),Block([Return(ArrayCell(BinaryOp('+',Id('____a'),Id('___b')),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
        
           
    def test_return_stmt3(self):
        input = """
        int main(){
            return;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
        
    def test_return_stmt4(self):
        input = """
        float main(){
            return 001.67;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],FloatType(),Block([Return(FloatLiteral(1.67))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
        
           
    def test_break_stmt(self):
        input = """
        int main(){
            break;
            break;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Break(),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
        
    def test_continue_stmt(self):
        input = """
        int main(){
            for(i;i;i) {break;continue;}
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('i'),Id('i'),Id('i'),Block([Break(),Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
        
           
    def test_combine_1(self):
        input = """
        int main(){
            int a, b[2];
            for (i;i<10;i=i+2) print("in so thu: %d ", a);
            if (a==3) return true;
            else {print(false); return reu;}
            return 12;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',ArrayType(2,IntType())),For(Id('i'),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(2))),CallExpr(Id('print'),[StringLiteral('in so thu: %d '),Id('a')])),If(BinaryOp('==',Id('a'),IntLiteral(3)),Return(BooleanLiteral(True)),Block([CallExpr(Id('print'),[BooleanLiteral(False)]),Return(Id('reu'))])),Return(IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
        
    def test_combine_2(self):
        input = """
        int main() {
                a = b + c;
                for (a; b; c) {
                    printf("this is a typical string");
                }
                do return; while 1;
            } 
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),Id('c'))),For(Id('a'),Id('b'),Id('c'),Block([CallExpr(Id('printf'),[StringLiteral('this is a typical string')])])),Dowhile([Return()],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
        
           
    def test_combine_3(self):
        input = """
        /*void enter()
        {
        }

        void init()
        {
            {}
        }

        void print()
        {
        }
        */
        int main()
        {
            enter()
            init();
            print();
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('enter'),[]),CallExpr(Id('init'),[]),CallExpr(Id('print'),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
        
    def test_combine_4(self):
        input = """
        int a  () {
            foo(foo_89("stringlit")[12]);
        }
        """
        expect = str(Program([FuncDecl(Id('a'),[],IntType(),Block([CallExpr(Id('foo'),[ArrayCell(CallExpr(Id('foo_89'),[StringLiteral('stringlit')]),IntLiteral(12))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
        
           
    def test_combine_5(self):
        input = """
        int main(){
            func(arr[num], arr[num + 1], arr[num + 2]);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('func'),[ArrayCell(Id('arr'),Id('num')),ArrayCell(Id('arr'),BinaryOp('+',Id('num'),IntLiteral(1))),ArrayCell(Id('arr'),BinaryOp('+',Id('num'),IntLiteral(2)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
        
    def test_combine_6(self):
        input = """
        void main(){
            foo(x,y,z);
        }  
        int[] foo(float x, float y, float z) {
            float list[3];
            list = x + y + z + 0.e12;
            return list;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[Id('x'),Id('y'),Id('z')])])),FuncDecl(Id('foo'),[VarDecl('x',FloatType()),VarDecl('y',FloatType()),VarDecl('z',FloatType())],ArrayPointerType(IntType()),Block([VarDecl('list',ArrayType(3,FloatType())),BinaryOp('=',Id('list'),BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('x'),Id('y')),Id('z')),FloatLiteral(0.0))),Return(Id('list'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
        
           
    def test_combine_7(self):
        input = """
        void x() 
        
        {{
            do (print("12")); if (2+2==3) do x; while i; while true;
        }}
        """
        expect = str(Program([FuncDecl(Id('x'),[],VoidType(),Block([Block([Dowhile([CallExpr(Id('print'),[StringLiteral('12')]),If(BinaryOp('==',BinaryOp('+',IntLiteral(2),IntLiteral(2)),IntLiteral(3)),Dowhile([Id('x')],Id('i')))],BooleanLiteral(True))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
        
    def test_combine_8(self):
        input = """
        void main(){
            boolean x;
            x = false;
            if (isEq1(a)) x = true;
        }  
        boolean isEq1(int a) {
            if (a==1) return true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('x',BoolType()),BinaryOp('=',Id('x'),BooleanLiteral(False)),If(CallExpr(Id('isEq1'),[Id('a')]),BinaryOp('=',Id('x'),BooleanLiteral(True)))])),FuncDecl(Id('isEq1'),[VarDecl('a',IntType())],BoolType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(1)),Return(BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
        
           
    def test_combine_9(self):
        input = """
        void main(){
            for (x = 8; x>9 && y >12; x=x+1) {
                y = y+1;
                printf("%d");
            }
            return;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(BinaryOp('=',Id('x'),IntLiteral(8)),BinaryOp('&&',BinaryOp('>',Id('x'),IntLiteral(9)),BinaryOp('>',Id('y'),IntLiteral(12))),BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),Block([BinaryOp('=',Id('y'),BinaryOp('+',Id('y'),IntLiteral(1))),CallExpr(Id('printf'),[StringLiteral('%d')])])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
        
    def test_combine_0(self):
        input = """
        int main(){
        }
        void main(){
            for (x = 8; x>9 && y >12; x=x+1) {
                y = ((y+1)>2)>3;
            }
            return;
        } 
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([])),FuncDecl(Id('main'),[],VoidType(),Block([For(BinaryOp('=',Id('x'),IntLiteral(8)),BinaryOp('&&',BinaryOp('>',Id('x'),IntLiteral(9)),BinaryOp('>',Id('y'),IntLiteral(12))),BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),Block([BinaryOp('=',Id('y'),BinaryOp('>',BinaryOp('>',BinaryOp('+',Id('y'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)))])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_combine_10(self):
        input = """
        int main(){
            print(foo());
        }   
        int[] foo(int a) {
            if (a&&b&&c) do printf("a==b==c"); while x=x+1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('print'),[CallExpr(Id('foo'),[])])])),FuncDecl(Id('foo'),[VarDecl('a',IntType())],ArrayPointerType(IntType()),Block([If(BinaryOp('&&',BinaryOp('&&',Id('a'),Id('b')),Id('c')),Dowhile([CallExpr(Id('printf'),[StringLiteral('a==b==c')])],BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_combine_11(self):
        input = """
        int main(){
            float a,b,c;
            break;
            for(a;1;1) do print("a"); close(); while c;
            c = 9*2/3;
            return 12;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType()),Break(),For(Id('a'),IntLiteral(1),IntLiteral(1),Dowhile([CallExpr(Id('print'),[StringLiteral('a')]),CallExpr(Id('close'),[])],Id('c'))),BinaryOp('=',Id('c'),BinaryOp('/',BinaryOp('*',IntLiteral(9),IntLiteral(2)),IntLiteral(3))),Return(IntLiteral(12))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
        
    def test_combine_12(self):
        input = """
        int main() {
                a = b + c;
                for (a; b; c) {
                    printf("this is a typical stringn");
                }
                do return; while 1;
            }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),Id('c'))),For(Id('a'),Id('b'),Id('c'),Block([CallExpr(Id('printf'),[StringLiteral('this is a typical stringn')])])),Dowhile([Return()],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_combine_13(self):
        input = """
        int main(){
            commit(12) + 9;
            {
                string str1, strs[0];
                break;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('+',CallExpr(Id('commit'),[IntLiteral(12)]),IntLiteral(9)),Block([VarDecl('str1',StringType()),VarDecl('strs',ArrayType(0,StringType())),Break()])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    
    def test_combine_14(self):
        input = """
        int main(){
            for (a;b;c) {
                if (123) return false;
            }
            return;
        }  
        int a, b;

        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('a'),Id('b'),Id('c'),Block([If(IntLiteral(123),Return(BooleanLiteral(False)))])),Return()])),VarDecl('a',IntType()),VarDecl('b',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
        
    def test_combine_15(self):
        input = """
        int main(){
            check(check(check(check()[12])));
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('check'),[CallExpr(Id('check'),[CallExpr(Id('check'),[ArrayCell(CallExpr(Id('check'),[]),IntLiteral(12))])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_combine_16(self):
        input = """
        int main(){
            int socket = 12;
            if (socket=connect) return done;
            else return not_done;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('socket',IntType()),IntLiteral(12),If(BinaryOp('=',Id('socket'),Id('connect')),Return(Id('done')),Return(Id('not_done')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_combine_17(self):
        input = """
        int[] main(int a[]){
            google(12);
            print("http://facebook.com");
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('a',ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([CallExpr(Id('google'),[IntLiteral(12)]),CallExpr(Id('print'),[StringLiteral('http://facebook.com')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
        
    def test_combine_18(self):
        input = """
        int main(){
            int link_;
            int str;
            print("http://localhost:8000:7171");
            return foo(12);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('link_',IntType()),VarDecl('str',IntType()),CallExpr(Id('print'),[StringLiteral('http://localhost:8000:7171')]),Return(CallExpr(Id('foo'),[IntLiteral(12)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_combine_19(self):
        input = """
        int main(){
            d();
        }
        int d() {
            for (i = 0; i < 10; i = i + 1) {
                for (j = 10; j > 0; j=j-1) {
                    if (j == i)
                    {
                        break;
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('d'),[])])),FuncDecl(Id('d'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([For(BinaryOp('=',Id('j'),IntLiteral(10)),BinaryOp('>',Id('j'),IntLiteral(0)),BinaryOp('=',Id('j'),BinaryOp('-',Id('j'),IntLiteral(1))),Block([If(BinaryOp('==',Id('j'),Id('i')),Block([Break()]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))


    def test_combine_20(self):
        input = """
        int a,b,c;
        void main(){
            array[d[r[a(10)]]];
        }
        void rescusive(int i,float z){
            int x;
            int c;
            if(exp)
                stamentt;
        }
        """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([ArrayCell(Id('array'),ArrayCell(Id('d'),ArrayCell(Id('r'),CallExpr(Id('a'),[IntLiteral(10)]))))])),FuncDecl(Id('rescusive'),[VarDecl('i',IntType()),VarDecl('z',FloatType())],VoidType(),Block([VarDecl('x',IntType()),VarDecl('c',IntType()),If(Id('exp'),Id('stamentt'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
        
    def test_combine_21(self):
        input = """
        int main(){ 
            int a[4],i;
            do putInt(4); i=i+1; while a[-foo(i)]==true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',ArrayType(4,IntType())),VarDecl('i',IntType()),Dowhile([CallExpr(Id('putInt'),[IntLiteral(4)]),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))],BinaryOp('==',ArrayCell(Id('a'),UnaryOp('-',CallExpr(Id('foo'),[Id('i')]))),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_combine_22(self):
        input = """
        void main(){
            int test, booltrue;
            test=f();
            putIntLn(test);
            {
                int i;
                int test;
                int f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);

            }
            putIntLn(test);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('test',IntType()),VarDecl('booltrue',IntType()),BinaryOp('=',Id('test'),CallExpr(Id('f'),[])),CallExpr(Id('putIntLn'),[Id('test')]),Block([VarDecl('i',IntType()),VarDecl('test',IntType()),VarDecl('f',IntType()),BinaryOp('=',Id('test'),BinaryOp('=',Id('f'),BinaryOp('=',Id('i'),IntLiteral(100)))),CallExpr(Id('putIntLn'),[Id('i')]),CallExpr(Id('putIntLn'),[Id('test')]),CallExpr(Id('putIntLn'),[Id('f')])]),CallExpr(Id('putIntLn'),[Id('test')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
    def test_combine_23(self):
        input = """
        int main(){
            boolean check;
            if(!check) print(check);
            else {
                print(!check);
            }                  
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('check',BoolType()),If(UnaryOp('!',Id('check')),CallExpr(Id('print'),[Id('check')]),Block([CallExpr(Id('print'),[UnaryOp('!',Id('check'))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
        
    def test_combine_24(self):
        input = """
        int main(){
            int a,b,c;
            a=b=c=5;
            float f[5];
            if (a==b) f[0]=1.0; 
            return a+foo();     
        }
        int foo(){
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),BinaryOp('=',Id('a'),BinaryOp('=',Id('b'),BinaryOp('=',Id('c'),IntLiteral(5)))),VarDecl('f',ArrayType(5,FloatType())),If(BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',ArrayCell(Id('f'),IntLiteral(0)),FloatLiteral(1.0))),Return(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])))])),FuncDecl(Id('foo'),[],IntType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_combine_25(self):
        input = """
        int main(int argc){
            int b,c;
        }
        void foo(string a)
        {
                return a[0];
        }
            void main(){
                int arr[10];
                float f;
                f = 0;
                do f=f+foo(arr); f=f+1; while (foo(arr)+f)<100;
                return;
            }
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType())],IntType(),Block([VarDecl('b',IntType()),VarDecl('c',IntType())])),FuncDecl(Id('foo'),[VarDecl('a',StringType())],VoidType(),Block([Return(ArrayCell(Id('a'),IntLiteral(0)))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('arr',ArrayType(10,IntType())),VarDecl('f',FloatType()),BinaryOp('=',Id('f'),IntLiteral(0)),Dowhile([BinaryOp('=',Id('f'),BinaryOp('+',Id('f'),CallExpr(Id('foo'),[Id('arr')]))),BinaryOp('=',Id('f'),BinaryOp('+',Id('f'),IntLiteral(1)))],BinaryOp('<',BinaryOp('+',CallExpr(Id('foo'),[Id('arr')]),Id('f')),IntLiteral(100))),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_combine_26(self):
        input = """
        int a[1], b;
        void main(){
                int i, temp;
                for(i=1;i<10;i=i+1)
                    {
                        if(temp<10)
                            temp=temp+1;
                    }
                return;
            }
        """
        expect = str(Program([VarDecl('a',ArrayType(1,IntType())),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('temp',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('<',Id('temp'),IntLiteral(10)),BinaryOp('=',Id('temp'),BinaryOp('+',Id('temp'),IntLiteral(1))))])),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
        