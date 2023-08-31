f = open(filename, mode)
#open an existing file for a read operation.
file = open(filename,'r')
#open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
file = open(filename,'w')
#open an existing file for append operation. It won’t override existing data.
file = open(filename,'a')
#To read and write data into the file. The previous data in the file will be overridden.
file = open(filename,'r+')
#To write and read data. It will override existing data.
file = open(filename,'w+')
#To append and read data from the file. It won’t override existing data.
file = open(filename,'a+')

# print every line in a file
for each in file:
    print (each)

# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

 def rename_file(filename, new_filename)
  
def delete_file(filename):
  
import os
 
def create_file(filename):

def search_inventory():

#open file
def main():
    file_name= input("file name: ")
    open_file = open(file_name,'a+')
    file_name.write("file manager")
    file_name.close() 
