import sys
import literal as lt
import symbol_Table as st
import libCall as lb

reg_list={'eax':0,'ecx':0,'edx':0,'ebx':0,'esp':0,'ebp':0,'esi':0,'edi':0}
reg_code={0:'eax',1:'ecx',2:'edx',3:'ebx',4:'esp',5:'ebp',6:'esi',7:'edi'}

def reverse_mod_rm(inst,rm_byte):
    if(inst==1):
        rm_byte=bin(int(rm_byte,16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if((rm_byte[0:2])=='11'):
            reg_list[reg_code[int(rm_byte[5:8],2)]]+=reg_list[reg_code[int(rm_byte[2:5],2)]]
    if(inst==131):
        #print(rm_byte,rm_byte[0:2])
        num = rm_byte[2:]
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if((rm_byte[0:2])=='11'):
            #print((reg_list[reg_code[int(rm_byte[5:8],2)]]))
            (reg_list[reg_code[int(rm_byte[5:8],2)]])+=int(num,16)

            #print((reg_list[reg_code[int(rm_byte[5:8],2)]]))
    if(inst==139):
        index=  rm_byte[3:-2]
        #print(rm_byte)
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='00'):
            index1=int(st.find_value_by_address(int(index))[4:])-1
            
            reg_list[reg_code[int(rm_byte[2:5],2)]]=int(lt.Literal_Table[index1].rl_value)
    if(inst==137):
        index=  rm_byte[3:-2]
        #print(index)
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='11'):
            reg_list[reg_code[int(rm_byte[5:8],2)]]=reg_list[reg_code[int(rm_byte[2:5],2)]]
    if(inst==3):
        #print(rm_byte[3:-2])
        index = int(rm_byte[3:-2])
        #print(index)
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='00'):
            reg_list[reg_code[int(rm_byte[2:5],2)]]+=int(lt.Literal_Table[int((st.find_value_by_address(index))[4:])-1].rl_value)
            #int(lt.Literal_Table[index].rl_value)
            #print(reg_list,int((st.find_value_by_address(index))[4:])-1)
            #print(lt.Literal_Table[int((st.find_value_by_address(index))[4:])-1].rl_value)
def smaco(objfile):
    ob = open(objfile,"r")
    lt.handle()
    st.handle()
    stack=[]
    lines = ob.readlines()
    for l in lines:
        #print(l)
        inst=int(l[:2],16)
        #print(l[:2],inst)
        if(inst>183 and inst<191):
            reg_list[reg_code[inst-184]]=int(l[2:],16)
            #print(reg_list)
        if(inst==139):
            reverse_mod_rm(inst,l[2:])
        if(inst==1):
            reverse_mod_rm(inst,l[2:])
        if(inst==3):
            #print(l)
            #st.print_symbol_table()
            reverse_mod_rm(inst,l[2:])
        if(inst>79 and inst < 88):
            stack=[(reg_code[inst-80],reg_list[reg_code[inst-80]])]+stack
        if(inst==104):
            stack=[lt.Literal_Table[int((st.find_value_by_address(int(l[3:-2])))[4:])-1].rl_value]+stack
        if(inst==232):
            if(int(l[3:-2],16)==0):
                lb.printf(stack)
        if(inst==131):
            reverse_mod_rm(inst,l[2:])
        if(inst==137):
            reverse_mod_rm(inst,l[2:])
        if(inst==161):
            reg_list['eax']=int(lt.Literal_Table[int((st.find_value_by_address(int(l[3:-2])))[4:])-1].rl_value)
if __name__ =="__main__":
    if(len(sys.argv)==2):
        para=sys.argv[1].split('.')
        if(len(para)==2 and para[1]=="lst" and para[0]=='p'):
            try:
                smaco(sys.argv[1])
            except:
                print("Error :"+" "+sys.argv[1]+" not found !!")
        else:
            print("Error : Invalid file format is provided")
    else:
        print("Invalid number of parameters")
            
