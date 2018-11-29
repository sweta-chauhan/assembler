#error were not handled in this pass all macro definetion are considered to be error free basic operator and operand combination like no of argument were checked and only 2 argument length pacro will be parsed
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
macro_expan=[]
def macro_definition(lines,index):
    m_d_t =  macro_definetion()
    m_d_t.index = index
    for line in lines:
        if "%macro" in line:
            line=line.split(' ')
            m_d_t.name = line[1]
            m_d_t.no_of_arg = int(line[2])
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
def put_expan(fd1,ind,token,index_of_arg,code_flag):
    for i in macro_definetion_table[ind].code:
        if '%' in i:
            macro_expan.append(code_flag)
            code_flag+=1
        else:
            code_flag+=1
    for i,k in enumerate(token[1:]):
        code1 = macro_definetion_table[ind].code[macro_expan[i]]
        index_of_arg+=1
        #print(token[1:],k,code1.replace("%"+str(index_of_arg),k))
        fd1.write(code1.replace("%"+str(index_of_arg),k))
        #print(code1.replace("%"+str(index_of_arg),k))
    return code_flag
def pass0(fd):
    fd1 = open(".pass0","w")
    #fd = open(filname,"r")
    lines = fd.readlines()
    startofmacro=[]
    endofmacro=[]
    code = []
    d_c = []
    b_c = []
    err = et.Error()
    text_flag = 0
    main_index = 0
    data_index = 0
    token = []
    count=0
    ind = 0
    index_of_arg=0
    for i,line in enumerate(lines):
        if ".data" in line:
            data_index = i
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
    while(main_index>data_index):
        fd1.write(code[data_index])
        data_index+=1
    for code1 in code[main_index:]:
        token=t.fileToToken(code1,ot.data_types,token)
        if(len(token)>0):
            if(len(token)==4 and token[0][-1]==':'):
                
                if(search_macro_in_mdt(token[1])):
                    
                    ind = search_index(token[1])
                    fd1.write(token[0])
                    if(len(token[2:]) == macro_definetion_table[ind].no_of_arg):
                        index_of_arg = 0
                        cnt=0
                        code_flag = 0
                        #fd1.write(token[0])
                        for i in macro_definetion_table[ind].code:
                            if '%' in i:
                                if(code_flag<len(macro_definetion_table[ind].code)):
                                    code_flag=put_expan(fd1,ind,token[1:],index_of_arg,0)
                                    code_flag+=code_flag
                            else:
                                
                                fd1.write(i)
                                code_flag+=1
                                index_of_arg =0
                        #print(code1)
                else:
                    
                    fd1.write(code1)
            elif(len(token)==3 and search_macro_in_mdt(token[0])):
                ind = search_index(token[0])
                if(len(token[1:]) == macro_definetion_table[ind].no_of_arg):
                    index_of_arg = 0
                    cnt=0
                    code_flag = 0
                    for i in macro_definetion_table[ind].code:
                        if '%' in i:
                            if(code_flag<len(macro_definetion_table[ind].code)):
                                code_flag=put_expan(fd1,ind,token,index_of_arg,0)
                                code_flag+=code_flag
                        else:
                            fd1.write(i)
                            code_flag+=1
                    
            else:
                fd1.write(code1)
            token=[]
    fd.close()
    fd1.close()

'''if __name__ == "__main__":
    fd=open(sys.argv[1],"r")
    pass0(fd) 
'''
