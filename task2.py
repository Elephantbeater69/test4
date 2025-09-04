text=input("Enter text to write to the file: ")
with open("output.txt","w") as file:
    file.write(text)
    print("Data successfully written to output.txt")
    file.close()
atext=input("Enter additional text to append to the file: ")
with open("output.txt","a") as file1:
    file1.write("\n" + atext)
    print("Data successfully appended to output.txt")
    file1.close()

file2=open("output.txt","r")
read=file2.read()
print("Final contents of output.txt: \n",read)
file2.close()