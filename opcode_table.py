label_specifier={"jmp","jz","je","jle","jnz","loop","call"}
directives  ={"section",".data",".bss",".text"}
mem_specifier={"dword"}
data_types={"db":1,"dd":4,"dw":2,"equ":1,"resb":1,"resw":2,"resd":4}

operand_count={
    "pusha":0,
    "popa":0,
    "inc":1,
    "extern":1,
    "call":1,
    "jmp":1,
    "jz":1,
    "je":1,
    "jnz":1,
    "jle":1,
    "jge":1,
    "global":1,
    "loop":1,
    "dec":1,
    "pop":1,
    "mov":2,
    "mull":2,
    "sub":2,
    "add":2,
    "div":2,
    "xor":2}

zero_operand_opcode={"pusha":"","popa":""}
one_operand_opcode={"inc":"","dec":"",}
two_operand_opcode={"add":"","sub":"","div":"","mov":"","mul":"","xor":""}
def is_operator(token):
    if token in operand_count:
        return True
    return False
def operand_count_of(token):
    if token in operand_count:
        return operand_count[token]
    return -1
def is_label_specifier(token):
    if token in label_specifier:
        return True
    return False
def IsKeyWord(token):
    flag=0
    if token in label_specifier:
        return True
    if token in directives:
        return True
    if token in mem_specifier:
        return True
    if token in data_types:
        return True
    if token in register_dict:
        return True
    return False
def find_size(token):
    if token in data_types:
        return data_types[token]
    
'''register_list = {'al':'01','ax':'02','eax':'03',
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

'''
register_dict = {"eax":"r32_0",
                 'ecx':'r32_1',
                 'edx':'r32_2',
                 'ebx':'r32_3',
                 'esp':'r32_4',
                 'ebp':'r32_5',
                 'esi':'r32_6',
                 'edi':'r32_7'}
register_code = {'0':0b000,
            '1':0b001,
            '2':0b010,
            '3':0b011,
            '4':0b100,
            '5':0b101,
            '6':0b110,
            '7':0b111}


def IsRegister(token):
    if token in register_dict:
        return True
    return False

def find_Intermiddiate(token):#find Intermiddiate code
    try:
        return register_dict[token]
    except:
        return None
def find_regis_opcode(token):#find opcode of register
    try:
        return register_dict[token[-1]]
    except:
        return None

#print(is_label_specifier("jmp"))
print(find_Intermiddiate("hello"))
print(find_Intermiddiate("eax"))
