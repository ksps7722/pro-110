import random
response=input("press y to roll again and n to exit:")
print("/n")
##reponse="y"
while response=="y":
    num=random.randint(1,6)
    if num==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if num==2:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")
    if num==3:
        print("[-----]")
        print("[     ]")
        print("[ 000 ]")
        print("[     ]")
        print("[-----]")
    if num==4:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
    if num==5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if num==6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")


    
       
