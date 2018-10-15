register_list = {'al':'01','ax':'02','eax':'03',
                 'cl':'11','cx':'12','ecx':'13',
                 'dl':'21','dx':'22','edx':'23',
                 'bl':'31','bx':'32','ebx':'33',
                 'ah':'41','sp':'42','esp':'43',
                 'ch':'51','bp':'52','ebp':'53',
                 'dh':'61','si':'62','esi':'63',
                 'bh':'71','di':'72','edi':'73'}

register_dict = {0:['r8_0','r16_0','r32_0'],
                 1:['r8_1','r16_1','r32_1'],
                 2:['r8_2','r16_2','r32_2'],
                 3:['r8_3','r16_3','r32_3'],
                 4:['r8_4','r16_4','r32_4'],
                 5:['r8_5','r16_5','r32_5'],
                 6:['r8_6','r16_6','r32_6'],
                 7:['r8_7','r16_7','r32_7']}


register = {'0':0b000,
            '1':0b001,
            '2':0b010,
            '3':0b011,
            '4':0b100,
            '5':0b101,
            '6':0b110,
            '7':0b111}


def IsRegister(register_list,token):
    for i in register_list:
        if i== token:
            return True
    return False

def find_key(register_list,token):
    for i in  register_list:
        if i== token:
            
            l = (register_list[i])
            return int(l[0]),int(l[1])
    return -1,-1

def find_Interm(register_dict,key,index):
    return register_dict[key][index]
def find_opcode(register,token):
    return register[token[-1]]

