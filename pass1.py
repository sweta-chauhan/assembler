import sys
import os
import re
import charToHex as ch
import literal as lt
import symbol_Table as st
import error_table as et
import opcode_table as ot
import isValid_token as ist
import tokenizer as t
import struct_to_file as stf


def intermiddiate(filename,rfilename):
    if(len(et.error)==0):
        fp = open(filename,"r")
        inter = open(rfilename,'w')
        #print(rfilename.split('.')[0]+'.i')
        lines = fp.readlines()
        for line in lines:
            token=[]
            token=t.fileToToken(line,ot.data_types,token)
            #print(line)
            #print(token)
            if(len(token)==1):
                stf.listTofile(inter,token)
            if(len(token)==2):
               if(token[0]=="section"):
                   stf.listTofile(inter,token)
               elif token[0] in ot.operand_count:
                   stf.listTofile(inter,token)
               else:
                   if(ot.IsRegister(token[1])):
                       token[1]=ot.find_Intermiddiate(token[1])
                       inter.write('\t')
                       stf.listTofile(inter,token)
                   elif(st.search_symtab(token[1])):
                       token[1]= 'Sym#'+str(st.search_index(token[1]))
                       inter.write('\t')
                       stf.listTofile(inter,token)
            elif(len(token)==3):
                if(st.search_symtab(token[0].strip(':')) ):
                    #print(token,token[1])
                    if(ot.IsKeyWord(token[1])):
                        if token[1] in ot.data_types:
                            token[2] = 'Sym#'+str(st.search_index(token[0]))
                            inter.write('\t')
                            stf.listTofile(inter,token)
                        if token[1] in ot.label_specifier:
                            #print(token)
                            token[0] = 'Sym#'+str(st.search_index(token[0].strip(':')))
                            
                            token[2] = 'Sym#'+str(st.search_index(token[2]))
                            inter.write('\t')
                            stf.listTofile(inter,token)
                elif token[0] in ot.operand_count:
                    #print(token)
                    if ot.IsRegister(token[1]):
                        token[1] = ot.find_Intermiddiate(token[1])
                        if ot.IsRegister(token[2]):
                            token[2] = ot.find_Intermiddiate(token[2])
                            inter.write('\t')
                            stf.listTofile(inter,token)
                        elif st.search_symtab(token[2]):
                            #print(token)
                            token[2] = 'Sym#'+str(st.search_index(token[2]))
                            inter.write('\t')
                            stf.listTofile(inter,token)
                        elif(ist.mem_specifier(token[2])):
                            ls = token[2][6:-1]
                            #print(token)
                            ls=list(map(lambda x : x.strip(' '),ls.split('+')))
                            if(st.search_symtab(ls[0])==True and len(ls)==1):
                                token[2]="dword[Sym#"+str(st.search_index(ls[0]))+"]"
                                inter.write('\t')
                                stf.listTofile(inter,token)
                            elif(ot.IsRegister(ls[0])==True and len(ls)==1):
                                token[2]="dword["+ot.find_Intermiddiate(ls[0])+"]"
                                inter.write('\t')
                                stf.listTofile(inter,token)
                            elif(len(ls)==2 and ls[1]!=''):
                                       ls1=list(map(lambda x : x.strip(' '),ls[1].split('*')))
                                       if(len(ls1)==2 and ls1[1]!=''):
                                           if(st.search_symtab(ls[0])==True):
                                               token[2]="dword[Sym#"+str(st.search_index(ls[0]))
                                           if(ot.IsRegister(ls1[0])==True):
                                               token[2]+=","+ot.find_Intermiddiate(ls1[0])+","+"lit#"+str(lt.find_index(int(ls1[1])))+"]"
                                               
                                               stf.listTofile(inter,token)
                                       else:
                                           token[2]="dword[Sym#"+str(st.search_index(ls[0]))+","+ot.find_Intermiddiate(ls1[0])+"]"
                                           inter.write('\t')
                                           stf.listTofile(inter,token)
                                               
                                
                        elif lt.Is_inserted(int(token[2])):
                            token[2] = 'lit#'+str(lt.find_index(int(token[2])))
                            inter.write('\t')
                            stf.listTofile(inter,token)
                        
            elif(len(token)==4):
                if(token[0][-1]==':'):
                    if token[1] in ot.operand_count:
                        if ot.IsRegister(token[2]):
                            token[2] = ot.find_Intermiddiate(token[2])
                            if ot.IsRegister(token[3]):
                                token[3] = ot.find_Intermiddiate(token[3])
                                inter.write('\t')
                                stf.listTofile(inter,token)
                                
                            elif st.search_symtab(token[3]):
                            #print(token)
                                token[3] = 'Sym#'+str(st.search_index(token[3]))
                                inter.write('\t')
                                stf.listTofile(inter,token)
                            elif(ist.mem_specifier(token[3])):
                                ls = token[3][6:-1]
                                #print(token)
                                ls=list(map(lambda x : x.strip(' '),ls.split('+')))
                                if(st.search_symtab(ls[0])==True and len(ls)==1):
                                    token[3]="dword[Sym#"+str(st.search_index(ls[0]))+"]"
                                    inter.write('\t')
                                    stf.listTofile(inter,token)
                                elif(ot.IsRegister(ls[0])==True and len(ls)==1):
                                    token[3]="dword["+ot.find_Intermiddiate(ls[0])+"]"
                                    inter.write('\t')
                                    stf.listTofile(inter,token)
                                elif(len(ls)==2 and ls[1]!=''):
                                    ls1=list(map(lambda x : x.strip(' '),ls[1].split('*')))
                                    if(len(ls1)==2 and ls1[1]!=''):
                                        if(st.search_symtab(ls[0])==True):
                                            token[3]="dword[Sym#"+str(st.search_index(ls[0]))
                                        if(ot.IsRegister(ls1[0])==True):
                                            token[3]+=","+ot.find_Intermiddiate(ls1[0])+","+"lit#"+str(lt.find_index(int(ls1[1])))+"]"
                                               
                                            stf.listTofile(inter,token)
                                    else:
                                        token[3]="dword[Sym#"+str(st.search_index(ls[0]))+","+ot.find_Intermiddiate(ls1[0])+"]"
                                        inter.write('\t')
                                        stf.listTofile(inter,token)
                                               
                                
                            elif lt.Is_inserted(int(token[3])):
                                token[3] = 'lit#'+str(lt.find_index(int(token[3])))
                                inter.write('\t')
                                stf.listTofile(inter,token)
                        
                    
        return True
    else:
        et.print_error(filename)
        os.remove(filename)
    return False
