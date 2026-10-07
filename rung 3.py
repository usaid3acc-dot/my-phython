def function(names):
    result=[]
    for i in names:
        i=(i.strip())
        i=(i.lower())
        if i not in result and i!='':
           result.append(i)
    return (result)
data= ['  Zed', '', 'zed', '   ']
print (function(data))
print (data)