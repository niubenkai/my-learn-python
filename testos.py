import os
def findStr(dir, str, result):
    list = os.listdir(dir)
    for x in list:
        if os.path.isfile(os.path.join(dir,x)):
            i = x.find(str)
            if i != -1:
                result.append(x)
        elif os.path.isdir(os.path.join(dir,x)):
            findStr(os.path.join(dir,x), str, result)
