theString = "abcdefghijklmnopqrstuvwxyz"

def alphabetString (s):
    # to increment
    strLen = 0
    #these 2 variables give the final answer
    answerStartIndex = 0
    answerStrLen = 0
    
    
    searchDone = False
    #start by looking at beginning letter, see how long a substring can be built 
    #from that letter. keep on updating the answerString by looping through each 
    #letter as start letter.
    
    for i in range(0,len(s)):
        j = i
        strLen = 0
        searchDone = False
       # print "j is %d"%j
       # print (not searchDone) and (j<len(s)-1)
        while (not searchDone) and (j<len(s)-1):
            indexCurrent = theString.index(s[j])
           # print "current letter index is %d"% indexCurrent
            indexNext = theString.index(s[j+1])
           # print "next letter index is %d"% indexNext
            if indexCurrent <= indexNext:
                strLen+=1
               # print "strLen ++ now is %d" % strLen
                j+=1
            else:
                searchDone = True 
       # print "string length is %d"% strLen
       # print "answer string length is %d"% answerStrLen
          
        
        if strLen > answerStrLen:        
            answerStartIndex = i
           # print "answer start at %d" % answerStartIndex
            answerStrLen = strLen+1
           # print "answer is %d long" % answerStrLen
       
        
       # print "loop %d" % j
        
     
   # print "final answer start at %d" % answerStartIndex
    #print "final answer is %d long" % answerStrLen  
    print s[answerStartIndex:answerStartIndex+answerStrLen] 
   
 
            
            
    
    



        
        
        
        
    
        
    