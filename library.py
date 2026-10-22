catalog={}
def add_checker(catalog):
    title=input("what book you want to add")
    title=title.strip()
    title=title.lower()
    if title not in catalog and title!="":
        catalog[title]="on shelf"
    else:
        print ("it is refused")
    return catalog
def lend_checker(catalog):
    title_2=input("which book you want to lend")
    title_2=title_2.strip()
    title_2=title_2.lower()
    if title_2 in catalog and catalog[title_2]=="on shelf":
        name=input("whats your name")
        name=name.strip()
        name=name.lower()
        if name!="" and name!="on shelf":
            catalog[title_2]=name
        else:
            print ("name is not correct")
    else:
        print ("it is refused")
    return catalog
def return_checker(catalog):
    title_3=input("which book you want to return")
    title_3=title_3.strip()
    title_3=title_3.lower()
    if title_3 in catalog and catalog[title_3]!="on shelf":
        catalog[title_3]="on shelf"
    else:
        print("it is refused")
    return catalog
def catalog_checker(catalog):
    shelf_counter=0
    for key, value in catalog.items():
        if value=="on shelf":
            shelf_counter=shelf_counter+1
        else:
            print (key,"is with",value)
    print("on shelf:", shelf_counter)
while True:
    command=input("choose add,lend,return,list or quit").strip().lower()
    if command=="quit":
        break
    elif command=="add":
        add_checker(catalog)
    elif command=="lend":
        lend_checker(catalog)
    elif command=="return":
        return_checker(catalog)
    elif command=="list":
        catalog_checker(catalog)
    else:
        print ("unknown command")