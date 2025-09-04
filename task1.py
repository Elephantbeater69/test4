try:
    file1=open('sample.txt','r')
    readline1=file1.readlines(1)
    readline2=file1.readlines(2)
    print("Reading file content: ")
    print("Line 1: ",readline1)
    print("Line 2: ",readline2)
    file1.close()
except FileNotFoundError:
    print("Error: File \'sample.txt\' not found.")

