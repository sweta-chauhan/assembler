class symbol_info():
    def __init__(self):
        self.line=0
        self.section=None
        self.name = None
        self.size = 0
        self.no_of_element = 0
        self.IsDefined = False
        self.d_type = None
        self.Type = None
        self.value = None
        self.address = 0
symbol_table = []

def insert_into_symtab(sym_info):
    symbol_table.append(sym_info)

def search_symtab(name):
    for i in symbol_table:
        if i.name==name:
            return True
    return False

def search_index(name):
    for i in symbol_table:
        if i.name==name:
            return i.line
    return -1

def find_d_type(token):
    for i in symbol_table:
        if i.name==token and i.d_type=="equ":
            return True
    return False

def find_len_from_symbolTable(value):
    size = -1
    for i in symbol_table:
        if i.name==value:
            return i.no_of_element
    return size
def size_symbol(value):
    size=-1
    for i in symbol_table:
        if i.name == value:
            return i.size
    return size

def find_not_defined():
    count=0
    for i in symbol_table:
        if(i.IsDefined==False and i.d_type==None):
            count+=1
    return count
def put_label_is_defined(token,line_no):
    for sym in symbol_table:
        if sym.name == token and sym.IsDefined==True:
            return -1  
        elif sym.name == token and sym.IsDefined==False:
            sym.IsDefined = True
            sym.address = line_no
            return 1
    return 0
def is_defined(token):
    for sym in symbol_table:
        if sym.name == token and sym.IsDefined==True:
            return 1
    return 0
def print_symbol_table():
    print("**********************************************************************Symbol Table**************************************************".center(50))
    print("Index".ljust(20),"Section".ljust(20),"Name".ljust(20),"Size".ljust(20),"No_Of_Element".ljust(20),"IsDefined".ljust(10),"d_type".ljust(10),"Type".ljust(10),"Value".ljust(10),"Address".ljust(10))
    for i in symbol_table:
        print(str(i.line).ljust(20),(i.section).ljust(20),(i.name).ljust(20),str(i.size).ljust(20),str(i.no_of_element).ljust(20),str(i.IsDefined).ljust(10),str(i.d_type).ljust(10),str(i.Type).ljust(10),str(i.value).ljust(10),str(i.address).ljust(10))

def symbol_to_file(fp):
    #fp = open(".sym","w")
    for i in symbol_table:
        fp.write(str(i.line)+"|"+i.section+"|"+i.name+"|"+str(i.size)+"|"+str(i.no_of_element)+"|"+str(i.IsDefined)+"|"+str(i.d_type)+"|"+str(i.Type)+"|"+str(i.value)+"|"+str(i.address)+'\n')


def file_to_symbol(lines,start,end):
    #lines = fp.readlines()
    for line in lines[start:end]:
        st=symbol_info()
        line = line.split('|')
        st.line=int(line[0])
        st.section=line[1]
        st.name = line[2]
        st.size = int(line[3])
        st.no_of_element = int(line[4])
        st.IsDefined = bool(line[5])
        st.d_type = line[6]
        st.Type = line[7]
        st.value = line[8]
        st.address = int(line[9])
        symbol_table.append(st)

def find_value_by_address(address):
    value =""
    for i in symbol_table:
        if(i.Type=='S' and i.address==address and i.section==".data"):
            value = i.value
            #print(value)
    return value
'''
oif __name__=="__main__":
    handle()
    print_symbol_table()
'''
#print(find_value_by_address(4))
