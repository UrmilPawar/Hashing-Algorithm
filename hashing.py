input='Urmil Pawar'
count={}
position={}
temp=[]
table=[]
sequence='abcdefghijklmnopqrstuvwxyz '

print('The given input is : ',input)
#------------------------------------Counting the occurences---------------------------------------------

input=input.lower()                            #converting the input to lowercase to avoid the conflict of cases
for char in input:             
    if char in count:                          #If char is already present in the map
        count[char] += 1
    else:
        count[char] = 1                        #If char is not present in the map : creating its entry

#-------------------------------------Generating the position table----------------------------------------

size=len(input)                                #the size of the input given by the user

def generate_table(i):                         #the functin that will generate the table of all posible positions a character can take in the input
    #appending element block
    # print(i)                                 #for tracking the progress of calculation
    global temp                                #declaring the temp as global
    append_element=lambda t,i : t+[i]          # not returning the t.append(temp) becauese the operation return 'Nonetype' after appending while we want the appended array in return
    temp=append_element(temp,i)
    # print(temp)
    if temp not in table:                     #since recursion is used there is possiblity of the repetetion
        table.append(temp)                    # Didn't directly used .append(temp)/ instead used lambda function because .append(temp) make updates at same memory location and the previou 'temp' stored in table gets updated, while lambda creates temp at new position every time.
    if i!=size:
        # print('Going to',i+1)
        generate_table(i+1)                   #iterating for next i
        # print('returned to',i)
    
    #remove element block
    remove_element=lambda t: t[:-1:]
    temp=remove_element(temp)
    if temp not in table:
        table.append(temp)
    # print(temp)
    if i!=size:
        # print('Going to',i+1)
        generate_table(i+1)
        # print('returned to',i)
 
generate_table(0)                                #creating th Position table
 #-------------------------------------Calculating the Positions of the characters----------------------------------------
 
for char in count:                                #for every char in count table
    i=0
    p=[]
    for ch in input:                              #for every char in the input
        if char==ch:
             p.append(i)                          #appending all positions of the char in sequence 
        i=i+1
    position[char]=p                              #including the positions of the character in the position table

print('The number of occurence of the characters is : ',count)   
print('The positions of the characters are : ',position)
 
 #---------------------------------Getting and replacing the value of position form the table---------------------------------------- 
            
for char in position:                              #for every charater position sequence in the position map
    p=position[char]        
    value=table.index(p)                           #replacing the position sequence with its's corresponding index in the tabel
    position[char]=value                           

print('The encoded positions of the characters are : ',position)

#------------------------------------------Getting the mod values of the positions----------------------------------------------------------
for char in position:
    p=position[char]
    p=p % 27                                       #Encoding the position with their mod with respect to 27
    position[char]=p

print('The mod encoded positions of the characters are : ',position)

#----------------------------------------Adding the count values with the mod positions----------------------------------------------------
h_values={}                                             
for char in position:                              
    p = position[char]                            #Encoding for the specific position of the character in the input
    c = count[char]                               #Encoding for the number of occurences of the character in the input
    value= p+c                                    #Combining the encoded value 
    h_values[char]=value                          #Soring the hash values of the character that occured in the input

print('The hash values of the present characters are : ',h_values)

#--------------------------------------Generating the Hash Value----------------------------------------------------------
counter=0
HashValue=''

def convert_2digit(num):                          #Function to convert a single digit numbe rot a 2 digit
    if num>=0 and num<=9:
        c='0'+str(num)
    else:
        c=str(num)
    return c

for char in sequence:
    if char in h_values:                          #for character present in the input string
        c = convert_2digit(h_values[char])
        HashValue=HashValue + c
    else:
        c=convert_2digit(counter)                 #for character not present in the input string
        HashValue=HashValue + c
        counter=counter+1

print('The Hash Value is : ',HashValue)
        
