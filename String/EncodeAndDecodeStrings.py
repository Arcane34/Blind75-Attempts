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



# ACTUAL SOLUTION
# Write the list of sizes for each string at the end of the string in a readable format such that you can use it to get the array of strings back when you need to
# Placing it at the end means you will always know where your list of ints are, as your delimeter will be unique and cannot be messed with since you encode the
# text yourself

def encode(self, strs: List[str]) -> str:
    if not strs:
        return ""
    sizes, res = [], ""
    for s in strs:
        sizes.append(len(s))
    for sz in sizes:
        res += str(sz)
        res += ','
    res += '#'
    for s in strs:
        res += s
    return res

def decode(self, s: str) -> List[str]:
    if not s:
        return []
    sizes, res, i = [], [], 0
    while s[i] != '#':
        cur = ""
        while s[i] != ',':
            cur += s[i]
            i += 1
        sizes.append(int(cur))
        i += 1
    i += 1
    for sz in sizes:
        res.append(s[i:i + sz])
        i += sz
    return res


encStr = encode(["lalala", "djsdj", "new", "love sdj"])