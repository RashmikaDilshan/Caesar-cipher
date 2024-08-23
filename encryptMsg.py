main_arr = [ 
'.', '?', '"', ' ', '/', ';', ':', '!',
'@', '$', '#', '%', 'a', 'b', 'c', 'd',
'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ',','[',']','(',')','{','}'
]

#User input 
try:
    tmp_msg = input("Enter  your message: ")
except:
    print(" You can't type this message, it contain undefined characters ")

print("\n")
print("Input message: ", tmp_msg, '\n')    

#apptend each character in msg in to  array
tmp_arr = [*str(tmp_msg)]

#print(" tmp message array : ", tmp_arr)
#print("length of tmp_arr: ",len(tmp_arr))

#Encrypting user input message
X = []
for i in range(len(tmp_arr)):
    for j in range(len(main_arr)):
        if ( tmp_arr[i] ==  main_arr[j] ):
           
            if( j > len(main_arr)-4):
                if (main_arr[j] == main_arr[-3]): 
                    y =  main_arr[0]
                    X.insert(i, y)
                elif(main_arr[j] ==main_arr[-2] ):
                    y= main_arr[1]
                    X.insert(i, y)
                elif(main_arr[j] == main_arr[-1]):
                    y = main_arr[2]
                    X.insert(i, y)
            else:
                y = main_arr[j+3]
                X.insert(i, y)

#print("Encrypted message : ",X)
#print("length of encrypted message: ",len(X))

print("Encrypted message : ",end='')           
m = 0
k = -2
l = -1
for i in range(1):
    for  j in range(int(len(X)/2)):     
        a = X[k+2]
        b = X[l+2]
        c = a+b
        print(c, end='')
        k = k+2
        l = l+2

print('\n')            


        

