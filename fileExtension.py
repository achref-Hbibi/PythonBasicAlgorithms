# Python program to accept a filename from the user and print the extension of that.
def getExtension():
    filename = input("enter a file name : ")
    extension = filename.split(".")
    print("The extension of the file : ", extension[-1])

if __name__ == "__main__":
    getExtension()
