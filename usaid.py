shopping_list=[]
while True:
    select= int(input("1 for add item , 2 to veiw the list , 3 for exit"))
    if select==1:
        shopping_list.append(input(""))
    elif select==2:
        print (shopping_list)
    elif select==3:
        break
print ("all done")

    
    