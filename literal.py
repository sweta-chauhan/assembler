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
