import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

#     def test_id_1(self):
#         # test case 1
#         self.assertTrue(TestLexer.checkLexeme(" id id1 id2 ", "id,id1,id2,<EOF>", 101))

#     def test_id_2(self):
#         # test case 2
#         self.assertTrue(TestLexer.checkLexeme(""" name name_ """, "name,name_,<EOF>", 102))
    
#     def test_id_3(self):
#         # test case 3
#         self.assertTrue(TestLexer.checkLexeme(""" 123name """, "123,name,<EOF>", 103))

#     def test_id_4(self):
#         # test case 4
#         self.assertTrue(TestLexer.checkLexeme(""" 123.e1name_ """, "123.e1,name_,<EOF>", 104))
    
#     def test_id_5(self):
#         # test case 5
#         self.assertTrue(TestLexer.checkLexeme(""" intabc int """, "intabc,int,<EOF>", 105))
    
#     def test_id_6(self):
#         # test case 6
#         self.assertTrue(TestLexer.checkLexeme(""" 1int1 """, "1,int1,<EOF>", 106))
    
#     def test_id_7(self):
#         # test case 7
#         self.assertTrue(TestLexer.checkLexeme(""" __int__ """, "__int__,<EOF>", 107))
    
#     def test_id_8(self):
#         # test case 8
#         self.assertTrue(TestLexer.checkLexeme(""" SAJDHAJSHD___123_1233NDJKFN """, "SAJDHAJSHD___123_1233NDJKFN,<EOF>", 108))
    
#     def test_id_9(self):
#         # test case 9
#         self.assertTrue(TestLexer.checkLexeme(""" _____A7688ASDHJAS """, "_____A7688ASDHJAS,<EOF>", 109))

#     def test_id_10(self):
#         # test case 10
#         self.assertTrue(TestLexer.checkLexeme(""" FOO() """, "FOO,(,),<EOF>", 110))

#     def test_keyword_1(self):
#         # test case 11
#         self.assertTrue(TestLexer.checkLexeme(""" void boolean int string float  """, "void,boolean,int,string,float,<EOF>", 111))
    
#     def test_keyword_2(self):
#         # test case 12
#         self.assertTrue(TestLexer.checkLexeme(""" while do if else for  """, "while,do,if,else,for,<EOF>", 112))

#     def test_keyword_3(self):
#         # test case 13
#         self.assertTrue(TestLexer.checkLexeme(""" void int string float while do else if return break returnbreak""", "void,int,string,float,while,do,else,if,return,break,returnbreak,<EOF>", 113)) 
    
#     def test_keyword_4(self):
#         # test case 14
#         self.assertTrue(TestLexer.checkLexeme(""" return break 123break """, "return,break,123,break,<EOF>", 114)) 
    
#     def test_keyword_5(self):
#         # test case 15
#         self.assertTrue(TestLexer.checkLexeme(""" return break 123break """, "return,break,123,break,<EOF>", 115)) 
    
#     def test_char_1(self):
#         # test case 16
#         self.assertTrue(TestLexer.checkLexeme(""" () {} 
#         () ; , ; , [[[]]]
#         """, 
#         """(,),{,},(,),;,,,;,,,[,[,[,],],],<EOF>""", 116)) 
    
#     def test_char_2(self):
#         # test case 17
#         self.assertTrue(TestLexer.checkLexeme(""" 123()3,4e5,6.8 """, 
#         "123,(,),3,,,4e5,,,6.8,<EOF>", 117)) 
    
#     def test_operator_1(self):
#         # test case 18
#         self.assertTrue(TestLexer.checkLexeme(""" =+ -* / %""", 
#         "=,+,-,*,/,%,<EOF>", 118)) 
    
#     def test_operator_2(self):
#         # test case 19
#         self.assertTrue(TestLexer.checkLexeme(""" =+-*/% """, 
#         "=,+,-,*,/,%,<EOF>", 119)) 
    
#     def test_operator_3(self):
#         # test case 20
#         self.assertTrue(TestLexer.checkLexeme(""" =====!==""", 
#         "==,==,=,!=,=,<EOF>", 120)) 
    
#     def test_operator_4(self):
#         # test case 21
#         self.assertTrue(TestLexer.checkLexeme(""" > < >= <= !! == && || """, ">,<,>=,<=,!,!,==,&&,||,<EOF>", 121)) 
    
#     def test_operator_5(self):
#         # test case 22
#         self.assertTrue(TestLexer.checkLexeme("""<><>>=><<==!==||&&&&""", "<,>,<,>,>=,>,<,<=,=,!=,=,||,&&,&&,<EOF>", 122)) 
    
#     def test_operator_6(self):
#         # test case 23
#         self.assertTrue(TestLexer.checkLexeme("""= == ==== = ===""", "=,==,==,==,=,==,=,<EOF>", 123)) 
    
#     def test_intlit_1(self):
#         # test case 24
#         self.assertTrue(TestLexer.checkLexeme("""123 0 3423""", "123,0,3423,<EOF>", 124)) 
    
#     def test_intlit_2(self):
#         # test case 25
#         self.assertTrue(TestLexer.checkLexeme("""0000 01012 0001212 """, "0000,01012,0001212,<EOF>", 125)) 
    
#     def test_intlit_3(self):
#         # test case 26
#         self.assertTrue(TestLexer.checkLexeme(""" 0 1 2 3 4 5 6 7 """, "0,1,2,3,4,5,6,7,<EOF>", 126)) 
    
#     def test_intlit_4(self):
#         # test case 27
#         self.assertTrue(TestLexer.checkLexeme("""09876545 12 32""", "09876545,12,32,<EOF>", 127)) 
    
#     def test_floatlit_1(self):
#         # test case 28
#         self.assertTrue(TestLexer.checkLexeme("""1.23 2.32 4.56 1e2 2e-34""", "1.23,2.32,4.56,1e2,2e-34,<EOF>", 128)) 
    
#     def test_floatlit_2(self):
#         # test case 29
#         self.assertTrue(TestLexer.checkLexeme("""0.000 .0000 0000 00e00 0.0000e00""", "0.000,.0000,0000,00e00,0.0000e00,<EOF>", 129)) 
    
#     def test_floatlit_3(self):
#         # test case 30
#         self.assertTrue(TestLexer.checkLexeme("""1.1e2.332e2.2e32.3E66 """, "1.1e2,.332e2,.2e32,.3E66,<EOF>", 130)) 
    
#     def test_floatlit_4(self):
#         # test case 31
#         self.assertTrue(TestLexer.checkLexeme("""0 00.0e00.00e00E000.00ee00.0e0 """, "0,00.0e00,.00e00,E000,.00,ee00,.0e0,<EOF>", 131)) 
    
#     def test_floatlit_5(self):
#         # test case 32
#         self.assertTrue(TestLexer.checkLexeme(""" 1e3 11E3 11.3E3 .11333e-3 1e-3 1.1e00""", "1e3,11E3,11.3E3,.11333e-3,1e-3,1.1e00,<EOF>", 132)) 

#     def test_floatlit_6(self):
#         # test case 37
#         self.assertTrue(TestLexer.checkLexeme(""" 1e3 11E3 11.3E3 .11333e-3 1e-3 1.1e00""", "1e3,11E3,11.3E3,.11333e-3,1e-3,1.1e00,<EOF>", 137)) 
    
#     def test_stringlit_1(self):
#         # test case 38
#         self.assertTrue(TestLexer.checkLexeme(""" "abc" "ABC" """, "abc,ABC,<EOF>", 138)) 

#     def test_stringlit_2(self):
#         # test case 39
#         self.assertTrue(TestLexer.checkLexeme(""" "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM      123456789000_" """, "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM      123456789000_,<EOF>", 139)) 

#     def test_stringlit_3(self):
#         # test case 40
#         self.assertTrue(TestLexer.checkLexeme(""" "'" "'''+-*/!@#$%^&*()_+=" """, "','''+-*/!@#$%^&*()_+=,<EOF>", 140)) 

#     def test_stringlit_4(self):
#         # test case 41
#         self.assertTrue(TestLexer.checkLexeme(""" "aaa 123
#         b
#         c" """, "Unclosed String: aaa 123", 141)) 

#     def test_stringlit_5(self): 
#         # test case 42
#         self.assertTrue(TestLexer.checkLexeme(""" "abc\\abc" """, 
#                                               "Illegal Escape In String: abc\\a", 142)) 

#     def test_stringlit_6(self):
#         # test case 43
#         self.assertTrue(TestLexer.checkLexeme(""" "\\n\\b\\t\\r\\\\" """, "\\n\\b\\t\\r\\\\,<EOF>", 143)) 

#     def test_stringlit_7(self):
#         # test case 44
#         self.assertTrue(TestLexer.checkLexeme(""" "int 1+1=3, 2+2=4, thay phung dep trai " \\\\"   """, "int 1+1=3, 2+2=4, thay phung dep trai ,Error Token \\", 144)) 

#     def test_stringlit_8(self):
#         # test case 45
#         self.assertTrue(TestLexer.checkLexeme(""" " " """, " ,<EOF>", 145)) 

#     def test_stringlit_9(self):
#         # test case 46
#         self.assertTrue(TestLexer.checkLexeme(""" "....???....''''''     " """, "....???....''''''     ,<EOF>", 146)) 
    
#     def test_stringlit_10(self):
#         # test case 47
#         self.assertTrue(TestLexer.checkLexeme( """ "\t\t\t" """ , "\t\t\t,<EOF>", 147)) 
    
#     def test_comment_1(self):
#         # test case 48
#         self.assertTrue(TestLexer.checkLexeme( """ a//"\t\t\t" """ , "a,<EOF>", 148)) 

#     def test_comment_2(self):
#         # test case 48
#         self.assertTrue(TestLexer.checkLexeme( """ a//abcaksdjaksdj  *//*xxx*/ //// 123?><!@#$%^&*_+*-/ """ , "a,<EOF>", 148)) 

#     def test_comment_3(self):
#         # test case 49
#         self.assertTrue(TestLexer.checkLexeme( """ int a;//"this is line comment"
#         string b;
#         1+1=2; """ , "int,a,;,string,b,;,1,+,1,=,2,;,<EOF>", 149)) 

#     def test_comment_5(self):
#         # test case 51
#         self.assertTrue(TestLexer.checkLexeme( """ int a; /*
#         {
#             void(x);
#             stirng lit b;
#             1+2=3;
#             for(int i=0;i,i<2;i++) {
#                 printf("helloworld");
#             }

#         }/*/ """ , "int,a,;,<EOF>", 151)) 

#     def test_comment_6(self):
#         # test case 52
#         self.assertTrue(TestLexer.checkLexeme( """
#         ///*abcs
#         */
#         """ , "*,/,<EOF>", 152)) 

#     def test_comment_7(self):
#         # test case 53
#         self.assertTrue(TestLexer.checkLexeme(""" string line_comment;// abc """ , "string,line_comment,;,<EOF>", 153)) 

#     def test_comment_8(self):
#         # test case 54
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         /*xasx
#         //// \\a\\b
#         */
#         "comment " """ ,"comment ,<EOF>", 154)) 

#     def test_1(self):
#         # test case 55
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             int a = 0;
#         } """ ,"void,main,(,),{,int,a,=,0,;,},<EOF>", 155)) 

#     def test_2(self):
#         # test case 56
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             int a = 0;
#             ///this is comment
#             while (x) do y();
#         } """ ,"void,main,(,),{,int,a,=,0,;,while,(,x,),do,y,(,),;,},<EOF>", 156)) 
    
#     def test_3(self):
#         # test case 57
#         self.assertTrue(TestLexer.checkLexeme( """ for (int i==0; i<10; i++) {
#             cout << x;
#         } """ ,"for,(,int,i,==,0,;,i,<,10,;,i,+,+,),{,cout,<,<,x,;,},<EOF>", 157)) 
    
#     def test_4(self):
#         # test case 58
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         if (a==c==b)
#             if (1+1==2) print(1);
#         else return; 
#         """ ,"if,(,a,==,c,==,b,),if,(,1,+,1,==,2,),print,(,1,),;,else,return,;,<EOF>", 158)) 
    
#     def test_5(self):
#         # test case 59
#         self.assertTrue(TestLexer.checkLexeme( """ foo(foo(foo(foo(foo(" , ")))))""" ,"foo,(,foo,(,foo,(,foo,(,foo,(, , ,),),),),),<EOF>", 159)) 
    
#     def test_6(self):
#         # test case 60
#         self.assertTrue(TestLexer.checkLexeme( """ return int a = 0; int inti1;;;
#         """ ,"return,int,a,=,0,;,int,inti1,;,;,;,<EOF>", 160)) 
    
#     def test_7(self):
#         # test case 61
#         self.assertTrue(TestLexer.checkLexeme( """ int a(string b[], string c, int c1) """, 
#                                                 "int,a,(,string,b,[,],,,string,c,,,int,c1,),<EOF>", 161)) 
    
#     def test_8(self):
#         # test case 62
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             int a;
#             int x;
#             a = 1;
#             x = (((((((a)))))));
#         } """ ,"void,main,(,),{,int,a,;,int,x,;,a,=,1,;,x,=,(,(,(,(,(,(,(,a,),),),),),),),;,},<EOF>", 162)) 
    
#     def test_9(self):
#         # test case 63
#         self.assertTrue(TestLexer.checkLexeme( """string int 3i_213 .3.e9""" ,"string,int,3,i_213,.3,Error Token .", 163)) 
    
#     def test_10(self):
#         # test case 64
#         self.assertTrue(TestLexer.checkLexeme( """int[] new(1+2) {


#             string x = "\\a\\b\\c";

#         }""" ,"int,[,],new,(,1,+,2,),{,string,x,=,Illegal Escape In String: \\a", 164)) 
    
#     def test_11(self):
#         # test case 65
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             if (a==3) if (x+1==2) y(); else return 1;
#         } """ ,"void,main,(,),{,if,(,a,==,3,),if,(,x,+,1,==,2,),y,(,),;,else,return,1,;,},<EOF>", 165)) 
    
#     def test_12(self):
#         # test case 66
#         self.assertTrue(TestLexer.checkLexeme( """void main() {
#             if (a) if (b) if (c) x; else y; else z;
#             //check if - else parser
#         } """ ,"void,main,(,),{,if,(,a,),if,(,b,),if,(,c,),x,;,else,y,;,else,z,;,},<EOF>", 166)) 
    
#     def test_13(self):
#         # test case 67
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             do
#             {
#                 1+1=2;
#             }
#             {
#                 return x;
#             }  {}          
#             while (true);

#         } """ ,"void,main,(,),{,do,{,1,+,1,=,2,;,},{,return,x,;,},{,},while,(,true,),;,},<EOF>", 167)) 
    
#     def test_14(self):
#         # test case 68
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             /*
#             nothing in here will be show up
#                 do nothing "i will give up"
#             */
#         } """ ,"void,main,(,),{,},<EOF>", 168)) 
    
#     def test_15(self):
#         # test case 69
#         self.assertTrue(TestLexer.checkLexeme( """
#             #include <stdio.h>
#             #define NUM 20000
#             #include <math.h>
#         """ ,"Error Token #", 169)) 
    
#     def test_16(self):
#         # test case 70
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         int x[12];
#         void main() {
#             int a = b>c>d;
#         } """ ,"int,x,[,12,],;,void,main,(,),{,int,a,=,b,>,c,>,d,;,},<EOF>", 170)) 
    
#     def test_17(self):
#         # test case 71
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             for (0=0;true;1+1) {
#                 print("xxx)
#             }
#         } """ ,"void,main,(,),{,for,(,0,=,0,;,true,;,1,+,1,),{,print,(,Unclosed String: xxx)", 171)) 
    
#     def test_18(self):
#         # test case 72
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             int x;
#             x = foo(1+1)[1*2];
#         } """ ,"void,main,(,),{,int,x,;,x,=,foo,(,1,+,1,),[,1,*,2,],;,},<EOF>", 172)) 
    
#     def test_19(self):
#         # test case 73
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             __int_32 i;
#             i = (i+2)[i+8];
#         } """ ,"void,main,(,),{,__int_32,i,;,i,=,(,i,+,2,),[,i,+,8,],;,},<EOF>", 173)) 
    
#     def test_20(self):
#         # test case 74
#         self.assertTrue(TestLexer.checkLexeme( """ void main(int[] a) {
#             {
#                 {
#                     break;
#                 }
#             }
#         } """ ,"void,main,(,int,[,],a,),{,{,{,break,;,},},},<EOF>", 174)) 
    
#     def test_21(self):
#         # test case 75
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         float f = 1.0; // ERROR
#         float f ; // CORRECT
#         int i[] ; // ERROR
#         int i[5] ; // CORRECT
#         """ ,"float,f,=,1.0,;,float,f,;,int,i,[,],;,int,i,[,5,],;,<EOF>", 175)) 
    
#     def test_22(self):
#         # test case 76
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         string x[2] = {"1+1","4+5"};
#         """ ,"string,x,[,2,],=,{,1+1,,,4+5,},;,<EOF>", 176)) 
    
#     def test_23(self):
#         # test case 77
#         self.assertTrue(TestLexer.checkLexeme( """ void main() {
#             for = int[i][2];
#         } """ ,"void,main,(,),{,for,=,int,[,i,],[,2,],;,},<EOF>", 177)) 
    
#     def test_24(self):
#         # test case 78
#         self.assertTrue(TestLexer.checkLexeme( """
#             //dont show on this \\b \t \t aaa
#             print("hello  ! world");
#         """ ,"print,(,hello  ! world,),;,<EOF>", 178)) 
    
#     def test_25(self):
#         # test case 79
#         self.assertTrue(TestLexer.checkLexeme( """ void ?main() {
#             int a = 0;
#             print("hello  ! world");

#         } """ ,"void,Error Token ?", 179)) 
    
#     def test_26(self):
#         # test case 80
#         self.assertTrue(TestLexer.checkLexeme( """ 
#         void func() {} 
#         void main(int argc, char **argv[]) {}
#         """ ,"void,func,(,),{,},void,main,(,int,argc,,,char,*,*,argv,[,],),{,},<EOF>", 180)) 
    
#     def test_27(self):
#         # test case 81
#         self.assertTrue(TestLexer.checkLexeme( """
#         (int aa, int bx[], float abc[], string d, boolean e){}
#         """ ,"(,int,aa,,,int,bx,[,],,,float,abc,[,],,,string,d,,,boolean,e,),{,},<EOF>", 181)) 

#     def test_28(self):
#         # test case 82
#         self.assertTrue(TestLexer.checkLexeme( """
#             int a = a>b>c + c>d>e;
#         """ ,"int,a,=,a,>,b,>,c,+,c,>,d,>,e,;,<EOF>", 182)) 

#     def test_29(self):
#         # test case 83
#         self.assertTrue(TestLexer.checkLexeme( """
#             float __1x = new float();
#             return 3;
#         """ ,"float,__1x,=,new,float,(,),;,return,3,;,<EOF>", 183)) 
    
#     def test_30(self):
#         # test case 84
#         self.assertTrue(TestLexer.checkLexeme( """
#             x = (3+2) * (a[b[x]] * 8);
#         """ ,"x,=,(,3,+,2,),*,(,a,[,b,[,x,],],*,8,),;,<EOF>", 184)) 

#     def test_31(self):
#         # test case 85
#         self.assertTrue(TestLexer.checkLexeme( """
#             x = (3+2) * (a[b)[x]] * 8);
#         """ ,"x,=,(,3,+,2,),*,(,a,[,b,),[,x,],],*,8,),;,<EOF>", 185)) 

#     def test_32(self):
#         # test case 86
#         self.assertTrue(TestLexer.checkLexeme( """
#             x = (3+2;
#             string s = "new string";
#         """ ,"x,=,(,3,+,2,;,string,s,=,new string,;,<EOF>", 186)) 
    
#     def test_33(self):
#         # test case 87
#         self.assertTrue(TestLexer.checkLexeme( """
#             x = !(-3+2) ------8;
#         """ ,"x,=,!,(,-,3,+,2,),-,-,-,-,-,-,8,;,<EOF>", 187)) 

#     def test_34(self):
#         # test case 88
#         self.assertTrue(TestLexer.checkLexeme( """
#             string x;
#             x = "123 ++ 467 // " + "4i8920 -1829" + i[8,9];
#         """ ,"string,x,;,x,=,123 ++ 467 // ,+,4i8920 -1829,+,i,[,8,,,9,],;,<EOF>", 188)) 

#     def test_35(self):
#         # test case 89
#         self.assertTrue(TestLexer.checkLexeme( """
#         void main() 
#         {
#             {
#                 if (y!=12) return true;
#                 else print("%ld",1+1);
#             }
#             float a = alloc(typeof(int));
#             do 
#             {
#                 print(Aa);
#                 if (!0) return;
#             }
#             {
#                 //first bracket
#                 {
#                     sqrt(14);
#                 }
#                 //second bracket */ /*
#             }
#             while(true);
#         }
#         int[] init(int a) {
#             return 14;
#         }
#         """ ,"void,main,(,),{,{,if,(,y,!=,12,),return,true,;,else,print,(,%ld,,,1,+,1,),;,},float,a,=,alloc,(,typeof,(,int,),),;,do,{,print,(,Aa,),;,if,(,!,0,),return,;,},{,{,sqrt,(,14,),;,},},while,(,true,),;,},int,[,],init,(,int,a,),{,return,14,;,},<EOF>", 189)) 
        
#     def test_36(self):
#         # test case 90
#         self.assertTrue(TestLexer.checkLexeme( """
#         int main(){
#             void x(){
#                 return true;
#             }
#         }
#         """ ,"int,main,(,),{,void,x,(,),{,return,true,;,},},<EOF>", 190)) 

#     def test_37(self):
#         # test case 91
#         self.assertTrue(TestLexer.checkLexeme( """
#         int main(){
#             'return .
#         }
#         """ ,"int,main,(,),{,Error Token '", 191)) 

#     def test_38(self):
#         # test case 92
#         self.assertTrue(TestLexer.checkLexeme( """
#             x = ~!(-3+2) ------8 \\;
#         """ ,"x,=,Error Token ~", 192)) 
    
#     def test_39(self):
#         # test case 93
#         self.assertTrue(TestLexer.checkLexeme( """
#             "abc /* comment */ end-comment" + 3
#         """ ,"abc /* comment */ end-comment,+,3,<EOF>", 193)) 

#     def test_40(self):
#         # test case 94
#         self.assertTrue(TestLexer.checkLexeme( """
#             "abc //comment */ end-comment" + 3
#         """ ,"abc //comment */ end-comment,+,3,<EOF>", 194)) 

#     def test_41(self):
#         # test case 95
#         self.assertTrue(TestLexer.checkLexeme( """
#         void :x(int a) {
#             for(;;) {
#                 int i=0;
#                 if (i!=8) {
#                     i++;
#                     print("day la so thu i);
#                 }
#                 else break;
#             }
#         }
#         """ ,"void,Error Token :", 195)) 
    
#     def test_42(self):
#         # test case 96
#         self.assertTrue(TestLexer.checkLexeme( """
#         void printHelloWorld(int a) {
#             for(;;) {
#                 int i=0;
#                 if (i!=8) {
#                     i++;
#                     print("day la so thu i);
#                 }
#                 else break;
#             }
#         }
#         """ ,"void,printHelloWorld,(,int,a,),{,for,(,;,;,),{,int,i,=,0,;,if,(,i,!=,8,),{,i,+,+,;,print,(,Unclosed String: day la so thu i);", 196))

#     def test_43(self):
#         # test case 97
#         self.assertTrue(TestLexer.checkLexeme( """
#         void printHelloWorld(int a) {} {} {{}}

#         """ ,"void,printHelloWorld,(,int,a,),{,},{,},{,{,},},<EOF>", 197))

#     def test_44(self):
#         # test case 98
#         self.assertTrue(TestLexer.checkLexeme( """
#         string x = "void printHelloWorld(int a) {} {} {{}}";
#         main(int I);

#         """ ,"string,x,=,void printHelloWorld(int a) {} {} {{}},;,main,(,int,I,),;,<EOF>", 198))
    
#     def test_45(self):
#         # test case 99
#         self.assertTrue(TestLexer.checkLexeme( """
#         boolean isPrime(int a){
#             int i;
#             boolean x;
#             for(i=0; i<sqrt(a); i++) if (a%i==0) return false;
#             return true;
#         }
#         void main(){
#             int x;
#             scanf("Input: %d",x);
#             if (isPrime(x)) printf("so nguyen to %d",x);
#             else printf("k phai so nguyen to");
#             return;
#         }
#         """ ,"boolean,isPrime,(,int,a,),{,int,i,;,boolean,x,;,for,(,i,=,0,;,i,<,sqrt,(,a,),;,i,+,+,),if,(,a,%,i,==,0,),return,false,;,return,true,;,},void,main,(,),{,int,x,;,scanf,(,Input: %d,,,x,),;,if,(,isPrime,(,x,),),printf,(,so nguyen to %d,,,x,),;,else,printf,(,k phai so nguyen to,),;,return,;,},<EOF>", 199))

#     def test_46(self):
#         # test case 100
#         self.assertTrue(TestLexer.checkLexeme( """
#             printf("\t \t \t \\a");
#         """ ,"printf,(,Illegal Escape In String: \t \t \t \\a", 100))

#     def test_47(self):
#         # test case 33
#         self.assertTrue(TestLexer.checkLexeme( """
#             int x;
#             x = 1;
#             x = (x*x)/(4*foo(12))%12true2;
#             (((((())))));
#         """ ,"int,x,;,x,=,1,;,x,=,(,x,*,x,),/,(,4,*,foo,(,12,),),%,12,true2,;,(,(,(,(,(,(,),),),),),),;,<EOF>", 133))

#     def test_48(self):
#         # test case 34
#         self.assertTrue(TestLexer.checkLexeme( """
#             1+2.e12 - 5.8600000003e-0000/90.6 + "this is string"
#             //cant catch this comment
#         """ ,"1,+,2.e12,-,5.8600000003e-0000,/,90.6,+,this is string,<EOF>", 134))

#     def test_49(self):
#         # test case 35
#         self.assertTrue(TestLexer.checkLexeme( """
#             _"foreverQuote"__(this is real comment) /* \a \b \c \t \n \f \r 
#             */
#             int a;
#         """ ,"_,foreverQuote,__,(,this,is,real,comment,),int,a,;,<EOF>", 135))

#     def test_50(self):
#         # test case 36
#         self.assertTrue(TestLexer.checkLexeme( """/*
#         #include <math.h>
#         #include <x>
#         [(])
#         #define [ )
#         */
#         // this is comment
#         "abc\\""" ,"Illegal Escape In String: abc\\", 136))

      
