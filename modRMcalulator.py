import re
import opcode_table as ot

def modRMcalulator(operand1,operand2):
    result=""
    if bool(re.match(r'^r',operand1)):
        if bool(re.match(r'^r',operand2)):
            result=hex(int('11'+ot.register_code[operand2[-1]]+ot.register_code[operand1[-1]],2))
            #print(operand1,operand2,result)
        elif bool(re.match(r'^d',operand2)):
            result=hex(int('00'+ot.register_code[operand1[-1]]+'101',2))#.strip('0x')
            if(len(result)<4):
                result=result[0:2]+'0'+result[2:]
        elif bool(re.match(r'^l',operand2)):
            result = hex(int('11'+'000'+ot.register_code[operand1[-1]],2))
    return result

def isModRM(inst_format):
    return (inst_format[-1]=='r')

