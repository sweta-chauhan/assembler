import opcode_table as ot
def fileToToken(line,data_types,list_of_Token):
    token=""
    i=0
    while(line[i]!='\n' and i<len(line)):
        if(line[i]==';'):
            while(line[i]!='\n'):
                i+=1
        elif(line[i]!=' 'and  line[i]!=','):
            token+=line[i]
            i+=1
            if(line[i]==':'):
                token+=line[i]
                i+=1
                list_of_Token.append(token)
                token=""
        
        else:        
            list_of_Token.append(token)
            if(ot.IsKeyWord(token)):
                token=""
                while(line[i]!='\n' and line[i]!=';'):
                    token+=line[i]
                    i+=1
            else:
                token=""
                i+=1
                while(line[i]==' '):
                    i+=1
    #print()
    #if(token[0]==','):
    token=token.strip(',')
    list_of_Token.append(token)
    token=""
    list_of_Token=list(map(str.strip,list_of_Token))
    list_of_Token=[x for x in list_of_Token if len(x)!=0]
    #print(list_of_Token)
    return list_of_Token

def token(line):
    return ((line.strip('\t')).strip('\n')).split(' ')

def opcodeReader(line):
    return ((line.strip('\t')).strip('\n')).split('|')
#print(token('\tmov r32_0 r32_1'))
#print(opcodeReader('B8+rd id|mov|r32|imm32'))
