

import os
import datetime
import sys



def main():
    getInput()



def getInput():

    oper = sys.argv[1]

    path = sys.argv[2]

    
    if(oper == "e"):
        encrypt(path)
    elif(oper == "d"):
        decrypt(path)



def encrypt(path):
    start = datetime.datetime.now()
    
    fileFullName = path.split(os.path.sep)  
    fileName =  fileFullName[len(fileFullName) - 1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName) - 1].split(".")[1]

    
    
    

    fileParent = path[0:len(path) - len(fileFullName[len(fileFullName) - 1])]
    newFileName =  "temp_" + fileFullName[len(fileFullName) - 1]
    newFilePath = fileParent + newFileName

    
    
    

    f_read = open(path, "rb")
    f_write = open(newFilePath, "wb")

    count = 0  
	
    list1 = ['84', '131', '178','225','16','63','110','157','204','251','42','89','136','183','230','21']

    
    for now in f_read:  
        for nowByte in now:  
            newByte = nowByte ^ int(list1[count%16])
            count += 1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()
    
    end = datetime.datetime.now()
    os.remove(path)
    os.rename(newFileName,path)
    print("文件加密完毕^_^", (end - start))



def decrypt(path):
    start = datetime.datetime.now()
    fileFullName = path.split(os.path.sep)  
    fileName = fileFullName[len(fileFullName) - 1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName) - 1].split(".")[1]
    fileParent = path[0:len(path) - len(fileFullName[len(fileFullName) - 1])]
    newFileName = "temp_" + fileFullName[len(fileFullName) - 1]
    newFilePath = fileParent + newFileName
    f_read = open(path, "rb")
    f_write = open(newFilePath, "wb")
    count = 0  
    list1 = ['84', '131', '178','225','16','63','110','157','204','251','42','89','136','183','230','21']
    
    for now in f_read:  
        for nowByte in now:  
            newByte = nowByte ^ int(list1[count%16])
            count += 1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()
    end = datetime.datetime.now()
    os.remove(path)
    os.rename(newFileName,path)
    print("文件解密完毕", (end - start))


main()