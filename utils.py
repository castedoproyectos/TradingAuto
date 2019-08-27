import datetime

def tprint(value):
    actual = datetime.datetime.now()
    prefix_time = str(actual.hour) + ":" + str(actual.minute) + ":" + str(actual.second) + ":" + str(actual.microsecond) 
    prefix_date = str(actual.day) + "/" + str(actual.month) + "/" + str(actual.year)

    prefix = prefix_time + " " + prefix_date
    print(prefix + "\t" + value)