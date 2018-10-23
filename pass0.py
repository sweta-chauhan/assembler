#error were not handled in this pass all macro definetion are considered to be error free basic operator and operand combination like no of argument were checked
import sys
import re
import opcode_table as ot
import tokenizer as t
import error_table as et
import struct_to_file as stf

class macro_definetion():
    def __init__(self):
        self.index=0
        self.name=None
        self.no_of_arg=0
        self.code=[]

macro_definetion_table=[]
#mac_expan=[]
def macro_definition(lines,index):
    m_d_t =  macro_definetion()
    m_d_t.index = index
    for line in lines:
        if "%macro" in line:
            line=line.split(' ')
            m_d_t.name = line[1]
            m_d_t.no_of_args = int(line[2])
        else:
            m_d_t.code.append(line)
    macro_definetion_table.append(m_d_t)

def search_macro_in_mdt(macro):
    for i in macro_definetion_table:
        if i.name == macro:
            return True
    return False
def search_macro_in_arg(macro):
    for i in macro_definetion_table:
        if i.name == macro:
            return i.index
    return -1
def search_index(macro):
    for i in macro_definetion_table:
        if i.name == macro:
            return i.index
    return -1
'''def find_no_of_argument(macro):
    for i in macro_definetion_table:
        if i.name == macro:
            return i.no_of_args
    return -1
def expend(fd,line,line_no):
    m_e=mac_expansion()
    inst=[]
    ind=1-
    if search_macro_in_mdt(line[0]) and len(line)-1 == find_no_of_argument(line[0]):
        for i in macro_definetion_table:
            if(i.name==line[0]):
                for j in i.code:
                    if(bool(re.match(r'^%[1-9]',j[2]))):
                        inst=j
                        inst[2]=j[ind]
                        ind+=1
                        fd.write('\t')
                        stf.listTofile(fd,j)
                    else:
                        fd.write('\t')
                        stf.listTofile(fd,j)
def end_of_mac(fd,):
'''    
def pass0(filename):
    fd = open(filename,"r")
    fd1 = open("pass0","w")
    lines = fd.readlines()
    startofmacro=[]
    endofmacro=[]
    code = []
    err = et.Error()
    text_flag = 0
    main_index = 0
    token = []
    count=0
    ind = 0
    index_of_arg=0
    for i,line in enumerate(lines):
        if ".text" in line:
            text_flag = 1
            main_index = i
        if text_flag!=1:
            if "%macro" in line:
                startofmacro.append(i)
            if "%endmacro" in line:
                endofmacro.append(i)
        code.append(line)
    for j in range(len(startofmacro)):
        macro_definition(code[startofmacro[j]:endofmacro[j]],count)
        count+=1
    for code1 in code[main_index:]:
        token=t.fileToToken(code1,ot.data_types,token)
        print(token)
        if(len(token)==3 and token[0][-1]==':'):
            if(search_macro_in_mdt(token[1])):
                ind = search_index(token[1])
                if(len(token[1:])-1 == macro_definetion_table[ind].no_of_arg):
                    index_of_arg =0
                    for k in token[2:]:
                        for i in macro_definetion_table[ind].code:
                            index_of_arg = index_of_arg+1
                            print(i.replace("%"+str(index_of_arg),k))
                        #print(i)
        elif(search_macro_in_mdt(token[0])):
             ind = search_index(token[1])
             if(len(token[1:])-1 == macro_definetion_table[ind].no_of_arg):
                 index_of_arg = 0
                 for k in token[2:]:
                     index_of_arg = index_of_arg+1
                     for i in macro_definetion_table[ind].code:
                         i.replace("%"+str(index_of_arg),k)
                         print(i.replace("%"+str(index_of_arg),k))
                         #print(i)
        else:
            print(code1)
        token=[]
                    
if __name__ =="__main__":
    pass0(sys.argv[1])
    for i in macro_definetion_table:
        print(i.index,i.name,i.no_of_args,i.code)





    
