from CryptoPlus.Cipher import python_AES, AES, python_DES, DES, python_DES3

srec=open("srec.txt", "r")
lines = srec.readlines()
print(lines)
file = open("datasrec.txt", "w")
file.truncate(0)
for i in lines:
    # print(i)
    if i[:2] == "S0":
        print('null')
    if i[:2] == "S5":
        print('null')
    if i[:2] == "S7":
        print('null')
    if i[:2] == "S8":
        print('null')
    if i[:2] == "S9":
        print('Closing srec file read operation')
        file.close()   
    if i[:2] == "S1":
        s = 8
        e = len(i)-3
        data = i[s:e]
        print(data)
        file = open("datasrec.txt", "a+")
        file.write(data)
    if i[:2] == "S2":
        s = 10
        e = len(i)-3
        data = i[s:e]
        print('data')
        file = open("datasrec.txt", "w")
        file.write(data)
    if i[:2] == "S3":
        s = 12
        e = len(i)-3
        data = i[s:e]
        print('data')
        file = open("datasrec.txt", "w")
        file.write(data)

cfile=open("datasrec.txt", "r")
contents=cfile.read()
print(contents)
cfile.close()
key = '2b7e151628aed2a6abf7158809cf4f3c'.decode('hex')
plaintext = contents.decode('hex')
cipher = AES.new(key, AES.MODE_CMAC)
cout = cipher.encrypt(plaintext).encode('hex')
cmacfile = open("datacmac.txt", "w")
cmacfile.write(cout)
cmacfile.close()

