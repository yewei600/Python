i =0
count=0
while i < len(s):
    if s[i] == 'b':
       str = s[i:i+3]
       if str == "bob":
          count+=1
    i+=1

print count
            