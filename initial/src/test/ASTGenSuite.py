import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_1(self):
        ip = """
        int std_id;
        float sem_score;
        boolean isStudent;
        string myString;
        """
        expect = str(
            Program([VarDecl("std_id",IntType()),VarDecl("sem_score",FloatType()),VarDecl("isStudent",BoolType()),VarDecl("myString",StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 301))

    def test_var_decl_2(self):
        ip = """
        int alpha;
        int alpha, beta, gama;
        """
        expect = str(
            Program([VarDecl("alpha", IntType()), VarDecl("alpha", IntType()), VarDecl("beta", IntType()), VarDecl("gama", IntType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 302))

    def test_var_decl_3(self):
        ip = """
        float math_score[5], phys_score, chem_score;
        """
        expect = str(
            Program([VarDecl("math_score", ArrayType(5, FloatType())), VarDecl("phys_score", FloatType()),VarDecl("chem_score", FloatType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 303))

    def test_var_decl_4(self):
        ip = """
        int my_Arr[0], my_Arr[1], my_Arr[2];
        """
        expect = str(
            Program([VarDecl("my_Arr",ArrayType(0,IntType())),VarDecl("my_Arr",ArrayType(1,IntType())),VarDecl("my_Arr",ArrayType(2,IntType()))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 304))

    def test_var_decl_5(self):
        ip = """
        int i; float j; string k;
        """
        expect = str(
            Program([VarDecl("i", IntType()), VarDecl("j", FloatType()), VarDecl("k", StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 305))

    def test_var_decl_6(self):
        ip = """
        int a, b, c, d[4], e[5], f[6];
        """
        expect = str(
            Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(4,IntType())),VarDecl("e",ArrayType(5,IntType())),VarDecl("f",ArrayType(6,IntType()))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 306))

    def test_func_decl_1(self):
        ip = """
        void main(){}
        int main1(){}
        float main2(){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("main1"),[],IntType(),Block([])),FuncDecl(Id("main2"),[],FloatType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 307))

    def test_func_decl_2(self):
        ip = """
        float[] main1() {}
        boolean[] main2() {}
        """
        expect = str(
            Program([FuncDecl(Id("main1"),[],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("main2"),[],ArrayPointerType(BoolType()),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 308))

    def test_func_decl_3(self):
        ip = """
        void main(int a, int b, float c){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",FloatType())],VoidType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 309))

    def test_func_decl_4(self):
        ip = """
        int[] main(string a[], float b[], boolean c){}
        """
        expect = str(
            Program([FuncDecl(Id("main"),[VarDecl("a", ArrayPointerType(StringType())), VarDecl("b", ArrayPointerType(FloatType())),VarDecl("c", BoolType())], ArrayPointerType(IntType()), Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 310))

    def test_func_decl_5(self):
        ip = """
        boolean checksum(boolean etc, boolean check[])
        {
            \t
        }
        """
        expect = str(
            Program([FuncDecl(Id("checksum"),[VarDecl("etc",BoolType()),VarDecl("check",ArrayPointerType(BoolType()))],BoolType(),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 311))

    def test_program_1(self):
        ip = """
        int x, y, z;
        void main(){
            int x, y, z;
        }
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("z",IntType())]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 312))

    def test_program_2(self):
        ip = """
        int x, y;
        void main(){
            //nothing in block
        }
        string z;
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([])),VarDecl("z",StringType())])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 313))

    def test_program_3(self):
        ip = """
        int x, y;
        void main(int x[], int y){
            //nothing in block
        }
        string z;
        int[] prime(string z[]){
            //nothing in block
        }
        """
        expect = str(
            Program([VarDecl("x",IntType()),VarDecl("y",IntType()),FuncDecl(Id("main"),[VarDecl("x",ArrayPointerType(IntType())),VarDecl("y",IntType())],VoidType(),Block([])),VarDecl("z",StringType()),FuncDecl(Id("prime"),[VarDecl("z",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 314))

    def test_if_and_block_1(self):
        ip = """
        void main(){
            if ( a && b )
                if( a || b )
                    a || b ;
            else
                a && b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),BinaryOp("||",Id("a"),Id("b")),BinaryOp("&&",Id("a"),Id("b"))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 315))

    def test_if_and_block_2(self):
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b )
                    a || b ;
            }
            else
                a && b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"), [], VoidType(), Block([If(BinaryOp("&&", Id("a"), Id("b")), Block([If(BinaryOp("||", Id("a"), Id("b")), BinaryOp("||", Id("a"), Id("b")))]), BinaryOp("&&", Id("a"), Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 316))

    def test_if_and_block_3(self):
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b ){a || b ;}
                else
                {}
            }
            else{a && b ;}
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),Block([If(BinaryOp("||",Id("a"),Id("b")),Block([BinaryOp("||",Id("a"),Id("b"))]),Block([]))]),Block([BinaryOp("&&",Id("a"),Id("b"))]))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 317))

    def test_if_and_block_4(self):
        ip = """
        void main(){
            if (a && b)
            if (a || b)
            if (a == b)
            {}
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",Id("a"),Id("b")),If(BinaryOp("||",Id("a"),Id("b")),If(BinaryOp("==",Id("a"),Id("b")),Block([]))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 318))

    def test_if_and_block_5(self):
        ip = """
        int main(){
            if (a == b){
                if((a == b)){
                    if(((a == b))){ return 1; }
                    else{
                        return 0;
                    }
                }
            }
            else{
                if(a != b)
                {
                    return 0;
                }
                else
                    return 1;
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))]),Block([If(BinaryOp("!=",Id("a"),Id("b")),Block([Return(IntLiteral(0))]),Return(IntLiteral(1)))]))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 319))

    def test_dowhile_and_block_1(self):
        ip = """
        void main(){
            do {} {} {} {} {} {}
            {}
            while a == b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])],BinaryOp("==",Id("a"),Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 320))

    def test_dowhile_and_block_2(self):
        ip = """
        int[] main(){
        do {
            do {//\n} while ( a < 0);
        } while a == b ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"), [], ArrayPointerType(IntType()),Block([Dowhile([Block([Dowhile([Block([])],BinaryOp("<",Id("a"),IntLiteral(0)))])],BinaryOp("==",Id("a"),Id("b")))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 321))

    def test_dowhile_and_block_3(self):
        ip = """
        void main(){
            do {{{int i;}}} while b<0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Block([Block([VarDecl("i",IntType())])])])],BinaryOp("<", Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 322))

    def test_dowhile_and_block_4(self):
        ip = """
        void main(){
            do i = 5; while b<=0;
            do j = 5; while b>=0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(5))],BinaryOp("<=",Id("b"),IntLiteral(0))),Dowhile([BinaryOp("=",Id("j"),IntLiteral(5))],BinaryOp(">=",Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 323))

    def test_dowhile_and_block_5(self):
        ip = """
        void main(){
            do i =5; j = 5; k = 5; while b>=0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(5)),BinaryOp("=",Id("j"),IntLiteral(5)),BinaryOp("=",Id("k"),IntLiteral(5))],BinaryOp(">=",Id("b"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 324))

    def test_dowhile_and_block_6(self):
        ip = """
        void main(){
        do do {{if(a){}}} while 5 == 0 ; while 5 >= 10 ;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Block([Block([If(Id("a"),Block([]))])])],BinaryOp("==",IntLiteral(5),IntLiteral(0)))],BinaryOp(">=",IntLiteral(5),IntLiteral(10)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 325))

    def test_dowhile_and_block_7(self):
        ip = """
        void main(){
        do
            {int a;}
            a = 0;
            a = a + 1;
        while a != 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType())]),BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("!=",Id("a"),IntLiteral(0)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 326))

    def test_dowhile_and_block_8(self):
        ip = """
        void main(){
            int i[5];
            boolean check;
            do{
                int count;
                count = 0;
                if(count != 0)
                    break;
                count = count*count;
                {}
            } while count == 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  VarDecl('i', ArrayType(5, IntType())),
                                  VarDecl('check', BoolType()),
                                  Dowhile([Block([
                                      VarDecl('count', IntType()),
                                      BinaryOp('=', Id('count'), IntLiteral(0)),
                                      If(BinaryOp('!=', Id('count'), IntLiteral(0)),
                                         Break()
                                         ),
                                      BinaryOp('=', Id('count'), BinaryOp('*', Id('count'), Id('count'))),
                                      Block([

                                      ])
                                  ])],
                                      BinaryOp('==', Id('count'), IntLiteral(0))
                                  )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 327))

    def test_for_and_block_1(self):
        ip = """
        int main(){
            for (i = 0; i < alpha; i = i + 1){}
            return 0;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('alpha')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([

                                      ])
                                      ),
                                  Return(IntLiteral(0))
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 328))

    def test_for_and_block_2(self):
        ip = """
        int main(){
            for (i = 0; i < alpha; i = i + 1){}
            for (i; j; k) {}
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('alpha')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([

                                      ])
                                      ),
                                  For(Id('i'),
                                      Id('j'),
                                      Id('k'),
                                      Block([

                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 329))

    def test_for_and_block_3(self):
        ip = """
        int main(){
            for (i = 1; j = 1; k = 1){
                i = i + 2;
                if ( i > j )
                    print(i);
                else
                    print(j);
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              IntType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(1)),
                                      BinaryOp('=', Id('j'), IntLiteral(1)),
                                      BinaryOp('=', Id('k'), IntLiteral(1)),
                                      Block([
                                          BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(2))),
                                          If(BinaryOp('>', Id('i'), Id('j')),
                                             CallExpr(Id('print'), [Id('i')]),
                                             CallExpr(Id('print'), [Id('j')])
                                             )
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 330))

    def test_for_and_block_4(self):
        ip = """
        void main(){
            for(i = 0; i < MATRIX; i = i + 1)
            {
                    matA[i] = -rand % 2;
            }
            return;
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                      BinaryOp('<', Id('i'), Id('MATRIX')),
                                      BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                      Block([
                                          BinaryOp('=', ArrayCell(Id('matA'), Id('i')),
                                                   BinaryOp('%', UnaryOp('-', Id('rand')), IntLiteral(2)))
                                      ])
                                      ),
                                  Return()
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 331))

    def test_for_and_block_5(self):
        ip = """
        void main(){
            for(changeA = 0; changeA < MATRIX/n_pros; changeA = changeA + 1)
            {
                for(i = 0; i < MATRIX; i = i + 1)
                {
                    matA[i] = rand % 2;
                }
            }
        }
        """
        expect = str(
            Program([FuncDecl(Id('main'),
                              [],
                              VoidType(),
                              Block([
                                  For(BinaryOp('=', Id('changeA'), IntLiteral(0)),
                                      BinaryOp('<', Id('changeA'), BinaryOp('/', Id('MATRIX'), Id('n_pros'))),
                                      BinaryOp('=', Id('changeA'), BinaryOp('+', Id('changeA'), IntLiteral(1))),
                                      Block([
                                          For(BinaryOp('=', Id('i'), IntLiteral(0)),
                                              BinaryOp('<', Id('i'), Id('MATRIX')),
                                              BinaryOp('=', Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                              Block([
                                                  BinaryOp('=', ArrayCell(Id('matA'), Id('i')),
                                                           BinaryOp('%', Id('rand'), IntLiteral(2)))
                                              ])
                                              )
                                      ])
                                      )
                              ]))
                     ])
        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 332))

    def test_for_and_block_5(self):
        ip = """

        """
        expect = str(

        )
        self.assertTrue(TestAST.checkASTGen(ip, expect, 333))
