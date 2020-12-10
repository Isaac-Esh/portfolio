#Ike Esh

'''
HammingEncode(string) takes a string as its input, turns it into binary, uses a Hamming code to encode it,
and returns a string of binary.
HamminngDecode(binary) takes a string of binary as its input, decodes it using a Hamming code, turns the binary
stringinto text and returns that string.
rsEncode(string) takes a string as its input, turns it into binary, uses a REed Soloman code to encode it,
and returns a string of binary.
rsDecode(binary) takes a string of binary as its input, decodes it using a Reed Soloman code, turns the
binary string into text and returns that string.
interference(binary, n) takes a string of binary and randomly adds n errors to it, then returns the binary string
with the errors.
The other functions are used by these five functions and you don't need to use them.

Running this code should show the two test codes
In test 1, only one bit is flipped, so both codes output the original message. Using a Hamming code to encode this
gives a much shorter string of binary than using a Reed Soloman code, so in this case a Hamming Code is more
efficient. 
In test 2, 5 errors are added. The Reed Soloman code still outputs the original message, but the Hamming code will
usually output a message with errors. The Hamming codes use a Hamming(16,11) code on chunks of 16 bits, and the
total length of the binary string is 80 bits, so it is possible that all of the errors will be in separate chunks
the Hamming code will output the original message, but this is unlikely. In this case it is better to use the Reed
Soloman codes because that will guarentee that the output will be unchanged by the interference.
Hamming codes will be better to use when errors are unlikely because they will use a much shorter string of bits
than Reed Soloman codes. Reed Soloman codes will be better to use when errors are more common because they can
correct a set number of errors regardless of where the errors occur. Reed Soloman codes can also be adjusted to
be able to correct a certain number of errors. Hamming codes will work fine as long as there is only one error
in each chunk of bits that has a Hamming code on it, so if you know every error will be a certian distance apart
using a Hamming code will be fine. If errors are grouped together then Hamming codes will not be able to correct
the errors. Reed Soloman codes will work if errors are grouped together, so if you know that errors will come near
other errors, it is better to use Reed Soloman codes.
'''

import random 
def decodedraft(lyst):
    a=0
    b=0
    c=0
    d=0
    e=0
    z=0
    for i in range(0, 16):  #overall parity check, 0 means no error
        a=(a+lyst[i])%2
    for i in range(1, 16, 2):  #first parity check, 0 means no error
        b=(b+lyst[i])%2
    for i in range(0, 16):  #second parity check, 0 means no error
        if (i%4 ==2) or (i%4 == 3):
            c=(c+lyst[i])%2
    for i in range(0, 16):  #third parity check, 0 means no error
        if (i%8 > 3):
            d=(d+lyst[i])%2
    for i in range(8, 16):  #fourth parity check, 0 means no error
        e=(e+lyst[i])%2
        
    for i in range(0, 16):
        z=(i*lyst[i])^a

    if (a == 0) and ((b == 1)or(c == 1)or(d == 1)or(e == 1)): #two errors
        #print('There are two errors.')
        return (str(lyst[3])+str(lyst[5])+str(lyst[6])+str(lyst[7])+str(lyst[9])+str(lyst[10])+str(lyst[11])+str(lyst[12])+str(lyst[13])+str(lyst[14])+str(lyst[15]))
    elif(a == 0) and ((b == 0)and(c == 0)and(d == 0)and(e == 0)):#no errors
        #print("There are no errors.")
        return (str(lyst[3])+str(lyst[5])+str(lyst[6])+str(lyst[7])+str(lyst[9])+str(lyst[10])+str(lyst[11])+str(lyst[12])+str(lyst[13])+str(lyst[14])+str(lyst[15]))
    else: #one error
        wrong = b+2*c+4*d+8*e
        lyst[wrong]= (lyst[wrong]+1)%2
        return (str(lyst[3])+str(lyst[5])+str(lyst[6])+str(lyst[7])+str(lyst[9])+str(lyst[10])+str(lyst[11])+str(lyst[12])+str(lyst[13])+str(lyst[14])+str(lyst[15]))

def encodedraft(lyst):
    b=(lyst[0]+lyst[1]+lyst[3]+lyst[4]+lyst[6]+lyst[8]+lyst[10])%2
    c=(lyst[0]+lyst[2]+lyst[3]+lyst[5]+lyst[6]+lyst[9]+lyst[10])%2
    d=(lyst[1]+lyst[2]+lyst[3]+lyst[7]+lyst[8]+lyst[9]+lyst[10])%2
    e=(lyst[4]+lyst[5]+lyst[6]+lyst[7]+lyst[8]+lyst[9]+lyst[10])%2
    a=(b+c+d+e+lyst[0]+lyst[1]+lyst[2]+lyst[3]+lyst[4]+lyst[5]+lyst[6]+lyst[7]+lyst[8]+lyst[9]+lyst[10])%2
    string=str(a)+str(b)+str(c)+str(lyst[0])+str(d)+str(lyst[1])+str(lyst[2])+str(lyst[3])+str(e)+str(lyst[4])+str(lyst[5])+str(lyst[6])+str(lyst[7])+str(lyst[8])+str(lyst[9])+str(lyst[10])
    return string
    
def stringtolist(string):
    lyst = []
    for i in range(0, len(string)):
        lyst+=[int(string[i])]
    return lyst

def encodedraft2(string):
    return(encodedraft(stringtolist(string)))
def decodedraft2(string):
    return(decodedraft(stringtolist(string)))

def stringToBinary(string):
    end = ''
    for i in string:
        num=ord(i)
        bin1 = bin(num)
        bin2 = bin1[2:-1]+bin1[-1]
        L = len(bin2)
        bin3 = ('0'*(7-L))+bin2    #should be a 7 digit binary number.
        end+=bin3
    return end

def intToBinary(x):
    end = ''
    bin1 = bin(x)
    bin2 = bin1[2:-1]+bin1[-1]
    L = len(bin2)
    bin3 = ('0'*(8-L))+bin2    #should be a 8 digit binary number.
    return bin3

def binToInt(string): #takes an 8 digit binary string
    end=0
    for i in range(8):
        #print(i)
        #print(string[7-i])
        #print(2**i)
        #print()
        end+=int(string[7-i])*(2**i)
    return end
    


def HammingEncode(string):
    binary = stringToBinary(string)
    L = len(binary)
    if L%11 != 0:
        extra = 11-L%11
        binary = binary + '0'*extra
    n = len(binary)//11
    encoded = ''
    x1 = 0
    x2=11
    for i in range(n):
        encoded+=encodedraft2(binary[x1:x2])
        x1+=11
        x2+=11
    return encoded
        
def HammingDecode(string): #string has a length divisible by 16
    n=len(string)//16
    decoded = ''
    x1=0
    x2=16
    for i in range(n):
        decoded+=decodedraft2(string[x1:x2])
        x1+=16
        x2+=16
    #take off ending 0s
    wantedLength = len(decoded)-(len(decoded)%7)
    decoded = decoded[0:wantedLength]
    n=len(decoded)//7
    end = ''
    x3=0
    x4=7
    for i in range(n):
        b = decoded[x3:x4]
        x3+=7
        x4+=7
        num = 64*int(b[0])+32*int(b[1])+16*int(b[2])+8*int(b[3])+4*int(b[4])+2*int(b[5])+1*int(b[6])
        if num >0:
            end+=chr(num)
    return end


from reedsolo import RSCodec
rsc=RSCodec(2)

def rsEncode(string):
    bString=bytes(string, 'utf-8')
    msg=rsc.encode(bString)
    encoded=''
    for i in msg:
        encoded+=intToBinary(i)
        #print(chr(i))
    return encoded

        
def rsDecode(string): #string should have a length divisible by 8
    L=len(string)
    n=L//8
    encoded=[]
    for i in range(n):
        x=string[8*i:8*(i+1)]
        intX=binToInt(x)
        #print(intX)
        encoded+=[intX]
    #print(encoded)
    decoded = rsc.decode(encoded)
    byteArray = decoded[0]
    endString=str(byteArray)
    end=endString[12:-2]
    return end
    
def interference(string, errors):
    if errors > len(string):
        errors = len(string)
    if errors<0:
        errors = 0
    numlyst=[]
    for i in range(len(string)):
        numlyst+=[i]
    newList=[]
    for i in range(errors):
        a=random.randint(0, len(numlyst)-1)
        #print(a)
        b=numlyst.pop(a)
        newList+=[b]
    #print(newList)
    for i in newList:
        if string[i] == '1':
            y='0'
        if string[i] == '0':
            y='1'
        string=string[0:i]+y+string[i+1:len(string)]
    return string
    
    
print('Test 1')
ex1a=HammingEncode('Message')
ex1b=rsEncode('Message')
print('Hamming Encoded String:')
print(ex1a)
print('Reed Soloman Encoded String:') 
print(ex1b)
print('Hamming Encoded String After 1 Error:')
ex1c = (interference(ex1a, 1))
print(ex1c)
print('Reed Soloman Encoded String After 1 Error:') 
ex1d = (interference(ex1b, 1))
print(ex1d)
ex1e = HammingDecode(ex1c)
ex1f = rsDecode(ex1d)
print('Hamming Decoded Message:')
print(ex1e)
print('Reed Soloman Decoded Message:') 
print(ex1f)
print()
print('Test 2')
ex2a=HammingEncode('Message')
ex2b=rsEncode('Message')
print('Hamming Encoded String:')
print(ex2a)
print('Reed Soloman Encoded String:') 
print(ex2b)
print('Hamming Encoded String After 5 Errors:')
ex2c = (interference(ex2a, 5))
print(ex2c)
print('Reed Soloman Encoded String After 5 Errors:') 
ex2d = (interference(ex2b, 5))
print(ex2d)
ex2e = HammingDecode(ex2c)
ex2f = rsDecode(ex2d)
print('Hamming Decoded Message:')
print(ex2e)
print('Reed Soloman Decoded Message:') 
print(ex2f)



