#set up a hashtable, init to all false.


def is_unique(str):
    charSet={}
    for char in str:
        if(charSet.get(char)):
            return False
        charSet[char]=True
    
    return True
    
