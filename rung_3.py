def words_to_dict(text):
    counter={}
    for word in text.split( ):
        word=word.lower()
        if word not in counter:
            counter[word]=1
        else:
            counter[word]=counter[word]+1
    return counter
try :
    with open ("story.txt","r")as e:
        b=e.read()
        b=b.strip()
        if b=="":
             c={}
             print("no words found")
        else:
             c= (words_to_dict(b))

except FileNotFoundError:
    c={}
    print ("no file found please try again")
with open ("word_counts.txt","w") as f:
    for key,value in c.items():
         f.write(key+" "+ (str(value))+"\n")
