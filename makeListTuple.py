# Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
def getListTuple():
    values = input("enter a sequence of numbers : ")
    myList = values.split(",")
    myTuple = tuple(myList)
    print("The list : ", myList)
    print("The tuple : ", myTuple)

if __name__ == "__main__":
    getListTuple()