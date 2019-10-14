# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0136\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\6\2H\n\2\r\2")
        buf.write("\16\2I\3\2\3\2\3\3\3\3\5\3P\n\3\3\4\3\4\3\4\5\4U\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\7\tf\n\t\f\t\16\ti\13\t\3\n\3\n\3\n\3\n\5\no\n\n")
        buf.write("\3\13\3\13\3\13\3\13\5\13u\n\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\7\r\177\n\r\f\r\16\r\u0082\13\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u008c\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0096\n\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u009f\n\20\3\21\3")
        buf.write("\21\7\21\u00a3\n\21\f\21\16\21\u00a6\13\21\3\21\3\21\3")
        buf.write("\22\3\22\5\22\u00ac\n\22\3\23\3\23\6\23\u00b0\n\23\r\23")
        buf.write("\16\23\u00b1\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\5\27\u00ca\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\5\31\u00d6\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u00de\n\32\f\32\16\32\u00e1")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u00e9\n\33\f")
        buf.write("\33\16\33\u00ec\13\33\3\34\3\34\3\34\3\34\3\34\5\34\u00f3")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u00fa\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u0102\n\36\f\36\16\36\u0105")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u010d\n\37\f")
        buf.write("\37\16\37\u0110\13\37\3 \3 \3 \5 \u0115\n \3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u011d\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0126")
        buf.write("\n\"\3#\3#\3#\3#\3#\7#\u012d\n#\f#\16#\u0130\13#\5#\u0132")
        buf.write("\n#\3#\3#\3#\2\6\62\64:<$\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\t\3\2\4\7\3\2")
        buf.write("\20\23\3\2\'(\3\2),\3\2\37 \3\2!#\4\2  $$\2\u0136\2G\3")
        buf.write("\2\2\2\4O\3\2\2\2\6T\3\2\2\2\bV\3\2\2\2\nZ\3\2\2\2\f\\")
        buf.write("\3\2\2\2\16^\3\2\2\2\20b\3\2\2\2\22j\3\2\2\2\24p\3\2\2")
        buf.write("\2\26y\3\2\2\2\30{\3\2\2\2\32\u008b\3\2\2\2\34\u0095\3")
        buf.write("\2\2\2\36\u0097\3\2\2\2 \u00a0\3\2\2\2\"\u00ab\3\2\2\2")
        buf.write("$\u00ad\3\2\2\2&\u00b7\3\2\2\2(\u00c1\3\2\2\2*\u00c4\3")
        buf.write("\2\2\2,\u00c7\3\2\2\2.\u00cd\3\2\2\2\60\u00d5\3\2\2\2")
        buf.write("\62\u00d7\3\2\2\2\64\u00e2\3\2\2\2\66\u00f2\3\2\2\28\u00f9")
        buf.write("\3\2\2\2:\u00fb\3\2\2\2<\u0106\3\2\2\2>\u0114\3\2\2\2")
        buf.write("@\u011c\3\2\2\2B\u0125\3\2\2\2D\u0127\3\2\2\2FH\5\4\3")
        buf.write("\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2K")
        buf.write("L\7\2\2\3L\3\3\2\2\2MP\5\16\b\2NP\5\24\13\2OM\3\2\2\2")
        buf.write("ON\3\2\2\2P\5\3\2\2\2QU\5\n\6\2RU\7\3\2\2SU\5\b\5\2TQ")
        buf.write("\3\2\2\2TR\3\2\2\2TS\3\2\2\2U\7\3\2\2\2VW\5\n\6\2WX\7")
        buf.write("\32\2\2XY\7\33\2\2Y\t\3\2\2\2Z[\t\2\2\2[\13\3\2\2\2\\")
        buf.write("]\t\3\2\2]\r\3\2\2\2^_\5\n\6\2_`\5\20\t\2`a\7\34\2\2a")
        buf.write("\17\3\2\2\2bg\5\22\n\2cd\7\35\2\2df\5\22\n\2ec\3\2\2\2")
        buf.write("fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\21\3\2\2\2ig\3\2\2\2j")
        buf.write("n\7-\2\2kl\7\32\2\2lm\7\20\2\2mo\7\33\2\2nk\3\2\2\2no")
        buf.write("\3\2\2\2o\23\3\2\2\2pq\5\6\4\2qr\5\26\f\2rt\7\26\2\2s")
        buf.write("u\5\30\r\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\27\2\2wx")
        buf.write("\5 \21\2x\25\3\2\2\2yz\7-\2\2z\27\3\2\2\2{\u0080\5\32")
        buf.write("\16\2|}\7\35\2\2}\177\5\32\16\2~|\3\2\2\2\177\u0082\3")
        buf.write("\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\31\3\2")
        buf.write("\2\2\u0082\u0080\3\2\2\2\u0083\u0084\5\n\6\2\u0084\u0085")
        buf.write("\7-\2\2\u0085\u008c\3\2\2\2\u0086\u0087\5\n\6\2\u0087")
        buf.write("\u0088\7-\2\2\u0088\u0089\7\32\2\2\u0089\u008a\7\33\2")
        buf.write("\2\u008a\u008c\3\2\2\2\u008b\u0083\3\2\2\2\u008b\u0086")
        buf.write("\3\2\2\2\u008c\33\3\2\2\2\u008d\u0096\5\36\20\2\u008e")
        buf.write("\u0096\5.\30\2\u008f\u0096\5$\23\2\u0090\u0096\5&\24\2")
        buf.write("\u0091\u0096\5,\27\2\u0092\u0096\5*\26\2\u0093\u0096\5")
        buf.write("(\25\2\u0094\u0096\5 \21\2\u0095\u008d\3\2\2\2\u0095\u008e")
        buf.write("\3\2\2\2\u0095\u008f\3\2\2\2\u0095\u0090\3\2\2\2\u0095")
        buf.write("\u0091\3\2\2\2\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0094\3\2\2\2\u0096\35\3\2\2\2\u0097\u0098\7\b")
        buf.write("\2\2\u0098\u0099\7\26\2\2\u0099\u009a\5\60\31\2\u009a")
        buf.write("\u009b\7\27\2\2\u009b\u009e\5\34\17\2\u009c\u009d\7\t")
        buf.write("\2\2\u009d\u009f\5\34\17\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\37\3\2\2\2\u00a0\u00a4\7\30\2\2\u00a1\u00a3")
        buf.write("\5\"\22\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a7\u00a8\7\31\2\2\u00a8!\3\2\2")
        buf.write("\2\u00a9\u00ac\5\34\17\2\u00aa\u00ac\5\16\b\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac#\3\2\2\2\u00ad\u00af")
        buf.write("\7\13\2\2\u00ae\u00b0\5\34\17\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7\n\2\2\u00b4\u00b5\5")
        buf.write("\60\31\2\u00b5\u00b6\7\34\2\2\u00b6%\3\2\2\2\u00b7\u00b8")
        buf.write("\7\16\2\2\u00b8\u00b9\7\26\2\2\u00b9\u00ba\5\60\31\2\u00ba")
        buf.write("\u00bb\7\34\2\2\u00bb\u00bc\5\60\31\2\u00bc\u00bd\7\34")
        buf.write("\2\2\u00bd\u00be\5\60\31\2\u00be\u00bf\7\27\2\2\u00bf")
        buf.write("\u00c0\5\34\17\2\u00c0\'\3\2\2\2\u00c1\u00c2\7\r\2\2\u00c2")
        buf.write("\u00c3\7\34\2\2\u00c3)\3\2\2\2\u00c4\u00c5\7\17\2\2\u00c5")
        buf.write("\u00c6\7\34\2\2\u00c6+\3\2\2\2\u00c7\u00c9\7\f\2\2\u00c8")
        buf.write("\u00ca\5\60\31\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2")
        buf.write("\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\7\34\2\2\u00cc-\3\2")
        buf.write("\2\2\u00cd\u00ce\5\60\31\2\u00ce\u00cf\7\34\2\2\u00cf")
        buf.write("/\3\2\2\2\u00d0\u00d1\5\62\32\2\u00d1\u00d2\7\36\2\2\u00d2")
        buf.write("\u00d3\5\60\31\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5\62")
        buf.write("\32\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\61")
        buf.write("\3\2\2\2\u00d7\u00d8\b\32\1\2\u00d8\u00d9\5\64\33\2\u00d9")
        buf.write("\u00df\3\2\2\2\u00da\u00db\f\4\2\2\u00db\u00dc\7%\2\2")
        buf.write("\u00dc\u00de\5\64\33\2\u00dd\u00da\3\2\2\2\u00de\u00e1")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\63\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b\33\1\2\u00e3")
        buf.write("\u00e4\5\66\34\2\u00e4\u00ea\3\2\2\2\u00e5\u00e6\f\4\2")
        buf.write("\2\u00e6\u00e7\7&\2\2\u00e7\u00e9\5\66\34\2\u00e8\u00e5")
        buf.write("\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\65\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00ee\58\35\2\u00ee\u00ef\t\4\2\2\u00ef\u00f0\58\35\2")
        buf.write("\u00f0\u00f3\3\2\2\2\u00f1\u00f3\58\35\2\u00f2\u00ed\3")
        buf.write("\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\67\3\2\2\2\u00f4\u00f5")
        buf.write("\5:\36\2\u00f5\u00f6\t\5\2\2\u00f6\u00f7\5:\36\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00fa\5:\36\2\u00f9\u00f4\3\2\2\2")
        buf.write("\u00f9\u00f8\3\2\2\2\u00fa9\3\2\2\2\u00fb\u00fc\b\36\1")
        buf.write("\2\u00fc\u00fd\5<\37\2\u00fd\u0103\3\2\2\2\u00fe\u00ff")
        buf.write("\f\4\2\2\u00ff\u0100\t\6\2\2\u0100\u0102\5<\37\2\u0101")
        buf.write("\u00fe\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0104\3\2\2\2\u0104;\3\2\2\2\u0105\u0103\3\2\2")
        buf.write("\2\u0106\u0107\b\37\1\2\u0107\u0108\5> \2\u0108\u010e")
        buf.write("\3\2\2\2\u0109\u010a\f\4\2\2\u010a\u010b\t\7\2\2\u010b")
        buf.write("\u010d\5> \2\u010c\u0109\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f=\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0111\u0112\t\b\2\2\u0112\u0115\5> \2\u0113")
        buf.write("\u0115\5@!\2\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("?\3\2\2\2\u0116\u0117\5B\"\2\u0117\u0118\7\32\2\2\u0118")
        buf.write("\u0119\5\60\31\2\u0119\u011a\7\33\2\2\u011a\u011d\3\2")
        buf.write("\2\2\u011b\u011d\5B\"\2\u011c\u0116\3\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011dA\3\2\2\2\u011e\u0126\5D#\2\u011f\u0126")
        buf.write("\5\f\7\2\u0120\u0126\7-\2\2\u0121\u0122\7\26\2\2\u0122")
        buf.write("\u0123\5\60\31\2\u0123\u0124\7\27\2\2\u0124\u0126\3\2")
        buf.write("\2\2\u0125\u011e\3\2\2\2\u0125\u011f\3\2\2\2\u0125\u0120")
        buf.write("\3\2\2\2\u0125\u0121\3\2\2\2\u0126C\3\2\2\2\u0127\u0128")
        buf.write("\7-\2\2\u0128\u0131\7\26\2\2\u0129\u012e\5\60\31\2\u012a")
        buf.write("\u012b\7\35\2\2\u012b\u012d\5\60\31\2\u012c\u012a\3\2")
        buf.write("\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0131")
        buf.write("\u0129\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0134\7\27\2\2\u0134E\3\2\2\2\34IOTgnt\u0080\u008b")
        buf.write("\u0095\u009e\u00a4\u00ab\u00b1\u00c9\u00d5\u00df\u00ea")
        buf.write("\u00f2\u00f9\u0103\u010e\u0114\u011c\u0125\u012e\u0131")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void'", "'int'", "'float'", "'string'", 
                     "'boolean'", "'if'", "'else'", "'while'", "'do'", "'return'", 
                     "'break'", "'for'", "'continue'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", 
                     "'&&'", "'!='", "'=='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "VOIDTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", 
                      "BOOLEANTYPE", "IF", "ELSE", "WHILE", "DO", "RETURN", 
                      "BREAK", "FOR", "CONTINUE", "INTLIT", "BOOLEANLIT", 
                      "FLOATLIT", "STRINGLIT", "BLOCKCOMMENT", "LINECOMMENT", 
                      "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "CM", 
                      "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                      "OR", "AND", "NEQ", "EQ", "LESS", "LESSEQ", "GREATER", 
                      "GREATEREQ", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_mctype = 2
    RULE_arraypointertype = 3
    RULE_primitivetype = 4
    RULE_literal = 5
    RULE_vardecl = 6
    RULE_variablelist = 7
    RULE_variable = 8
    RULE_funcdecl = 9
    RULE_funcname = 10
    RULE_parameterlist = 11
    RULE_parameter = 12
    RULE_stmt = 13
    RULE_ifstmt = 14
    RULE_blockstmt = 15
    RULE_blockitem = 16
    RULE_dowhilestmt = 17
    RULE_forstmt = 18
    RULE_breakstmt = 19
    RULE_continuestmt = 20
    RULE_returnstmt = 21
    RULE_expstmt = 22
    RULE_expr = 23
    RULE_expr1 = 24
    RULE_expr2 = 25
    RULE_expr3 = 26
    RULE_expr4 = 27
    RULE_expr5 = 28
    RULE_expr6 = 29
    RULE_expr7 = 30
    RULE_expr8 = 31
    RULE_operands = 32
    RULE_funcall = 33

    ruleNames =  [ "program", "decl", "mctype", "arraypointertype", "primitivetype", 
                   "literal", "vardecl", "variablelist", "variable", "funcdecl", 
                   "funcname", "parameterlist", "parameter", "stmt", "ifstmt", 
                   "blockstmt", "blockitem", "dowhilestmt", "forstmt", "breakstmt", 
                   "continuestmt", "returnstmt", "expstmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "operands", "funcall" ]

    EOF = Token.EOF
    VOIDTYPE=1
    INTTYPE=2
    FLOATTYPE=3
    STRINGTYPE=4
    BOOLEANTYPE=5
    IF=6
    ELSE=7
    WHILE=8
    DO=9
    RETURN=10
    BREAK=11
    FOR=12
    CONTINUE=13
    INTLIT=14
    BOOLEANLIT=15
    FLOATLIT=16
    STRINGLIT=17
    BLOCKCOMMENT=18
    LINECOMMENT=19
    LB=20
    RB=21
    LP=22
    RP=23
    LSB=24
    RSB=25
    SEMI=26
    CM=27
    ASSIGN=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    NOT=34
    OR=35
    AND=36
    NEQ=37
    EQ=38
    LESS=39
    LESSEQ=40
    GREATER=41
    GREATEREQ=42
    ID=43
    WS=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46
    ERROR_CHAR=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.decl()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.VOIDTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.BOOLEANTYPE))) != 0)):
                    break

            self.state = 73
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MCParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(MCParser.PrimitivetypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def arraypointertype(self):
            return self.getTypedRuleContext(MCParser.ArraypointertypeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mctype)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.primitivetype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.arraypointertype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraypointertypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(MCParser.PrimitivetypeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arraypointertype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraypointertype" ):
                return visitor.visitArraypointertype(self)
            else:
                return visitor.visitChildren(self)




    def arraypointertype(self):

        localctx = MCParser.ArraypointertypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arraypointertype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.primitivetype()
            self.state = 85
            self.match(MCParser.LSB)
            self.state = 86
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(MCParser.BOOLEANTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitivetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitivetype" ):
                return visitor.visitPrimitivetype(self)
            else:
                return visitor.visitChildren(self)




    def primitivetype(self):

        localctx = MCParser.PrimitivetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitivetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.BOOLEANTYPE))) != 0)):
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


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANLIT(self):
            return self.getToken(MCParser.BOOLEANLIT, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0)):
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


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(MCParser.PrimitivetypeContext,0)


        def variablelist(self):
            return self.getTypedRuleContext(MCParser.VariablelistContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.primitivetype()
            self.state = 93
            self.variablelist()
            self.state = 94
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablelistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VariableContext)
            else:
                return self.getTypedRuleContext(MCParser.VariableContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_variablelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariablelist" ):
                return visitor.visitVariablelist(self)
            else:
                return visitor.visitChildren(self)




    def variablelist(self):

        localctx = MCParser.VariablelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variablelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.variable()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 97
                self.match(MCParser.CM)
                self.state = 98
                self.variable()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MCParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MCParser.ID)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 105
                self.match(MCParser.LSB)
                self.state = 106
                self.match(MCParser.INTLIT)
                self.state = 107
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def funcname(self):
            return self.getTypedRuleContext(MCParser.FuncnameContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MCParser.BlockstmtContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(MCParser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.mctype()
            self.state = 111
            self.funcname()
            self.state = 112
            self.match(MCParser.LB)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.BOOLEANTYPE))) != 0):
                self.state = 113
                self.parameterlist()


            self.state = 116
            self.match(MCParser.RB)
            self.state = 117
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_funcname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncname" ):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = MCParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MCParser.ParameterContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = MCParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.parameter()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 122
                self.match(MCParser.CM)
                self.state = 123
                self.parameter()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(MCParser.PrimitivetypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.primitivetype()
                self.state = 130
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.primitivetype()
                self.state = 133
                self.match(MCParser.ID)
                self.state = 134
                self.match(MCParser.LSB)
                self.state = 135
                self.match(MCParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(MCParser.IfstmtContext,0)


        def expstmt(self):
            return self.getTypedRuleContext(MCParser.ExpstmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MCParser.DowhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MCParser.ForstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MCParser.ReturnstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MCParser.ContinuestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MCParser.BreakstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MCParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.ifstmt()
                pass
            elif token in [MCParser.INTLIT, MCParser.BOOLEANLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.LB, MCParser.SUB, MCParser.NOT, MCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.expstmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.dowhilestmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.forstmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.returnstmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.continuestmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.breakstmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.blockstmt()
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


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MCParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MCParser.IF)
            self.state = 150
            self.match(MCParser.LB)
            self.state = 151
            self.expr()
            self.state = 152
            self.match(MCParser.RB)
            self.state = 153
            self.stmt()
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 154
                self.match(MCParser.ELSE)
                self.state = 155
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def blockitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.BlockitemContext)
            else:
                return self.getTypedRuleContext(MCParser.BlockitemContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MCParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MCParser.LP)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.RETURN) | (1 << MCParser.BREAK) | (1 << MCParser.FOR) | (1 << MCParser.CONTINUE) | (1 << MCParser.INTLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID))) != 0):
                self.state = 159
                self.blockitem()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockitemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_blockitem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockitem" ):
                return visitor.visitBlockitem(self)
            else:
                return visitor.visitChildren(self)




    def blockitem(self):

        localctx = MCParser.BlockitemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blockitem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF, MCParser.DO, MCParser.RETURN, MCParser.BREAK, MCParser.FOR, MCParser.CONTINUE, MCParser.INTLIT, MCParser.BOOLEANLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.LB, MCParser.LP, MCParser.SUB, MCParser.NOT, MCParser.ID]:
                self.state = 167
                self.stmt()
                pass
            elif token in [MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE, MCParser.BOOLEANTYPE]:
                self.state = 168
                self.vardecl()
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


    class DowhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MCParser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dowhilestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MCParser.DO)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.stmt()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.RETURN) | (1 << MCParser.BREAK) | (1 << MCParser.FOR) | (1 << MCParser.CONTINUE) | (1 << MCParser.INTLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID))) != 0)):
                    break

            self.state = 177
            self.match(MCParser.WHILE)
            self.state = 178
            self.expr()
            self.state = 179
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MCParser.FOR)
            self.state = 182
            self.match(MCParser.LB)
            self.state = 183
            self.expr()
            self.state = 184
            self.match(MCParser.SEMI)
            self.state = 185
            self.expr()
            self.state = 186
            self.match(MCParser.SEMI)
            self.state = 187
            self.expr()
            self.state = 188
            self.match(MCParser.RB)
            self.state = 189
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MCParser.BREAK)
            self.state = 192
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MCParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MCParser.CONTINUE)
            self.state = 195
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MCParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MCParser.RETURN)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.LB) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID))) != 0):
                self.state = 198
                self.expr()


            self.state = 201
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpstmt" ):
                return visitor.visitExpstmt(self)
            else:
                return visitor.visitChildren(self)




    def expstmt(self):

        localctx = MCParser.ExpstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expr()
            self.state = 204
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MCParser.Expr1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expr1(0)
                self.state = 207
                self.match(MCParser.ASSIGN)
                self.state = 208
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MCParser.Expr1Context,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    self.match(MCParser.OR)
                    self.state = 218
                    self.expr2(0) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MCParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    self.match(MCParser.AND)
                    self.state = 229
                    self.expr3() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr4Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr4Context,i)


        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MCParser.NEQ, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = MCParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr3)
        self._la = 0 # Token type
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.expr4()
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==MCParser.NEQ or _la==MCParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.expr4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.expr4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr5Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr5Context,i)


        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def LESSEQ(self):
            return self.getToken(MCParser.LESSEQ, 0)

        def GREATEREQ(self):
            return self.getToken(MCParser.GREATEREQ, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MCParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.expr5(0)
                self.state = 243
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.LESSEQ) | (1 << MCParser.GREATER) | (1 << MCParser.GREATEREQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self.expr5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.expr5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MCParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MCParser.Expr5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 252
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 253
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 254
                    self.expr6(0) 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MCParser.Expr6Context,0)


        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.expr7() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def expr8(self):
            return self.getTypedRuleContext(MCParser.Expr8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MCParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB, MCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB or _la==MCParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                self.expr7()
                pass
            elif token in [MCParser.INTLIT, MCParser.BOOLEANLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.LB, MCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr8()
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


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MCParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr8)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.operands()
                self.state = 277
                self.match(MCParser.LSB)
                self.state = 278
                self.expr()
                self.state = 279
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operands)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.funcall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.match(MCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.match(MCParser.LB)
                self.state = 288
                self.expr()
                self.state = 289
                self.match(MCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MCParser.ID)
            self.state = 294
            self.match(MCParser.LB)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.LB) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID))) != 0):
                self.state = 295
                self.expr()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.CM:
                    self.state = 296
                    self.match(MCParser.CM)
                    self.state = 297
                    self.expr()
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 305
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr1_sempred
        self._predicates[25] = self.expr2_sempred
        self._predicates[28] = self.expr5_sempred
        self._predicates[29] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




