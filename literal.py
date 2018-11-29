class Literal_info():
    def __init__(self):
        self.f_line=0
        self.rl_value=None
        self.hex_value=None

Literal_Table = []

def insert_Into_Literal(Lt_info):
    Literal_Table.append(Lt_info)

def search_lit(index):
    return Literal_Table[index].hex_value

def Is_inserted(value):
    for i in Literal_Table:
        if i.rl_value == value:
            return True
    return False
def find_index(real_value):
    for i in Literal_Table:
        if i.rl_value == real_value:
            return i.f_line
    return -1
def print_literal_table():
    print("**********************************************************************Literal Table**************************************************".center(50))
    print("Index".ljust(10),"Real Value".ljust(70),"Hex Value".ljust(90))
    for i in Literal_Table:
        print(str(i.f_line).ljust(10),str(i.rl_value).ljust(70),(i.hex_value).ljust(90))
        
def literal_to_file(fp):
    for i in Literal_Table:
        fp.write(str(i.f_line)+"|"+str(i.rl_value)+"|"+i.hex_value+'\n')

def file_to_symbol(lines,start,end):
    #lines = fp.readlines()
    for line in lines[start:end]:
        lt=Literal_info()
        line = line.split('|')
        lt.f_line=int(line[0])
        lt.rl_value=(line[1])
        lt.hex_value = (line[2])
        Literal_Table.append(lt)
    
'''if __name__=="__main__":
    handle()
    print_literal_table()
'''
