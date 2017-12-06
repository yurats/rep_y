

## индекс множества файлов

def generateindex(fnames):
    index = {}
    for fname in fnames:
        f = open(fname)
        f_line = f.read()
        f_line_list = f_line.split()
