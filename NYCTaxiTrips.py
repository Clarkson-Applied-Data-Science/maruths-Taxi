import csv
import datetime


def ReadCsv():
    fl=open(csvname,'r')
    reader=csv.reader(fl)
    n = 0
    for row in reader:
        if n < 6:
           print (row)
        n+=1
    return (reader)


def question1(data):
    '''Question 1 -
        What datetime range does your data cover?  How many rows are there total '''
    len=0
    n=0
    min_pickup = None
    max_dropoff = None
    for row in data:
        if n >0:
            dto= None
            len+=1
            try:
                dto = datetime.datetime.strptime(row[5],'%Y-%m-%d %H:%M:%S')
                dts = datetime.datetime.strptime(row[6],'%Y-%m-%d %H:%M:%S')
            except Exception as e:
                print (e)
            if dto is not None :
                if min_pickup is None or dto < min_pickup:
                    min_pickup = dto
                if max_dropoff is None or dts > max_dropoff:
                    max_dropoff = dts
        n+=1
    print(f"Number of rows in the dataset:{len}")
    #print(f"Min PickUp date: {min_pickup} ")
    #print(f"Max DropOff date: {max_dropoff} ")
    print(f"Time Range {min_pickup} between {max_dropoff} ")



csvname="trip_data_1.csv"
if __name__ == '__main__':
    #readcsv()
    starttime=datetime.datetime.now()
    Dataset=ReadCsv()
    question1(Dataset)
    endtime=datetime.datetime.now()-starttime
    print(f"{endtime} : Time Taken")