


def showBooks():
    j=1
    for i in books:
        print(f"{j}.{i}")
        j+=1




def issueBook(username,Bookname):
    if(books.count(Bookname)==0):
        if(issued.get(Bookname)):
            print(f"soory book is not available issued by {issued.get(Bookname)}")
        else:
            print("soory book is not availble in the libraray yet")    
    else:
        books.remove(Bookname)
        issued[Bookname]=username
        print("book issued")


    


    
    


def returnBook(username,Bookname):
    temp=issued.get(Bookname)
    if(temp==username):
        issued.pop(Bookname)
        books.append(Bookname)
        print("book returned")
        
    else:
        print("you havent issued any book yet")    


def addBook(username,Bookname,passw):
    _passward="ayush65"
    if(_passward==passw):
        print(f"welcome {username} which book you want to add")
        books.append(Bookname)
        print("book added")
    else:
        print("wrong password")    
       










books=["c","java","python","ruby","angular"]
users={79:"ayush",999:"Anish",88:"Ravi",55:"Rahul"}
issued={}




while(True):
    print("welcome to ayush library")
    username=input("enter you name:")
    id=int(input("enter your id:"))


    if(not users.get(id)):
       print("you havent gegestired to our library")
       agree=int(input("enter 1 for register and 0 for exit"))
       if(agree==1):
           users[id]=username
       else:
           break
    print("choose the following options")
    print("1:showBooks\n2.issuebook\n3.ReturnBook\n4.AddBook\n5.exit")
    choice=int(input())
    if(choice==1):
        print("\n")
        showBooks()
        
    elif(choice==2):
        Bookname=input("enter bookname:")
        issueBook(username,Bookname)
    elif(choice==3):
        Bookname=input("enter bookname:")
        returnBook(username,Bookname)
    elif(choice==4):
        passwd=(input("enter passwrd:"))
        Bookname=input("enter bookname:")
        addBook(username,Bookname,passwd)    
    elif(choice==5):
        print("Thankyou for visiting our library")   
        break   
    else:
        print("wrong choice")    
    print("\n\n")     



        


     
    