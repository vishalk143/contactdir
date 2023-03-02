'''
main file
===========
'''

def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
    
    fp=open('data.txt','a')
    n=input("enter name:")
    mn=input("enter mobile number:")
    res=validate_mob(mn)
    #print(res)
    if res==1:
        a,b=search_mob(mn)
        if b==1:
            print("Number Already Exist")
        else:
            
            d=n+":"+mn+"\n"
            fp.write(d)
            fp.close()
            print("contact created successfully!!")
    else:
        print("please enter valid mobile number!!")



def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("==========contact directory============")
    print()
    print(d)
    print("=====================================")

def search_name():
    print("search contact number by name")
    ns=input("Enter name:")
    fp=open('data.txt','r')
    data=fp.readlines()
    #print(data)
    for x in data:        
        #print(x)
        l=x.split(":")
        #print(l)
        #print(l[0])
        if ns.upper()==l[0].upper():                            
            print(x)
            flag=1
        if flag==0:        
            print("contact not found")
        fp.close()
    


def search_mob(n):
        
        fp=open('data.txt','r')
        data=fp.readlines()
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("contact found")
                #print(x)
                return x,1
            
        else:
                return '',0
    


    
print("welcome to contact directory console application:")
print()
while True:
    print("1.create contact")
    print("2.view contact")
    print("3.search by name")
    print("4.search by mobile number")
    print("5.Exit")
    ch=int(input("Enter your choise:"))

    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        search_name()
        
    elif ch==4:
        ms=input("Enter Mobile Number To Be Serached:")
        
        a,b=search_mob(ms)
        #print(a)
        #print(b)
        if b==1:
            print("Number Found:")
            print(a)
        else:
            print("NOT FOUND:")
            

            
    elif ch==5:
        break
    else:
        print("please enter valid option!!!")

else:
    print("thank you for using application")
