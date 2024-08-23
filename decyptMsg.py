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
    tmp_msg = input("Enter  encrypted message: ")
except:
    print(" You can't type this message, it contain undefined characters ")

print("\n")
print("User Input message: ", tmp_msg, '\n')    

#apptend each character in msg in to  array
tmp_arr = [*str(tmp_msg)]

#print(" tmp message array : ", tmp_arr)
#print("length of tmp_arr: ",len(tmp_arr))

#Decrypting Encrypted message
Y = []
for i in range(len(tmp_arr)):
    for j in range(len(main_arr)):
        if ( tmp_arr[i] ==  main_arr[j] ):
            
            if( j < 3):
                if (main_arr[j] == main_arr[0]): 
                    z =  main_arr[-3]
                    Y.insert(i, z)
                elif(main_arr[j] ==main_arr[1] ):
                    z= main_arr[-2]
                    Y.insert(i, z)
                elif(main_arr[j] == main_arr[2]):
                    z = main_arr[-1]
                    Y.insert(i, z)
            else:
                z = main_arr[j-3]
                Y.insert(i, z)

#print("Decrypted message :", Y)
#print("length of encrypted message: ",len(Y))

print("Decrypted message : ",end='')           
m = 0
k = -2
l = -1
for i in range(1):
    for  j in range(int(len(Y)/2)):     
        a = Y[k+2]
        b = Y[l+2]
        c = a+b
        print(c, end='')
        k = k+2
        l = l+2

print('\n')  