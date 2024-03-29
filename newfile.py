import time
print("this program will make new  empty files")
name=input("please enter the name of the files after the name of the files numbers will append\n#>>")
#to make a loop till the user not enter numbers
while True:
   
 num=input("please enter the no files to be created\n#>> ")
 try:
    num2=int(num)
    break
 except:
    print("please enter only numbers")
    continue
last=num
#to load last numbers
file=open("lastnum.txt","w+")
file.write("lastnum is:0")
 
file.close()
lastnum=open("lastnum.txt","r")

lastnum=lastnum.read()
lastnum=lastnum.split(":")

if lastnum[1] !=0:
   
   count=lastnum[1]
   count=int(count)
   num2=num2+count
else:
   count=0
#to make random number of files

for i  in range(count,num2+1):
   i=str(i)
   if i ==0:
      i=None
   lastfile=open(name+i,"w+")
   lastfile.close()
print("thanks for using it")
file=open("lastnum.txt","w+")
file.write("lastnum is:"+last)
 
file.close()
