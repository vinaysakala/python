with open("vinay.txt", "r") as file:
   content = file.read()
   print(content)


with open("vinay.txt", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()

with open("vinay.txt", "a") as file:
   file.write("if you are avalliablel i would like to pick up you")
   print ("Content added Successfully!!")

# try:
#    file = open("viany.txt", "a")
#    file.write("This is an example with exception handling.")
# finally:
#    file.close()
#    print ("File closed successfully!!")


f1 = open('vinay.txt','r')
content=f1.read()
print(content)
f1.close()


with open('test.bin', 'wb') as f:
   data = b"Hello World"
   f.write(data)


with open("vinay.txt", "r+") as fo:
   # Move the read/write pointer to the 10th byte position
   fo.seek(11, 0)

   fo.write('vinay')

   fo.seek(0,0)

    
   # Read 3 bytes from the current position
   data = fo.read(10)
    
   # Print the read data
   print(data)


import os

# current_file = "vinay.txt"

# new_file="gupta.txt"

# os.rename(current_file,new_file)


# os.remove('test.bin')


directory_path = "D:\suvarna\python"

if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")


os.mkdir("test2")
print ("Directory created successfully")

cuurent_dic=os.getcwd()
print(cuurent_dic)


constent=os.listdir(directory_path)
for item in constent:
   print(item)