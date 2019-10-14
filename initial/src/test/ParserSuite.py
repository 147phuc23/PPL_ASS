import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_declaration_1(self):
        #test-case 0
        input = """
        int main() { }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))

#     def test_declaration_2(self):
#         #test-case 1
#         input = """
#         int a[12];
#         int main() {
#             string x[2],y;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,201))

#     def test_declaration_3(self):
#         #test-case 2
#         #Err: cannot name ID keywords
#         input = """
#         int a[12];
#         string int[2];
#         int main() {
#             string x[2],y;
#         }
#         """
#         expect = "Error on line 3 col 15: int"
#         self.assertTrue(TestParser.checkParser(input,expect,202))

#     def test_declaration_4(self):
#         #test-case 3
#         #Err: cannot use void type for vardecl
#         input = """
#         int a[12];
#         void x;
#         int main() {
#             string x[2],y;
#         }
#         """
#         expect = "Error on line 3 col 14: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,203))
    
#     def test_declaration_5(self):
#         #test-case 4
#         #Err: missing variable
#         input = """
#         int a;
#         string b;
#         float c[12];
#         int;
#         """
#         expect = "Error on line 5 col 11: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

#     def test_declaration_6(self):
#         #test-case 5
#         #Err: cannot define func in blockstatement
#         input = """
#         void main(int argc, int argv)
#         {
#             int x(a) {
#                 print(F);
#             };
#         }
#         """
#         expect = "Error on line 4 col 17: ("
#         self.assertTrue(TestParser.checkParser(input,expect,205))

#     def test_declaration_7(self):
#         #test-case 6
#         input = """
#         int x;
#         void main(int argc, int argv)
#         {
#             float c[12];
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,206))

#     def test_declaration_8(self):
#         #test-case 7
#         input = """
#         string str[12];
#         int long, bool, __int32__;
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,207))
    
#     def test_declaration_9(self):
#         #test-case 8
#         #Error: missing ';'
#         input = """
#         void main() {
#             int x;
#             float a[12]
#         }
#         """
#         expect = "Error on line 5 col 8: }"
#         self.assertTrue(TestParser.checkParser(input,expect,208))

#     def test_declaration_10(self):
#         #test-case 9
#         input = """
#         void main() {
#             int x;
#             float a[   12 ];
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,209))

#     def test_declaration_11(self):
#         #test-case 10
#         #Error: 
#         input = """
#         void main() {
#             int math [12];
#             string _google;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,210))

#     def test_declaration_12(self):
#         #test-case 11
#         input = """
#         boolean isPrime(int a, int x[]){}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,211))

#     def test_declaration_13(self):
#         #test-case 12
#         input = """
#         boolean[] isPrime(int a, int[] x){}
#         """
#         expect = "Error on line 2 col 36: ["
#         self.assertTrue(TestParser.checkParser(input,expect,212))
    
#     def test_declaration_14(self):
#         #test-case 13
#         #Error: cant assign int in array declaration
#         input = """
#         boolean[] isPrime(int a, int x[5  ]){}
#         """
#         expect = "Error on line 2 col 39: 5"
#         self.assertTrue(TestParser.checkParser(input,expect,213))

#     def test_declaration_15(self):
#         #test-case 14
#         #Error: cant assign variable in array declaration
#         input = """
#         boolean[] isPrime(int               a, int x)
#         void main(){
#             int a[  21], int b[a ];
#         }
#         """
#         expect = "Error on line 3 col 8: void"
#         self.assertTrue(TestParser.checkParser(input,expect,214))

#     def test_declaration_16(self):
#         #test-case 15
#         #Error: cant assign variable in array declaration
#         input = """
#         boolean[2] isPrime(void x)
#         void main(){
#             int a[21], int b[4];
#         }
#         """
#         expect = "Error on line 2 col 16: 2"
#         self.assertTrue(TestParser.checkParser(input,expect,215))

#     def test_ifstmt_1(self):
#         #test-case 16
#         #Error: missing '(' ')'
#         input = """
#         void main(){
#             if a b;
#         }
#         """
#         expect = "Error on line 3 col 15: a"
#         self.assertTrue(TestParser.checkParser(input,expect,216))

#     def test_ifstmt_2(self):
#         #test-case 17
#         #Error: missing '(' ')'
#         input = """
#         void main(){
#             if (1+1==2) playMusic();
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,217))

#     def test_ifstmt_3(self):
#         #test-case 18
#         #misisng
#         input = """
#         void main(){
#             if (!isPrime()) 
#             {if (9) print("in if");}
#             else {

#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,218))

#     def test_ifstmt_4(self):
#         #test-case 19
#         #misisng
#         input = """
#         void main(){
#             if (!isPrime()) if (9) print("in if"); else say("hello");
#             else {

#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,219))

#     def test_ifstmt_5(self):
#         #test-case 20
#         #misisng if-else
#         input = """
#         void main(){
#             if (!isPrime(x)) if (1!=0) print("in if"); else say("hello");
#             else {

#             }
#             else print("hello world");
#         }
#         """
#         expect = "Error on line 7 col 12: else"
#         self.assertTrue(TestParser.checkParser(input,expect,220))

#     def test_ifstmt_5(self):
#         #test-case 20
#         input = """
#         void main(){
#             if (a==b) if (b==c) print("a=b"); else say("hello");
#             else {

#             }
#             else print("b==c");
#         }
#         """
#         expect = "Error on line 7 col 12: else"
#         self.assertTrue(TestParser.checkParser(input,expect,221))
    
#     def test_ifstmt_6(self):
#         #test-case 21
#         input = """
#         void main(){
#             if (a && b)
#             if( a || b )
#             a || b;
#             else a && b;
#             if (a != b)
#             a == b;
#             else
#         }
#         """
#         expect = "Error on line 10 col 8: }"
#         self.assertTrue(TestParser.checkParser(input,expect,222))

#     def test_ifstmt_7(self):
#         #test-case 23
#         input = """
#         void main(){
#             if (a && b)
#             if( a || b )
#             if( a || b )
#             if (a != b)
#             if( a || b )
#             if( a || b )
#             if( a || b )
#             a == b;
#             else {}
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,223))


#     def test_ifstmt_8(self):
#         #test-case 24
#         input = """
#         void main(){
#             if (str=="gen") gen(str);
#             else {
#                 switch(x, x[2]);
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,224))

#     def test_ifstmt_9(self):
#         #test-case 24
#         input = """
#         if (true) return;
#         void main(){}
#         """
#         expect = "Error on line 2 col 8: if"
#         self.assertTrue(TestParser.checkParser(input,expect,280))

#     def test_ifstmt_10(self):
#         #test-case 25
#         input = """
#         void main(){
#             if (true) {};
#         }
#         """
#         expect = "Error on line 3 col 24: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,225))
    
#     def test_whilestmt_1(self):
#         #test-case 26
#         input = """
#         void main(){
#             do println("%d No \\n", a);
#             while (a!=100);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,226))

#     def test_whilestmt_2(self):
#         #test-case 27
#         input = """
#         void main(){
#             do
#                 println("%d PrintLN ", a);
#                 1+2==3;
#             while (a!=100);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,227))

#     def test_whilestmt_3(self):
#         #test-case 28
#         input = """
#         void main(){
#             do
#                 println("%d No \\n", a);
#                 1+2==3
#             while (a!=100);
#         }
#         """
#         expect = "Error on line 6 col 12: while"
#         self.assertTrue(TestParser.checkParser(input,expect,228))

#     def test_whilestmt_4(self):
#         #test-case 29
#         input = """
#         void main(){
#             do {
#                 println("%d No \\n", a);
#                 1+2==3;
#             }
#             {
#                 if (a==b) cout(a);
#             }
#             while (a!=100);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,229))
    
#     def test_whilestmt_5(self):
#         #test-case 30
#         input = """
#         void main(){
#             do {} {}
#             {
#                 do {}{} while true;
#             }
#             while (a!=100);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,230))

#     def test_whilestmt_6(self):
#         #test-case 31
#         input = """
#         void main(){
#             do {
#                 do {//\n} while ( a < 0);
#                 if ( a && b )
#                 {
#                     if( a || b ){a || b ;}
#                     else
#                     {}
#                 }
#                 else{a && b ;}
#             } {}
#             while a == b ;
#             while a != b ;
#         }
#         """
#         expect = "Error on line 15 col 12: while"
#         self.assertTrue(TestParser.checkParser(input,expect,231))

#     def test_whilestmt_7(self):
#         #test-case 32
#         input = """
#         void main(){
#             do do do do do x; while a == b ; while a; while a; while a; while a;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,232))

#     def test_whilestmt_8(self):
#         #test-case 33
#         input = """
#         void main(){
#             do while a;
#         }
#         """
#         expect = "Error on line 3 col 15: while"
#         self.assertTrue(TestParser.checkParser(input,expect,233))

#     def test_whilestmt_9(self):
#         #test-case 34
#         input = """
#         void main(){
#             if (x==0) {
#                 do 
#                     printf(12);
#                     if (true) {foo();}
#                     {do foo1(); while 1+1s;}
#                 while (x>2);
#             }
#         }
#         """
#         expect = "Error on line 7 col 41: s"
#         self.assertTrue(TestParser.checkParser(input,expect,234))

#     def test_forstmt_1(self):
#         #test-case 35
#         input = """
#         void main(){
#             int i;
#             for(i=0; i<10; i=i+1) foo();
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,235))

#     def test_forstmt_2(self):
#         #test-case 36
#         input = """
#         void main(){
#             int i;
#             for(i=0000; i<10e-9; "   ") foo();
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,236))

#     def test_forstmt_3(self):
#         #test-case 36
#         input = """
#         void main(){
#             int i;
#             for(i=0; i<10; i=i+1) {
#                 int j;
#                 for(j=0; j<10; j=i+1) {
#                     break;
#                     return;
#                 }
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,236))

#     def test_forstmt_4(self):
#         #test-case 37
#         input = """
#         boolean isPrime(int n)
#         { 
#             if (n <= 1) return false; 
#             int i; 
#             for (i = 2; i < n; i = i + 1) 
#                 if (n % i == 0) return false;
#             return true; 
#         }        
#         void printPrime(int n)
#         {
#             int i;
#             for (i = 2; i <= n; i = i + 1) { 
#                 if (isPrime(i)) 
#                     print(i); 
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,237))
        
#     def test_forstmt_5(self):
#         #test-case 38
#         input = """
#         int main(){
#             for (i = 0; i <  r; i = i + 1) 
#                 for (j = 0; j < c; j = j + 1) 
#                     for (m = 0; m <  r; i = i + 1) 
#                         for (n = 0; n < c; j = j + 1) break;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,238))
    
#     def test_stmt_1(self):
#         #test-case 39
#         input = """
#         int main(){
#             ;
#         }
#         """
#         expect = "Error on line 3 col 12: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,239))

#     def test_stmt_2(self):
#         #test-case 40
#         input = """
#         int main(){
#             for (x;x;x) {
#                 {{{{{a;}}}}}
#             }
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,240))

#     def test_stmt_3(self):
#         #test-case 41
#         input = """
#         int main(){
#             if (a>b>c) for (i==0;;) print("12'");
#         }  
#         """
#         expect = "Error on line 3 col 19: >"
#         self.assertTrue(TestParser.checkParser(input,expect,241))

#     def test_stmt_4(self):
#         #test-case 42
#         input = """
#         int main(){
#             if (a+3=2) for (i==0;;) print("12'");
#         }  
#         """
#         expect = "Error on line 3 col 33: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,242))

#     def test_stmt_5(self):
#         #test-case 43
#         input = """
#         int main(){
#             string a;
#             a = "sas"; 
#             do {
#                 this.foo();                
#             } 
#             if (1==2) return;
#         }  
#         """
#         expect = "."
#         self.assertTrue(TestParser.checkParser(input,expect,243))

#     def test_stmt_6(self):
#         #test-case 44
#         input = """
#         void main(){
#             foo(a[4],"this is sring", 12);
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,244))

#     def test_stmt_7(self):
#         #test-case 45
#         input = """
#         void main(float argc, int argv ){
#             do {break} while 1+1;
#         }  
#         """
#         expect = "Error on line 3 col 21: }"
#         self.assertTrue(TestParser.checkParser(input,expect,245))

#     def test_stmt_8(self):
#         #test-case 46
#         input = """
#         void main(float argc, int argv ){
#             main(1+1)=2;
#             if (true) {
#                 for (i=0;foo[12];x+1) do 12; while a;
#                 return false;
#             }
#             else return true;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,246))

#     def test_stmt_9(self):
#         #test-case 47
#         input = """
#         void main(float argc, int argv ){
#             int x[12], _[2];
#             _[2](2);
#             return;
#         }  
#         """
#         expect = "Error on line 4 col 16: ("
#         self.assertTrue(TestParser.checkParser(input,expect,247))

#     def test_stmt_10(self):
#         #test-case 48
#         input = """
#         void main(int argc, int argv ){
#             int x[12], _[2];
#             return;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,248))

#     def test_stmt_11(self):
#         #test-case 49
#         input = """
#         void main(int argc, int argv ){
#             int x[12], _[2];
#             for (int1 = 0; 8+; "12"+3) {
#                 {
#                     if (1+1==2) do play(); while (true);
#                     _02(a);
#                 }
#             }
#         }  
#         """
#         expect = "Error on line 4 col 29: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,249))

#     def test_stmt_12(self):
#         #test-case 50
#         input = """
#         void main(int argc, int argv ){
#             int for;
#             do {{for(gg = 9; 1; 90+9) return false;}}
#             while 000;
#         }  
#         """
#         expect = "Error on line 3 col 16: for"
#         self.assertTrue(TestParser.checkParser(input,expect,250))

#     def test_expr_1(self):
#         #test-case 51
#         input = """
#         void main(string argc, int argv ){
#             int a;
#             a = a + b + c + d;
#             a = a - b - c - d;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,251))

#     def test_expr_2(self):
#         #test-case 52
#         input = """
#         void main(int argc, int argv ){
#             int x[12], _[2];
#             a[12] > b > c;
#         }  
#         """
#         expect = "Error on line 4 col 22: >"
#         self.assertTrue(TestParser.checkParser(input,expect,252))

#     def test_expr_3(self):
#         #test-case 53
#         input = """
#         void toString(int x) {
#             parseString(x);
#         }
#         void main(void argc, int argv ){
#             return (1+a)[(((12)))];
#         }  
#         """
#         expect = "Error on line 5 col 18: void"
#         self.assertTrue(TestParser.checkParser(input,expect,253))

#     def test_expr_4(self):
#         #test-case 54
#         input = """
#         void main(){
#             3 + "s123" != 26 != 8;
#         }  
#         """
#         expect = "Error on line 3 col 29: !="
#         self.assertTrue(TestParser.checkParser(input,expect,254))

#     def test_expr_5(self):
#         #test-case 55
#         input = """
#         void main(){
#             3 + "s123" == 26 != 8;
#         }  
#         """
#         expect = "Error on line 3 col 29: !="
#         self.assertTrue(TestParser.checkParser(input,expect,255))
    
#     def test_expr_6(self):
#         #test-case 56
#         input = """
#         void main(){
#             int cout;
#             cout = (a+foo(a[2])[17]) + 8;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,256))

#     def test_expr_7(self):
#         #test-case 57
#         input = """
#         void main(){
#             int cout;
#             cout = (a+foo(a[2])[17])[a(x(12))] * (8 +46);
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,257))
    
#     def test_expr_8(self):
#         #test-case 58
#         input = """
#         void main(){
#             int cout;
#             cout = (1+1)*2 + "78";
#             in/3 == 1>2 && c;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,258))

#     def test_expr_9(self):
#         #test-case 59
#         input = """
#         void main(){
#             _yellow = purple + 9 = 12 = !this;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,259))

#     def test_expr_10(self):
#         #test-case 60
#         input = """
#         void main(){
#             _yellow = purple + 9 = 12 = !(this(102));
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,260))

#     def test_expr_11(self):
#         #test-case 61
#         input = """
#         void main(){
#             !(3>2[12*(a)]);
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,261))

#     def test_expr_12(self):
#         #test-case 62
#         input = """
#         void main(){
#             arr[arr[5]]; //pass
#             arr1[arr2[arr3[5]]]; //pass
#             arr[arr[[5]]; 
#         }  
#         """
#         expect = "Error on line 5 col 20: ["
#         self.assertTrue(TestParser.checkParser(input,expect,262))

#     def test_expr_13(self):
#         #test-case 63
#         input = """
#         void main(){
#             ---x = 12 + ------3;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,263))
    
#     def test_expr_14(self):
#         #test-case 64
#         input = """
#         void main(){
#             int init;
#             init + 9.092e9 = 12/6*8 > 0;
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,264))
    
#     def test_expr_15(self):
#         #test-case 65
#         input = """
#         void main(){
#             boolean x;
#             x = true;
#             x("12", 78)
#         }  
#         """
#         expect = "Error on line 6 col 8: }"
#         self.assertTrue(TestParser.checkParser(input,expect,265))   
    

#     def test_expr_16(self):
#         #test-case 66
#         input = """
#         void main(){
#             boolean x[12];
#             x = !!!!!-12 + 23;     
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,266))

#     def test_expr_17(self):
#         #test-case 67
#         input = """
#         void main(){
#             for (i = -10; i+9; true) {
#                 if (!(14+a)) x == 0;
#                 return false;
#             }
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,267))

#     def test_expr_18(self):
#         #test-case 68
#         input = """
#         void main(){
#             for (i = -10; i+9; true) {
#                 if (!(14+a)) == 0;
#             }
#         }  
#         """
#         expect = "Error on line 4 col 29: =="
#         self.assertTrue(TestParser.checkParser(input,expect,268))

#     def test_expr_19(self):
#         #test-case 69
#         input = """
#         boolean ai(int a[], int c) {
#             _init_();
#             MPI_ID(COM_WORLD);
#             foo ((((10 +     !!20 = 18)))) ;
#         }
          
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,269))
    
#     def test_expr_20(self):
#         #test-case 70
#         input = """
#         void main() {
#             func(());
#         }
#         """
#         expect = "Error on line 3 col 18: )"
#         self.assertTrue(TestParser.checkParser(input,expect,270))

#     def test_expr_21(self):
#         #test-case 71
#         input = """
#         void main() {
#             func((((a))));
#             foo(!());
#         }
#         """
#         expect = "Error on line 4 col 18: )"
#         self.assertTrue(TestParser.checkParser(input,expect,271))

#     def test_expr_22(self):
#         #test-case 72
#         input = """
#         void main() {
#             parse(a[12]) + 102;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,272))

#     def test_expr_23(self):
#         #test-case 73
#         input = """
#         int main(){
#             func(arr[num], arr[num + 1], arr[num + 2]);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,273))

#     def test_expr_24(self):
#         #test-case 74
#         input = """
#         int main(){
#             x = ((!(a > 6) > 9) >= 9) + 9;            
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,274))

#     def test_expr_25(self):
#         #test-case 75
#         input = """
#         int main(){
#             string a;
#             a = (b==c) != d; 
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,275))

#     def test_expr_26(self):
#         # test case 76
#         ip = """
#         int main(){
#             a = ++b;
#         }
#         """
#         expect = "Error on line 3 col 16: +"
#         self.assertTrue(TestParser.checkParser(ip, expect, 276))
    
#     def test_expr_27(self):
#         # test case 77
#         ip = """
#         int main(){
#             a = !(((--3 - 4) --5) -- 6 - 7 - 8);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(ip, expect, 277))
    
#     def test_expr_28(self):
#         #test-case 78
#         input = """
#         void main(){
#             boolean x[12;
#             if (a==b>c) print("1+2"=2);
#             do {} while (_67[a[12]]);
#         }  
#         """
#         expect = "Error on line 3 col 24: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,278))

#     def test_expr_29(self):
#         #test-case 79
#         input = """
#         void main(){
#             boolean x[12];
#             if (a==b>c) print("1+2"=2);
#             do {} while (_67[a[12]]);
#         }  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,279))

#     def test_combine_1(self):
#         #test-case 81
#         input = """
#         void main(){
#             foo(x,y,z);
#         }  
#         int[] foo(float x, float y, float z) {
#             float list[3];
#             list = x + y + z + 0.e12;
#             return list;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,281))

#     def test_combine_2(self):
#         #test-case 82
#         input = """
#         void main(){
#             int total;
#             total = !(foo(y,x,z)) + foo(x,y,z);
#         }  
#         int[] foo(float x, float y, float z) {
#             float list[3];
#             list = x + y + z + 0.e12;
#             return list;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,282))

#     def test_combine_3(self):
#         #test-case 83
#         input = """
#         void x() 
        
#         {{
#             do (print("12")); if (2+2==3) do x; while i; while true;
#         }}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,283))

#     def test_combine_4(self):
#         #test-case 84
#         input = """
#         void main(){
#             boolean x;
#             x = false;
#             if (isEq1(a)) x = true;
#         }  
#         boolean isEq1(int a) {
#             if (a==1) return true;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,284))

#     def test_combine_5(self):
#         #test-case 85
#         input = """
#         void main(){
#             for (x = 8; x>9 && y >12; x=x+1) {
#                 y = y+1;
#                 printf("%d");
#                 //comment
#                 /* new comment \n \r 
#                     for (int i=0;i<12;i++) if if if
#                 */
#             }
#             return;
#         }

#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,285))

#     def test_combine_6(self):
#         #test-case 86
#         input = """
#         void main(){
#             for (x = 8; x>9 && y >12; x=x+1) {
#                 y = ((y+1)>2)>3;
#             }
#             return;
#         }  

#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,286))

#     def test_combine_7(self):
#         #test-case 87
#         input = """
#         int main(a[],12){
#             for (int a, int b, int c) {
#                 if (break) return false;
#             }
#             return;
#         }  

#         """
#         expect = "Error on line 2 col 17: a"
#         self.assertTrue(TestParser.checkParser(input,expect,287))

#     def test_combine_8(self):
#         #test-case 88
#         input = """
#         int main(a[],12){
#             int x;
#             x = ((((((x)>3)))));
#         }  
#         """
#         expect = "Error on line 2 col 17: a"
#         self.assertTrue(TestParser.checkParser(input,expect,288))
    
#     def test_combine_9(self):
#         #test-case 89
#         input = """
#         int main(int a[],string b){
#             for (int_+a, b>2, c=(c+3)) {
#                 if (break;) return false;
#             }
#             return;
#         }  

#         """
#         expect = "Error on line 3 col 23: ,"
#         self.assertTrue(TestParser.checkParser(input,expect,289))

#     def test_combine_10(self):
#         #test-case 90
#         input = """
#         int main(int a[],string b){
#             for (int_+a; b>2; c=(c+3)) {
#                 if (break) return false;
#             }
#             return;
#         }  

#         """
#         expect = "Error on line 4 col 20: break"
#         self.assertTrue(TestParser.checkParser(input,expect,290))

#     def test_combine_11(self):
#         #test-case 91
#         input = """
#         int[] foo(int a) {
#             if (a&&b&&c) do printf("a==b==c"); while x=x+1;
#         }

#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,291))

#     def test_combine_12(self):
#         #test-case 92
#         input = """
#         int[] foo(int a) {
#             if (a||b&&c) do printf(a==b+!1); while x=x+1;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,292))

#     def test_combine_13(self):
#         #test-case 93
#         input = """
#         void enter()
#         {
#         }

#         void init()
#         {
#             {}
#         }

#         void print()
#         {
#         }

#         int main()
#         {
#             enter();
#             init();
#             print();
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,293))
    
#     def test_combine_14(self):
#         #test-case 94
#         input = """
#         /*void enter()
#         {
#         }

#         void init()
#         {
#             {}
#         }

#         void print()
#         {
#         }
#         */
#         int main()
#         {
#             enter()
#             init();
#             print();
#         }
#         """
#         expect = "Error on line 18 col 12: init"
#         self.assertTrue(TestParser.checkParser(input,expect,294))

#     def test_combine_15(self):
#         #test-case 95
#         input = """
#         int a  () {
#             foo(foo_89("stringlit")[12]);
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,295))

#     def test_combine_16(self):
#         #test-case 96
#         input = """
#         int a  () {
#             if if x(); else true;
#         }
#         """
#         expect = "Error on line 3 col 15: if"
#         self.assertTrue(TestParser.checkParser(input,expect,296))

#     def test_combine_17(self):
#         #test-case 97
#         input = """
#         int a  () {
#             do print (1+         23, " \\n \\b"); {//first comment } { }
#             } {{}} ;
#             while true;
#         }
#         """
#         expect = "Error on line 4 col 19: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,297))

#     def test_combine_18(self):
#         #test-case 98
#         input = """
#         int main() {
#                 a = b + c;
#                 for (a; b; c) {
#                     printf("this is a typical string \\n");
#                 }
#                 do return; while 1;
#             } 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,298))
    
#     def test_combine_19(self):
#         input = """
#             int main() {
#                 a = b + c;
#                 for (a; b; c) {
#                     printf("this is not a typical string 
#                     ");
#                     /*  [[[[[[[[[[[]]]]]]]]]]]]*/
#                 }
#                 do return; while 1;
#             } 
#         """
#         expect = "this is not a typical string "
#         self.assertTrue(TestParser.checkParser(input,expect,299))
    