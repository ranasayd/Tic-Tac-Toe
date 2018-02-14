arr = [100,100,100,100,100,100,100,100,100]
arr1 = []
arr2 = []
arr3 = []
arr4 = []


for i in range ( 0,9,1 ):
    if ( arr[i] == 100 ):
        arr[i]=" "

print('|',arr[0] ,'|',arr[1] ,'|',arr[2] ,'|')
print('-------------')
print('|',arr[3] ,'|',arr[4] ,'|',arr[5] ,'|')
print('-------------')
print('|',arr[6] ,'|',arr[7] ,'|',arr[8] ,'|')



while ( True ):
    n=int(input("entre the position: "))
    x=int(input("entre the value: "))

    while(True):
       if x<1 or x>9:
            print("error")
            x=int(input("entre the value: "))
       else:    
          if x%2==0:
             print("put an odd number")
             x=int(input("entre the value: "))
          else:
             break

    while(True):
        if x in arr2:
            print("error,entre another value")
            x=int(input("enter the value"))
        else:
            break

    #arr2.append(x)
    arr2.append(x)    
    #print(n)
    #print(x)
    arr[n]=x
    #print(arr[n])

    for i in range ( 0,9,1 ):
        if ( arr[i] == 100 ):
            arr[i]=" "
    
    print('|',arr[0] ,'|',arr[1] ,'|',arr[2] ,'|')
    print('-------------')
    print('|',arr[3] ,'|',arr[4] ,'|',arr[5] ,'|')
    print('-------------')
    print('|',arr[6] ,'|',arr[7] ,'|',arr[8] ,'|')

    
    for i in range ( 0,9,1 ):
        if ( arr[i] == 100 ):
            arr[i]=" "

    
    n=int(input("enter the position: "))
    y=int(input("enter the value: "))
    while(True):
        if n<0 or n>8:
            print("error")
            n=int(input("entre the position: "))
        else:
           break
    while(True):
        if n in arr1:
            print("entre the posision")
            n=int(input("entre the position"))
        else:
            break
    arr1.append(n)
    while(True):
        if y<0 or y>8:
            print("error")

        if y<0 or y>8:
            print("error")
            y=int(input("enter the value"))
        else:
            break
    while(True):
         if y%2!=0:
             print("error")
             y=int(input("enter the value: "))
         else:
           break
    while(True):
         if y in arr4:
              print("entre another value")
              y=int(input("entre the value: "))
         else:
             break       
    arr4.append(y)
    #print(n)
    #print(y)
    #arr[n]=y
    #print(arr[n])


    arr[n]=y
    #print(arr[n])

    for i in range ( 0,9,1 ):
        if ( arr[i] == 100 ):
            arr[i]=" "


    print('|',arr[0] ,'|',arr[1] ,'|',arr[2] ,'|')
    print('-------------')
    print('|',arr[3] ,'|',arr[4] ,'|',arr[5] ,'|')
    print('-------------')
    print('|',arr[6] ,'|',arr[7] ,'|',arr[8] ,'|')

    for i in range ( 0,9,1 ):
        if ( arr[i] == " " ):
            arr[i]=100

    if(arr[0]+arr[1]+arr[2]==15):
        print ("you are the winner")
        break
    if (arr[0]+arr[3]+arr[6]==15):
        print ("you are winner")
        break
    if (arr[1]+arr[4]+arr[7]==15):
        print ("you are winner")
        break
    if (arr[3]+arr[4]+arr[5]==15):
        print ("you are winner")
        break
    if (arr[2]+arr[5]+arr[8]==15):
        print ("you are winner")
        break
    if(arr[6]+arr[7]+arr[8]==15):
        print ("you are winner")
        break
    if (arr[0]+arr[4]+arr[8]==15):
        print ("you are winner")
        break
    if (arr[2]+arr[4]+arr[6]==15):
        print ("you are winner")
        break
