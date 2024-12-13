s="hello World From Python"
new={}
for i in s:
    if i.isalpha():
        new[i]=new.get(i,0)+1
print(new)
