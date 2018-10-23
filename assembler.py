import sys
import re
import charToHex as ch
import register_dict as rd
import literal as lt
import symbol_Table as st
import error_table as et
import opcode_table as ot
import isValid_token as ist
import pass1 as p1
import tokenizer as t

class Traced_section():
    def __init__(self):
        self.s_name=None
        self.addr=0

    
def equ_size(data_type,next_part):
    l = next_part.split("$-")
    if(len(l)==2):
        l1 = l[1].strip(' ')
    count =0
    if l[0]=='':
        count = st.find_len_from_symbolTable(l1)
    else:
        count=int(next_part)
    return count

def find_len(string):
    count = 0
    j=0
    main_str=""
    l = string.split(",")
    for i in l:
        if i == '10' or i == '0':
            count+=1
        else:
            main_str = i
    if(j==0 and (main_str[j]=="\"" and main_str[len(main_str)-1]=="\"")):
        for i in main_str:
            if i != "'" and i !="\"" and i!="\\":
                count+=1
    else:
        count=len(l)  
    return count
def Is_traced(traced_section,section):
    for i in traced_section:
        if(section==i.s_name):
            return True
    return False
def traced_s_addr(traced_section,section):
    for i in traced_section:
        if i.s_name==section:
            return i.addr
    return 0
def Isvalid_identifer(label):
    return bool(re.match())
def parse_data(token,section,in_addr,line_no,sym_cnt,lit_cnt):
    error = et.Error()
    symbol = st.symbol_info()
    Lt_info = lt.Literal_info()
    #print(token)
    if section == ".data":
        if (len(token)==3):
            if(ot.IsKeyWord(token[0])!=True):
                
                if(st.search_symtab(token[0])):
                    error.lineno=line_no
                    error.errorno = 3
                    error.token = token[0]
                    et.insert_into_err(error)
                    if(ot.is_operator(token[1])!=True):
                        err=Error()
                        err.errorno=1
                        err.lineno=line_no
                        et.insert_into_err(error)
                else:
                    if(ist.Isvalid_naming(token[0])!=True):
                        error.lineno=line_no
                        error.errorno = 15
                        error.token = token[0]
                        et.insert_into_err(error)
                    elif(token[1]=='db'):
                        sym_cnt+=1
                        if(lt.Is_inserted(token[2])!=True):
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            Lt_info.rl_value = token[2]
                            Lt_info.hex_value = ch.int_to_hex(token[2],'db')
                            lt.insert_Into_Literal(Lt_info)
                        symbol.line = sym_cnt
                        symbol.section=section
                        symbol.name=token[0]
                        symbol.size = 1
                        symbol.no_of_element = find_len(token[2])
                        symbol.d_type='db'
                        symbol.IsDefined = True
                        symbol.address = in_addr
                        symbol.Type = 'S'
                        symbol.value = 'lit#'+str(lit_cnt)
                        in_addr=in_addr + (symbol.size)*(symbol.no_of_element)
                        st.insert_into_symtab(symbol)
                    elif(token[1]=='dd'):
                        sym_cnt+=1
                        if(lt.Is_inserted(token[2])!=True):
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            Lt_info.rl_value = token[2]
                            Lt_info.hex_value = ch.int_to_hex(token[2],'dd')
                            lt.insert_Into_Literal(Lt_info)
                        symbol.line = sym_cnt
                        symbol.section=section
                        symbol.name=token[0]
                        symbol.size = 4
                        symbol.d_type='dd'
                        symbol.no_of_element = len(token[2].split(','))
                        symbol.IsDefined = True
                        symbol.address = in_addr
                        symbol.value = 'lit#'+str(lit_cnt)
                        symbol.Type='S'
                        in_addr=in_addr + (symbol.size)*(symbol.no_of_element)
                        st.insert_into_symtab(symbol)
                    elif(token[1]=='dw'):
                        sym_cnt+=1
                        if(lt.Is_inserted(token[2])!=True):
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            Lt_info.rl_value = token[2]
                            Lt_info.hex_value = ch.int_to_hex(token[2],'dw')
                            lt.insert_Into_Literal(Lt_info)                        
                        symbol.name=token[0]
                        symbol.line = sym_cnt#line_no
                        symbol.section=section
                        symbol.address = in_addr 
                        symbol.d_type='dq'
                        symbol.Type='S'
                        symbol.value = 'lit#'+str(lit_cnt)
                        in_addr=in_addr + (symbol.size)*(symbol.no_of_element)
                        st.insert_into_symtab(symbol)
                    elif(token[1]=='equ'):
                        symbol.size = equ_size("equ",token[2])
                        l=token[2]
                        l=l.strip("$- ")[0]

                        if(l=="\"" and token[2][-1]=="\""):
                            
                            err=et.Error()
                            err.errorno=7
                            err.lineno=line_no
                            et.insert_into_err(err)
                        elif(l=="\"" or token[2][-1]=="\""): 
                            err1=et.Error()
                            err1.errorno=2
                            err1.lineno=line_no
                            err=et.Error()
                            err.errorno=9
                            err.lineno=line_no
                            et.insert_into_err(err1)
                            et.insert_into_err(err)
                        if(token[2][-1]!="\""):
                            if(symbol.size==-1):
                                error.errorno = 8
                                error.token = token[2]
                                error.lineno = line_no
                            else:
                                sym_cnt+=1
                                if(lt.Is_inserted(token[2])!=True):
                                    lit_cnt+=1
                                    Lt_info.f_line = lit_cnt
                                    Lt_info.rl_value = symbol.size
                                    Lt_info.hex_value = hex(symbol.size).strip('0x')
                                    lt.insert_Into_Literal(Lt_info)
                                symbol.line=sym_cnt
                                symbol.section=section
                                symbol.name=token[0]
                                symbol.no_of_element = 0
                                symbol.IsDefined = True
                                symbol.value = None
                                symbol.d_type='equ'
                                symbol.Type='S'
                                symbol.value = 'lit#'+str(lit_cnt)
                                in_addr=in_addr +(symbol.size)*(symbol.no_of_element)
                                st.insert_into_symtab(symbol)
                    else:
                        error.errorno=1
                        error.lineno=line_no
                        et.insert_into_err(error)
                        if(st.search_symtab(token[0])):
                            err = Error()
                            err.lineno=line_no
                            err.errorno = 3
                            err.token = token[0]
                            et.insert_into_err(err)
            else:
                error.errorno=15
                error.lineno=line_no
                et.insert_into_err(error)
                if(st.search_symtab(token[0])):
                    err = Error()
                    err.lineno=line_no
                    err.errorno = 3
                    err.token = token[0]
                    et.insert_into_err(error)
        elif(len(token)>3 or len(token)==2):
            if(ot.IsKeyWord(token[0])==True):
                error.errorno =12
                error.lineno = line_no
                error.token = token[0]
                et.insert_into_err(error)
            elif(ot.IsKeyWord(token[0])!=True and ot.IsKeyWord(token[1])==True):
                error.errorno = 13
                error.lineno = line_no
                et.insert_into_err(error)
            else:
                error.errorno=6
                error.lineno = line_no
                et.insert_into_err(error)
    elif(section==".bss"):
        if (len(token)==3):
            if((ot.IsKeyWord(token[0])!=True) and(ot.is_operator(token[0])!=True)and (ot.IsRegister(token[0])!=True)):
                if(st.search_symtab(token[0])):
                    error.lineno=line_no
                    error.errorno = 3
                    error.token = token[0]
                    et.insert_into_err(error)
                    if(ot.IsKeyWord(token[1])!=True):
                        err=Error()
                        err.errorno=1
                        err.lineno=line_no
                        et.insert_into_err(error)
                else:
                    if(ist.Isvalid_naming(token[0])!=True):
                        error.lineno=line_no
                        error.errorno = 15
                        error.token = token[0]
                        et.insert_into_err(error)
                    elif(token[1]=="resb"):
                        chk=st.find_d_type(token[2])
                        isd=token[2].isdigit()  
                        if(chk or isd):
                            sym_cnt+=1
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            symbol.line = sym_cnt#line_no
                            symbol.section=section
                            symbol.name=token[0]
                            symbol.size = ot.find_size(token[1])
                            if(chk):
                                Lt_info.rl_value = st.size_symbol(token[2])
                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'resb')
                                
                            else:
                                Lt_info.rl_value = int(token[2])
                                Lt_info.hex_value = ch.int_to_hex(token[2],'resb')
                                
                            symbol.IsDefined = True
                            symbol.no_of_element = 1
                            symbol.address = in_addr
                            symbol.d_type='resb'
                            symbol.Type = 'S'
                            symbol.value = 'lit#'+str(lit_cnt)
                            in_addr=(in_addr) + (symbol.size)*(Lt_info.rl_value) 
                            st.insert_into_symtab(symbol)
                            lt.insert_Into_Literal(Lt_info)
                        elif(st.search_symtab(token[2])):
                            error.errorno=4
                            error.lineno=line_no
                            et.insert_into_err(error)
                        
                        elif(st.search_symtab(token[2]) != True and len(token[2])-2>4):
                            error.errorno=7
                            error.lineno=line_no
                            et.insert_into_err(error)
                        else:
                            error.errorno=8
                            error.token=token[2]
                            error.lineno=line_no
                            et.insert_into_err(error)
                    elif(token[1]=="resw"):
                        chk=st.find_d_type(token[2])
                        isd=token[2].isdigit()
                        if(chk or isd):
                            sym_cnt+=1
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            symbol.line = sym_cnt
                            symbol.section=section
                            symbol.name=token[0]
                            symbol.value = 'lit#'+str(lit_cnt)
                            symbol.size = ot.find_size(token[1])
                            if(chk):
                                Lt_info.rl_value = st.size_symbol(token[2])
                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'resw')                     
                            else:
                                Lt_info.rl_value = int(token[2])
                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'resw')
                            symbol.IsDefined = True
                            symbol.no_of_element = 1
                            symbol.address = in_addr
                            symbol.d_type='resw'
                            symbol.Type = 'S'
                            in_addr=in_addr + (symbol.size)*(Lt_info.rl_value)
                            st.insert_into_symtab(symbol)
                            lt.insert_Into_Literal(Lt_info)
                        elif(st.search_symtab(token[2])):
                            error.errorno=4
                            error.lineno=line_no
                            et.insert_into_err(error)
                        elif(st.search_symtab(token[2]) != True and len(token[2])-2>4):
                            error.errorno=7
                            error.lineno=line_no
                            et.insert_into_err(error)
                        else:
                            error.errorno=8
                            error.token=token[2]
                            error.lineno=line_no
                            et.insert_into_err(error)
                    elif(token[1]=="resd"):
                        chk=st.find_d_type(token[2])
                        isd=token[2].isdigit()
                        if(chk or isd):
                            sym_cnt+=1
                            lit_cnt+=1
                            Lt_info.f_line = lit_cnt
                            symbol.line = sym_cnt
                            symbol.section=section
                            symbol.name=token[0]
                            symbol.value = 'lit#'+str(lit_cnt)
                            symbol.size = ot.find_size(token[1])
                            if(chk):
                                Lt_info.rl_value = st.size_symbol(token[2])
                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'resd')
                                
                            else:
                                Lt_info.rl_value = int(token[2])#SizeInSymbolTable(sym_tab,token[2])
                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'resd')
                            symbol.IsDefined = True
                            symbol.no_of_element = 1
                            symbol.address = in_addr
                            symbol.d_type='resd'
                            symbol.Type = 'S'
                            in_addr=in_addr + (symbol.size)*(Lt_info.rl_value)
                            st.insert_into_symtab(symbol)
                            lt.insert_Into_Literal(Lt_info)
                        elif(st.search_symtab(token[2])):
                            error.errorno=4
                            error.lineno=line_no
                            et.insert_into_err(error)
                        elif(st.search_symtab(sym_tab,token[2]) != True and len(token[2])-2>4):
                            error.errorno=7
                            error.lineno=line_no
                            et.insert_into_err(error)
                        else:
                            error.errorno=8
                            error.token=token[2]
                            error.lineno=line_no
                            et.insert_into_err(error)
                    elif(ot.IsKeyWord(token[1])):
                        error.errorno=5
                        error.lineno=line_no
                        et.insert_into_err(error)
                    else:
                        error.errorno=6
                        error.lineno=line_no
                        et.insert_into_err(error)
            else:
                error.errorno = 0
                error. lineno = line_no
                et.insert_into_err(error)
    elif(section ==".text"):
            if(len(token)>0):
                if(token[0]=='global'):
                    len_lst = len(token)
                    for i in range(1,len_lst):    
                        if(ist.Isvalid_naming(token[i])!=True):
                            #print("Hello")
                            error.lineno=line_no
                            error.errorno = 15
                            error.token = token[i]
                            et.insert_into_err(error)
                        elif(ot.IsKeyWord(token[i])==True):
                            #print("H1")
                            error.lineno=line_no
                            error.errorno = 15
                            error.token = token[i]
                            et.insert_into_err(error)
                        else:
                            symbol=st.symbol_info()
                            sym_cnt+=1
                            symbol.line = sym_cnt#line_no
                            symbol.section=section
                            symbol.name=token[i]
                            symbol.IsDefined = False
                            symbol.address = line_no 
                            symbol.Type = 'L'
                            st.insert_into_symtab(symbol)
                if(token[0]=='extern'):
                    len_lst = len(token)
                    for i in range(1,len_lst):
                        if(ist.Isvalid_naming(token[i])!=True):
                            error.lineno=line_no
                            error.errorno = 15
                            error.token = token[i]
                            et.insert_into_err(error)
                        else:
                            symbol=st.symbol_info()
                            sym_cnt+=1
                            symbol.line = sym_cnt#line_no
                            symbol.section=section
                            symbol.name=token[i]
                            symbol.IsDefined = False
                            symbol.address = line_no 
                            symbol.Type = 'L'
                            symbol.d_type ='EX'
                            st.insert_into_symtab(symbol)
                if(token[0][-1]==":"):
                    
                    label=token[0].strip(":")
                    if(ist.Isvalid_naming(token[0])!=True):
                            error.lineno=line_no
                            error.errorno = 15
                            error.token = token[0]
                            et.insert_into_err(error)
                    else:
                        l=st.put_label_is_defined(label,line_no)
                        if(l==0):
                            if(ist.Isvalid_naming(token[0])!=True):
                                error.lineno=line_no
                                error.errorno = 15
                                error.token = token[0]
                                et.insert_into_err(error)
                            else:
                                sym_cnt+=1
                                symbol.line = sym_cnt
                                symbol.section=section
                                symbol.name=label
                                symbol.IsDefined = True
                                symbol.address = line_no 
                                symbol.Type = 'L'
                                st.insert_into_symtab(symbol)
                        elif(l==-1):
                            error.errorno=10
                            error.token=symbol.name
                            error.lineno = line_no
                            et.insert_into_err(error)
                if(ot.is_label_specifier(token[0])==True and (token[0]!='global' or token[0]!='extern')):
                    if(st.search_symtab(token[1])!=True):
                        if(ist.Isvalid_naming(token[0])!=True):
                            error.lineno=line_no
                            error.errorno = 15
                            error.token = token[0]
                            et.insert_into_err(error)
                        elif ot.IsKeyWord(token[0])==True and ot.is_label_specifier(token[0]!=True):
                            error.lineno=line_no
                            #print(token)
                            error.errorno = 17
                            error.token = token[0]
                            et.insert_into_err(error)
 
                        else:
                            sym_cnt+=1
                            symbol.line = sym_cnt#line_no
                            symbol.section=section
                            symbol.name=token[1]
                            symbol.IsDefined = False
                            symbol.address = line_no 
                            symbol.Type = 'L'
                            st.insert_into_symtab(symbol)
            if(len(token)==3):
                
                if token[0] in ot.operand_count:
                    if ot.operand_count[token[0]] == 2:
                        #print(token)
                        if ot.IsRegister(token[1]):
                            if ot.IsRegister(token[2])!=True:
                               if(bool(re.match(r'dword[\D$]',token[2]))):#Expression must be in the from of [iden+Index[reg,int]*Scale] or [iden+iden] or [iden]
                                   ls = token[2][6:-1]
                                   ls=list(map(lambda x : x.strip(' '),ls.split('+')))
                                   if(len(ls)==3):
                                       error.lineno=line_no
                                       error.errorno = 20
                                       et.insert_into_err(error)
                                   elif(st.search_symtab(ls[0])!=True and ot.IsRegister(ls[0])!=True and len(ls)==1):
                                       if(bool(re.match(r'^\d*$',ls[0]))!=True):
                                           sym_cnt+=1
                                           symbol.line = sym_cnt
                                           symbol.section=section
                                           symbol.name=ls[0]
                                           symbol.IsDefined = False
                                           symbol.address = line_no 
                                           symbol.Type = 'L'
                                           st.insert_into_symtab(symbol)
                                       else:
                                           Lt_info.rl_value = int(ls[0])
                                           Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'dd')
                                           lit_cnt+=1
                                           Lt_info.f_line=lit_cnt
                                           lt.insert_Into_Literal(Lt_info)
                                   elif(len(ls)==2 and ls[1]!=''):
                                       ls1=list(map(lambda x : x.strip(' '),ls[1].split('*')))
                                       
                                       if(len(ls1)==2 and ls1[1]!=''):
                                           
                                           if(st.search_symtab(ls[0])!=True and ot.IsRegister(ls[0])!=True and (bool(re.match(r'\d*$',ls1[0]))==True and bool(re.match(r'\d*$',ls1[1]))==True)):
                                               sym_cnt+=1
                                               symbol.line = sym_cnt
                                               symbol.section=section
                                               symbol.name=ls[0]
                                               symbol.IsDefined = False
                                               symbol.address = line_no 
                                               symbol.Type = 'L'
                                               st.insert_into_symtab(symbol)
                                               Lt_info.rl_value = int(ls1[0])
                                               Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'dd')
                                               lit_cnt+=1
                                               Lt_info.f_line=lit_cnt
                                               lt.insert_Into_Literal(Lt_info)

                                               lit=lt.Literal_info()
                                               lit.rl_value = int(ls1[1])
                                               lit.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'dd')
                                               lit_cnt+=1
                                               lit.f_line=lit_cnt
                                               lt.insert_Into_Literal(lit)
                                           if(st.search_symtab(ls[0])!=True and ot.IsRegister(ls[0])!=True and ot.IsRegister(ls1[0])==True and bool(re.match(r'^\d*$',ls1[1]))==True):                                                
                                                sym_cnt+=1
                                                symbol.line = sym_cnt
                                                symbol.section=section
                                                symbol.name=ls[0]
                                                symbol.IsDefined = False
                                                symbol.address = line_no 
                                                symbol.Type = 'L'
                                                st.insert_into_symtab(symbol)
                                                Lt_info.rl_value = int(ls1[1])
                                                Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'dd')
                                                lit_cnt+=1
                                                Lt_info.f_line=lit_cnt
                                                lt.insert_Into_Literal(Lt_info)
                                       elif(len(ls)==2):
                                           print(token)
                                           if(st.search_symtab(ls[0])!=True and ot.IsRegister(ls[1])==True):
                                               sym_cnt+=1
                                               symbol.line = sym_cnt
                                               symbol.section=section
                                               symbol.name=ls[0]
                                               symbol.IsDefined = False
                                               symbol.address = line_no 
                                               symbol.Type = 'L'
                                               st.insert_into_symtab(symbol)
                                           
                                               
                                       elif(ot.IsRegister(ls[0])!=True and ot.IsRegister(ls1[0])!=True):
                                           error.lineno=line_no
                                           error.errorno = 20
                                           et.insert_into_err(error)
                                                                           
                               elif(bool(re.match(r'^\d*$',token[2]))):
                                   Lt_info.rl_value = int(token[2])
                                   Lt_info.hex_value = ch.int_to_hex(str(Lt_info.rl_value),'dd')
                                   lit_cnt+=1
                                   Lt_info.f_line=lit_cnt
                                   lt.insert_Into_Literal(Lt_info)
                               elif(token[2][0]!="\"" and token[2][-1]!="\""):
                                   if(st.search_symtab(token[2])!=True and ot.IsRegister(token[2])!=True):
                                       
                                       sym_cnt+=1
                                       symbol.line = sym_cnt
                                       symbol.section=section
                                       symbol.name=token[2]
                                       symbol.IsDefined = False
                                       symbol.address = line_no 
                                       symbol.Type = 'L'
                                       st.insert_into_symtab(symbol)
                               else:
                                   error.lineno=line_no
                                   error.errorno = 14
                                   et.insert_into_err(error)
    return in_addr,sym_cnt,lit_cnt
def parse_it(fp):
    instruction = []
    section = ""
    token = []
    line_no=0
    global_flag = False
    error_flag=False
    section_count=0
    sym_cnt=0
    lit_cnt=0
    traced_section=[]
    lines = fp.readlines()
    for line in lines:
        line_no+=1
        token=t.fileToToken(line,ot.data_types,[])
        #print(token)
        if(len(token)!=0):
            if(token[0]=="section"):
                s_info =Traced_section()
                if(token[1]==".data"):
                    section = ".data"
                    if(Is_traced(traced_section,section)!=True):
                        s_info.s_name=section
                        s_info.addr=0
                        traced_section.append(s_info)
                    else:
                        s_info.addr=traced_s_addr(traced_section,section)
                if(token[1]==".bss"):
                    section = ".bss"
                    
                    if(Is_traced(traced_section,section)!=True):
                        s_info.s_name=section
                        s_info.addr=0
                        traced_section.append(s_info)
                    else:
                        s_info.addr=traced_s_addr(traced_section,section)
                if(token[1]==".text"):
                    section = ".text"
                    if(Is_traced(traced_section,section)!=True):
                        s_info.s_name=section
                        s_info.addr=0
                        traced_section.append(s_info)
                    else:
                        s_info.addr=traced_s_addr(traced_section,section)
        if(len(token)>0):
            if(section==".data" and token[0]!="section" ):
                s_info.addr,sym_cnt,lit_cnt=parse_data(token,".data",s_info.addr,line_no,sym_cnt,lit_cnt)
                
            elif(section==".bss" and token[0]!="section"):
                s_info.addr,sym_cnt,lit_cnt=parse_data(token,".bss",s_info.addr,line_no,sym_cnt,lit_cnt)
            elif(section==".text" and token[0]!="section"):
                s_info.addr,sym_cnt,lit_cnt=parse_data(token,".text",s_info.addr,line_no,sym_cnt,lit_cnt)
    et.collect_undefined()
    fp.close()
    return True


'''def lst_file(filename,symbol_tab,lit_tab):#8 Oct
    #all lst logic will be inserted here
    inter =open(filename,"r")
    lst = open("p.lst","w")
    et.print_undefined()'''

if __name__ == "__main__":
    if(len(sys.argv)<2):
        print("Error: file name is not inserted !!")
    else:
        l=sys.argv[1].split('.')
        if(len(l)==2):
            if(l[1]=='asm'):
                try:
                    fp = open(sys.argv[1],"r")
                    if (fp):
                        parse_it(fp)
                        p1.intermiddiate(sys.argv[1])
                except:
                    print("Error: file not found !!")
        else:
             print("Error: Invalid File format !!")
            #print(sys.argv[1])
        #fp1=open(sys.argv[2],"w")
        #st.print_symbol_table()
        #lt.print_literal_table()    
        #p1.intermiddiate(sys.argv[1])
        
        #print(et.error)
        #print(et.undefined_label)
