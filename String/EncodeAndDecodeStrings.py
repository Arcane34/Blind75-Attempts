# https://neetcode.io/problems/string-encode-and-decode?list=blind75
#FINISHED

def encode(strs):
    newstr = ""
    for i in strs:
        print(i, "hey")
        newstr+= i
        newstr += "@@@"
    
    if len(newstr) != 3:
        newstr = newstr[0:-3]
    
    return(newstr)

def decode(s: str):
    if s == "":
        return []
    elif s == "@@@":
        return [""]
    return s.split("@@@")




encStr = encode(["lalala", "djsdj", "new", "love sdj"])