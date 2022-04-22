import datetime
def getdate():
    return datetime.datetime.now()

def take(k):
    if k==1:
       print("1.Worlout","2.Food")
       c=int(input())
       if c==1:
         value=input("Type Here\n")
         with open("mahi-w.txt","a")as o:
             o.write(str(str(getdate()))+ ":"+ value)
             print("Sucessfully submited")
       elif c==2:
           value = input("Type Here\n")
           with open("mahi-f.txt", "a") as o:
               o.write(str(str(getdate()))+ ":"+ value)
               print("Sucessfully submited")
    elif k==2:
        print("1.Worlout", "2.Food")
        c = int(input())
        if c == 1:
            value = input("Type Here\n")
            with open("rajesh-w.txt", "a") as o:
                o.write(str(str(getdate()))+ ":"+ value)
                print("Sucessfully submited")
        elif c == 2:
            value = input("Type Here\n")
            with open("rajesh-f.txt", "a") as o:
                o.write(str(str(getdate()))+ ":"+ value)
                print("Sucessfully submited")
    elif k==3:
        print("1.Worlout", "2.Food")
        c = int(input())
        if c == 1:
            value = input("Type Here\n")
            with open("nitish-w.txt", "a") as o:
                o.write(str(str(getdate()))+ ":"+ value)
                print("Sucessfully submited")
        elif c == 2:
            value = input("Type Here\n")
            with open("nitish-f.txt", "a") as o:
                o.write(str(str(getdate()))+ ":"+ value)
                print("Sucessfully submited")
def ret(k):
    if k==1:
       print("1.Worlout","2.Food")
       c=int(input())
       if c==1:
         with open("mahi-w.txt")as o:
             for i in o:
                 print(i,end="")
       elif c==2:
           with open("mahi-f.txt") as o:
               for i in o:
                   print(i, end="")

    elif k==2:
        print("1.Worlout", "2.Food")
        c = int(input())
        if c == 1:
           with open("rajesh-w.txt") as o:
             for i in o:
                print(i, end="")

        elif c == 2:
           with open("rajesh-f.txt") as o:
             for i in o:
                 print(i, end="")

    elif k==3:
        print("1.Worlout", "2.Food")
        c = int(input())
        if c == 1:
            with open("najesh-w.txt") as o:
               for i in o:
                  print(i, end="")
        elif c==2:
            with open("najesh-w.txt")as o:
                for i in o:
                    print(i,end="")



print("Welcome To Mahendra Gym")
print("1.Log The data")
print("2.Read the Data")
a=int(input())
if a==1:
    print("1.Mahi")
    print("2.Rajesh")
    print("3.Nitish")
    b=int(input())
    take(b)
elif a==2:
    print("1.Mahi")
    print("2.Rajesh")
    print("3.Nitish")
    b = int(input())
    ret(b)
