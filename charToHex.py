
def int_to_hex(string,d_flag):
    str1=""
    int_eq = 0
    l = ""
    if(d_flag=='db'):
        #print(string)
        string = string.split(",")
        if string[0][0]=="\"":
            for i in string[0]:
                if(i!="\""):
                    
                    l=hex(ord(i)).strip('0x')
                    if(len(l)==1):
                        l='0'+l
                    str1+=l
            for j in range(1,len(string)):
                
                l=hex(int(string[j])).strip('0x')
                if l =='':
                    l='00'
                if(len(l)==1):
                    l='0'+l
                str1+=l
                
        else:
            for i in string[:1]:
                print(string)
                l=hex(int(i)).strip('0x')
                if(len(l)==1):
                    l='0'+l
                    str1+=l
    if(d_flag =='dd'):
        string = string.split(",")
        for i in string:
            l=hex(int(i)).strip('0x')
            if l =='':
                l='00'
            if(len(l)==1):
                l='0'+l
            for i in range(8-len(l)):
                l+='0'
            str1+=l
            l=""
    if(d_flag == 'dw'):
        string = string.split(",")
        if string[0][0]=="\"":
            for i in string[0]:
                if(i!="\""):
                    l=hex(ord(i)).strip('0x')
                    if(len(l)==1):
                        l='0'+l
                    for k in range(4-len(l)):
                        l+='0'
                    str1+=l
                    l=""
            for j in range(1,len(string)):
                
                l=hex(int(string[j])).strip('0x')
                if l =='':
                    l='00'
                if(len(l)==1):
                    l='0'+l
                str1+=l
        else:
            for i in string:
                l=hex(int(i)).strip('0x')
                if(len(l)==1):
                    l='0'+l
                str1+=l
    if(d_flag=="resb"):
        l=hex(int(string)).strip('0x')
        if l =='':
            l='00'
        if(len(l)==1):
            l='0'+l
        for i in range(8-len(l)):
            l='0'+l
        str1=l
    if(d_flag=="resw"):
        l=hex(int(string)*2).strip('0x')
        if l =='':
            l='00'
        if(len(l)==1):
            l='0'+l
        for i in range(8-len(l)):
            l='0'+l
        str1=l
    if(d_flag=="resd"):
        l=hex(int(string)*4).strip('0x')
        if l =='':
            l='00'
        if(len(l)==1):
            l='0'+l
        for i in range(8-len(l)):
            l='0'+l
        str1=l
    
    return str1

