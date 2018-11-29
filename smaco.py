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
        num = rm_byte[2:]
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if((rm_byte[0:2])=='11'):
            (reg_list[reg_code[int(rm_byte[5:8],2)]])+=int(num,16)
    if(inst==139):
        index=  rm_byte[3:-2]
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='00'):
            index1=int(st.find_value_by_address(int(index))[4:])-1
            reg_list[reg_code[int(rm_byte[2:5],2)]]=int(lt.Literal_Table[index1].rl_value)
    if(inst==137):
        index=  rm_byte[3:-2]
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='11'):
            reg_list[reg_code[int(rm_byte[5:8],2)]]=reg_list[reg_code[int(rm_byte[2:5],2)]]
    if(inst==3):
        index = int(rm_byte[3:-2])
        rm_byte=bin(int(rm_byte[0:2],16))[2:]
        if(len(rm_byte)<8):
            for i in range(8-len(rm_byte)):
                rm_byte='0'+rm_byte
        if(rm_byte[0:2]=='00'):
            reg_list[reg_code[int(rm_byte[2:5],2)]]+=int(lt.Literal_Table[int((st.find_value_by_address(index))[4:])-1].rl_value)
            
def smaco(objfile):
    ob = open(objfile,"r")
    main = 0
    stack=[]
    lines = ob.readlines()
    syn_size = int(lines[1].strip('\n'))
    lit_size = int(lines[2].strip('\n'))
    filename = lines[0].strip('\n')
    lt.file_to_symbol(lines,syn_size+3,lit_size+syn_size+3)
    st.file_to_symbol(lines,3,syn_size+3)
    main = st.is_defined("main")
    if(main):
        for l in lines[syn_size+lit_size+3:]:
            inst=int(l[:2],16)
            if(inst>183 and inst<191):
                reg_list[reg_code[inst-184]]=int(l[2:],16)
            if(inst==139):
                reverse_mod_rm(inst,l[2:])
            if(inst==1):
                reverse_mod_rm(inst,l[2:])
            if(inst==3):
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
    else:
        print("Alert : No Reference to < main >")
        
if __name__ =="__main__":
    if(len(sys.argv)==2):
        para=sys.argv[1].split('.')
        if(len(para)==2 and para[1]=="o"):
            try:
                smaco(sys.argv[1])
            except:
                print("Error :"+" "+sys.argv[1]+" not found !!")
        else:
            print("Error : Invalid file format is provided")
    else:
        print("Invalid number of parameters")
            
