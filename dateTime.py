import datetime
def dateSubtract(lastDate):
    a = datetime.date.today()
    date_object = datetime.datetime.strptime("{}".format(lastDate), '%Y-%m-%d').date()
    data = str(date_object-a)
    newStr=""
    for i in range(len(data)-10,-1,-1):
        newStr+=data[i]
    return (newStr[::-1])
if __name__ == "__main__":
    print(dateSubtract("2022-11-24"))