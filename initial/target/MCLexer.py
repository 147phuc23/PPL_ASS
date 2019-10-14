# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u016e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\6\20")
        buf.write("\u00b4\n\20\r\20\16\20\u00b5\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00c1\n\21\3\22\3\22\5\22\u00c5")
        buf.write("\n\22\3\23\3\23\5\23\u00c9\n\23\3\23\6\23\u00cc\n\23\r")
        buf.write("\23\16\23\u00cd\3\24\6\24\u00d1\n\24\r\24\16\24\u00d2")
        buf.write("\3\24\3\24\7\24\u00d7\n\24\f\24\16\24\u00da\13\24\5\24")
        buf.write("\u00dc\n\24\3\24\7\24\u00df\n\24\f\24\16\24\u00e2\13\24")
        buf.write("\3\24\3\24\6\24\u00e6\n\24\r\24\16\24\u00e7\5\24\u00ea")
        buf.write("\n\24\3\25\3\25\3\25\3\25\7\25\u00f0\n\25\f\25\16\25\u00f3")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u00fb\n\26\f")
        buf.write("\26\16\26\u00fe\13\26\3\26\3\26\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u0109\n\27\f\27\16\27\u010c\13\27\3")
        buf.write("\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\6/\u0145")
        buf.write("\n/\r/\16/\u0146\3/\7/\u014a\n/\f/\16/\u014d\13/\3\60")
        buf.write("\6\60\u0150\n\60\r\60\16\60\u0151\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\7\61\u015a\n\61\f\61\16\61\u015d\13\61\3\62")
        buf.write("\3\62\3\62\3\62\7\62\u0163\n\62\f\62\16\62\u0166\13\62")
        buf.write("\3\62\3\62\3\62\5\62\u016b\n\62\3\63\3\63\5\u00f1\u00fc")
        buf.write("\u0164\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\2\37\20!\21#\22%\2\'\2)\23+\24")
        buf.write("-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61\3\2\n\3\2\62")
        buf.write(";\4\2GGgg\t\2$$^^ddhhppttvv\6\2\f\f\17\17$$^^\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u0181\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\3g\3\2\2\2\5l\3\2\2\2\7p\3\2\2\2\t")
        buf.write("v\3\2\2\2\13}\3\2\2\2\r\u0085\3\2\2\2\17\u0088\3\2\2\2")
        buf.write("\21\u008d\3\2\2\2\23\u0093\3\2\2\2\25\u0096\3\2\2\2\27")
        buf.write("\u009d\3\2\2\2\31\u00a3\3\2\2\2\33\u00a7\3\2\2\2\35\u00b0")
        buf.write("\3\2\2\2\37\u00b3\3\2\2\2!\u00c0\3\2\2\2#\u00c2\3\2\2")
        buf.write("\2%\u00c6\3\2\2\2\'\u00e9\3\2\2\2)\u00eb\3\2\2\2+\u00f6")
        buf.write("\3\2\2\2-\u0104\3\2\2\2/\u010f\3\2\2\2\61\u0111\3\2\2")
        buf.write("\2\63\u0113\3\2\2\2\65\u0115\3\2\2\2\67\u0117\3\2\2\2")
        buf.write("9\u0119\3\2\2\2;\u011b\3\2\2\2=\u011d\3\2\2\2?\u011f\3")
        buf.write("\2\2\2A\u0121\3\2\2\2C\u0123\3\2\2\2E\u0125\3\2\2\2G\u0127")
        buf.write("\3\2\2\2I\u0129\3\2\2\2K\u012b\3\2\2\2M\u012d\3\2\2\2")
        buf.write("O\u0130\3\2\2\2Q\u0133\3\2\2\2S\u0136\3\2\2\2U\u0139\3")
        buf.write("\2\2\2W\u013b\3\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2]\u0144")
        buf.write("\3\2\2\2_\u014f\3\2\2\2a\u0155\3\2\2\2c\u015e\3\2\2\2")
        buf.write("e\u016c\3\2\2\2gh\7x\2\2hi\7q\2\2ij\7k\2\2jk\7f\2\2k\4")
        buf.write("\3\2\2\2lm\7k\2\2mn\7p\2\2no\7v\2\2o\6\3\2\2\2pq\7h\2")
        buf.write("\2qr\7n\2\2rs\7q\2\2st\7c\2\2tu\7v\2\2u\b\3\2\2\2vw\7")
        buf.write("u\2\2wx\7v\2\2xy\7t\2\2yz\7k\2\2z{\7p\2\2{|\7i\2\2|\n")
        buf.write("\3\2\2\2}~\7d\2\2~\177\7q\2\2\177\u0080\7q\2\2\u0080\u0081")
        buf.write("\7n\2\2\u0081\u0082\7g\2\2\u0082\u0083\7c\2\2\u0083\u0084")
        buf.write("\7p\2\2\u0084\f\3\2\2\2\u0085\u0086\7k\2\2\u0086\u0087")
        buf.write("\7h\2\2\u0087\16\3\2\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7n\2\2\u008a\u008b\7u\2\2\u008b\u008c\7g\2\2\u008c\20")
        buf.write("\3\2\2\2\u008d\u008e\7y\2\2\u008e\u008f\7j\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7n\2\2\u0091\u0092\7g\2\2\u0092\22")
        buf.write("\3\2\2\2\u0093\u0094\7f\2\2\u0094\u0095\7q\2\2\u0095\24")
        buf.write("\3\2\2\2\u0096\u0097\7t\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7w\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7p\2\2\u009c\26\3\2\2\2\u009d\u009e\7d\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7m\2\2\u00a2\30\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7t\2\2\u00a6\32\3\2\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7g\2\2\u00af\34\3\2\2\2\u00b0\u00b1")
        buf.write("\t\2\2\2\u00b1\36\3\2\2\2\u00b2\u00b4\5\35\17\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6 \3\2\2\2\u00b7\u00b8\7v\2\2")
        buf.write("\u00b8\u00b9\7t\2\2\u00b9\u00ba\7w\2\2\u00ba\u00c1\7g")
        buf.write("\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7u\2\2\u00bf\u00c1\7g\2\2\u00c0\u00b7")
        buf.write("\3\2\2\2\u00c0\u00bb\3\2\2\2\u00c1\"\3\2\2\2\u00c2\u00c4")
        buf.write("\5\'\24\2\u00c3\u00c5\5%\23\2\u00c4\u00c3\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5$\3\2\2\2\u00c6\u00c8\t\3\2\2\u00c7")
        buf.write("\u00c9\7/\2\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00cb\3\2\2\2\u00ca\u00cc\5\37\20\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce&\3\2\2\2\u00cf\u00d1\5\35\17\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00db\3\2\2\2\u00d4\u00d8\7")
        buf.write("\60\2\2\u00d5\u00d7\5\35\17\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00d4\3")
        buf.write("\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00ea\3\2\2\2\u00dd\u00df")
        buf.write("\5\35\17\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e3\u00e5\7\60\2\2\u00e4\u00e6")
        buf.write("\5\35\17\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2")
        buf.write("\u00e9\u00d0\3\2\2\2\u00e9\u00e0\3\2\2\2\u00ea(\3\2\2")
        buf.write("\2\u00eb\u00f1\7$\2\2\u00ec\u00ed\7^\2\2\u00ed\u00f0\t")
        buf.write("\4\2\2\u00ee\u00f0\n\5\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f4\u00f5\7$\2\2\u00f5*\3\2\2\2\u00f6\u00f7\7\61\2")
        buf.write("\2\u00f7\u00f8\7,\2\2\u00f8\u00fc\3\2\2\2\u00f9\u00fb")
        buf.write("\13\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00ff\u0100\7,\2\2\u0100\u0101\7")
        buf.write("\61\2\2\u0101\u0102\3\2\2\2\u0102\u0103\b\26\2\2\u0103")
        buf.write(",\3\2\2\2\u0104\u0105\7\61\2\2\u0105\u0106\7\61\2\2\u0106")
        buf.write("\u010a\3\2\2\2\u0107\u0109\n\6\2\2\u0108\u0107\3\2\2\2")
        buf.write("\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010b\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e")
        buf.write("\b\27\2\2\u010e.\3\2\2\2\u010f\u0110\7*\2\2\u0110\60\3")
        buf.write("\2\2\2\u0111\u0112\7+\2\2\u0112\62\3\2\2\2\u0113\u0114")
        buf.write("\7}\2\2\u0114\64\3\2\2\2\u0115\u0116\7\177\2\2\u0116\66")
        buf.write("\3\2\2\2\u0117\u0118\7]\2\2\u01188\3\2\2\2\u0119\u011a")
        buf.write("\7_\2\2\u011a:\3\2\2\2\u011b\u011c\7=\2\2\u011c<\3\2\2")
        buf.write("\2\u011d\u011e\7.\2\2\u011e>\3\2\2\2\u011f\u0120\7?\2")
        buf.write("\2\u0120@\3\2\2\2\u0121\u0122\7-\2\2\u0122B\3\2\2\2\u0123")
        buf.write("\u0124\7/\2\2\u0124D\3\2\2\2\u0125\u0126\7,\2\2\u0126")
        buf.write("F\3\2\2\2\u0127\u0128\7\61\2\2\u0128H\3\2\2\2\u0129\u012a")
        buf.write("\7\'\2\2\u012aJ\3\2\2\2\u012b\u012c\7#\2\2\u012cL\3\2")
        buf.write("\2\2\u012d\u012e\7~\2\2\u012e\u012f\7~\2\2\u012fN\3\2")
        buf.write("\2\2\u0130\u0131\7(\2\2\u0131\u0132\7(\2\2\u0132P\3\2")
        buf.write("\2\2\u0133\u0134\7#\2\2\u0134\u0135\7?\2\2\u0135R\3\2")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137\u0138\7?\2\2\u0138T\3\2")
        buf.write("\2\2\u0139\u013a\7>\2\2\u013aV\3\2\2\2\u013b\u013c\7>")
        buf.write("\2\2\u013c\u013d\7?\2\2\u013dX\3\2\2\2\u013e\u013f\7@")
        buf.write("\2\2\u013fZ\3\2\2\2\u0140\u0141\7@\2\2\u0141\u0142\7?")
        buf.write("\2\2\u0142\\\3\2\2\2\u0143\u0145\t\7\2\2\u0144\u0143\3")
        buf.write("\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u014b\3\2\2\2\u0148\u014a\t\b\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2")
        buf.write("\u014b\u014c\3\2\2\2\u014c^\3\2\2\2\u014d\u014b\3\2\2")
        buf.write("\2\u014e\u0150\t\t\2\2\u014f\u014e\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153\u0154\b\60\2\2\u0154`\3\2\2\2\u0155")
        buf.write("\u015b\7$\2\2\u0156\u0157\7^\2\2\u0157\u015a\t\4\2\2\u0158")
        buf.write("\u015a\n\5\2\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2")
        buf.write("\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3")
        buf.write("\2\2\2\u015cb\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0164")
        buf.write("\7$\2\2\u015f\u0160\7^\2\2\u0160\u0163\t\4\2\2\u0161\u0163")
        buf.write("\n\5\2\2\u0162\u015f\3\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0165\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u016a\7")
        buf.write("^\2\2\u0168\u016b\n\4\2\2\u0169\u016b\7\2\2\3\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016bd\3\2\2\2\u016c\u016d")
        buf.write("\13\2\2\2\u016df\3\2\2\2\32\2\u00b5\u00c0\u00c4\u00c8")
        buf.write("\u00cd\u00d2\u00d8\u00db\u00e0\u00e7\u00e9\u00ef\u00f1")
        buf.write("\u00fc\u010a\u0146\u014b\u0151\u0159\u015b\u0162\u0164")
        buf.write("\u016a\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VOIDTYPE = 1
    INTTYPE = 2
    FLOATTYPE = 3
    STRINGTYPE = 4
    BOOLEANTYPE = 5
    IF = 6
    ELSE = 7
    WHILE = 8
    DO = 9
    RETURN = 10
    BREAK = 11
    FOR = 12
    CONTINUE = 13
    INTLIT = 14
    BOOLEANLIT = 15
    FLOATLIT = 16
    STRINGLIT = 17
    BLOCKCOMMENT = 18
    LINECOMMENT = 19
    LB = 20
    RB = 21
    LP = 22
    RP = 23
    LSB = 24
    RSB = 25
    SEMI = 26
    CM = 27
    ASSIGN = 28
    ADD = 29
    SUB = 30
    MUL = 31
    DIV = 32
    MOD = 33
    NOT = 34
    OR = 35
    AND = 36
    NEQ = 37
    EQ = 38
    LESS = 39
    LESSEQ = 40
    GREATER = 41
    GREATEREQ = 42
    ID = 43
    WS = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46
    ERROR_CHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'int'", "'float'", "'string'", "'boolean'", "'if'", 
            "'else'", "'while'", "'do'", "'return'", "'break'", "'for'", 
            "'continue'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", 
            "'&&'", "'!='", "'=='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "VOIDTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", 
            "IF", "ELSE", "WHILE", "DO", "RETURN", "BREAK", "FOR", "CONTINUE", 
            "INTLIT", "BOOLEANLIT", "FLOATLIT", "STRINGLIT", "BLOCKCOMMENT", 
            "LINECOMMENT", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", 
            "CM", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", 
            "AND", "NEQ", "EQ", "LESS", "LESSEQ", "GREATER", "GREATEREQ", 
            "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "VOIDTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "BOOLEANTYPE", 
                  "IF", "ELSE", "WHILE", "DO", "RETURN", "BREAK", "FOR", 
                  "CONTINUE", "DIGIT", "INTLIT", "BOOLEANLIT", "FLOATLIT", 
                  "EX", "FRACTION", "STRINGLIT", "BLOCKCOMMENT", "LINECOMMENT", 
                  "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "CM", "ASSIGN", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", "AND", 
                  "NEQ", "EQ", "LESS", "LESSEQ", "GREATER", "GREATEREQ", 
                  "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        elif tk == self.STRINGLIT:
            result = super().emit()
            result.text = result.text[1:-1]
        else:
            return super().emit();


