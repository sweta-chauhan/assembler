libCall=['printf','scanf']
libVal = {'printf':0,'scanf':1}

def printf(stack):
    top=stack[0]
    top=top.replace("%d",'{}')
    top=top.strip("\"")
    reg,value = stack[1]
    try:
        print(top.format(value))
    except:
        print("Segmentation fault")

