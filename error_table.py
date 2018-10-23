import sys
import symbol_Table as st
error=[]
error_table=["Invalid No of argument",#0
             "No data type is specified",#1
             "comma, colon, decorator or end of line expected after operand",#2
             "symbol {} redefined",#3
             "attempt to reserve non-constant quantity of BSS space",#4
             "attempt to initialize memory in BSS section `.bss'",#5
             "instruction is expected",#6
             "character constant too long",#7
             "symbol {} not defined",#8
             "unterminated string",#9
             "multiple definition of label {}",#10
             "{} decleared without section keyword",#11
             "{} not preceded by label",#12
             "no operand for data declaration",#13
             "invalid combination of opcode and operands",#14
             "label or instruction expected at the start of line",#15
             "unsigned byte value exceeds bounds",#16
             "Keyword can not to used as label specifier",#17
             "Only integer are allowed",#18
             "Invalid Expression",#19
             "expression syntax error"#20
             "Invalid no of argument for macro {}"#21
]

undefined_label=[]

class Undefined():
    def __init__(self):
        self.name=None
        self.sym_tab=0
        self.line=0
class Error():
    def __init__(self):
        self.errorno = -1
        self.lineno  = -1
        self.token = None

def check_error():
    if(len(error)>0):
        return True
    return False

def insert_into_err(err_info):
    error.append(err_info)
    
def collect_undefined():
    flag = 0
    for i in st.symbol_table:
        un = Undefined()
        if(i.IsDefined==False and i.d_type==None):
           un.name=i.name
           un.sym_tab=i.line
           un.line =i.address
           undefined_label.append(un)
           flag=1
    return flag
def print_error(filename):
    if(check_error()):
        for i in error:
            if(i.token==None):
             
                print(filename+" : " +str(i.lineno)+" error  : "+(error_table[i.errorno]).format(i.token))
            else:
                print(filename+" : " +str(i.lineno)+" error  : "+(error_table[i.errorno]).format(i.token))
def print_undefined(filename):
    for i in undefined_label:
        print(filename+" :  "+ str(i.line)+" error :"+ (error_table[8]).format("'"+i.name+"'"))
               
            
