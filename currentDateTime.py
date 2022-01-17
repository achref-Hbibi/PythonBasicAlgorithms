import datetime


def getDateTime():
    now = datetime.datetime.now()
    print("The current date : ", now.strftime("%Y-%m-%d"))
    print("The current time : ", now.strftime("%H:%M:%S"))


if __name__ == "__main__":
    getDateTime()
