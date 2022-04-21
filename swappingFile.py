


def swapFileData() :
    FileName  = input("Enter first File Name : ")
    FileName2 = input("Enter second File Name : ")

    with open(FileName , 'r') as a:
        dataA = a.read()

    with open(FileName2 , 'r') as b:
        dataB = b.read()


    with open(FileName , 'w') as a:
        a.write(dataB)

    with open(FileName2 , 'w') as b:
        b.write(dataA)

   

  


swapFileData()

    
