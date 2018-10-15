import re

def Isvalid_naming(string):
    return bool(re.match(r'\D',string))
def mem_specifier(token):
    return (bool(re.match(r'dword[\D$]',token)))
