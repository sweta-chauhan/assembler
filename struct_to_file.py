
def listTofile(fp,lines):
    lines=" ".join(lines)
    fp.writelines(lines)
    fp.write('\n')
    return 0
