import csv
import datetime


def ReadCsv():
    fl=open(csvname,'r')
    reader=csv.reader(fl)
    n = 0
  #  for row in reader:
   #     if n < 6:
    #       print (row)
     #   n+=1
    return(reader)


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


def question5(data):
    n =0
    min_plong = 0
    max_plog = 0
    min_plat = 0
    max_plat = 0
    min_dlong = 0
    max_dlong = 0
    min_dlat = 0
    max_dlat = 0
    for row in data:
        if n >0:
            try:
                plong=float(row[10])
                plat=float(row[11])
                dlong=float(row[12])
                dlat = float(row[13])
            except Exception as e:
                print (e)
            if plong < 99 and plong > -99:
                if min_plong == 0 or plong < min_plong:
                    min_plong = plong
                if max_plog == 0 or plong > max_plog:
                    max_plog = plong
            if plat < 99 and plat > -99:
                if min_plat == 0 or plat < min_plat:
                    min_plat = plat
                if max_plat == 0 or plat > max_plat:
                    max_plat = plat
            if dlong < 99 and dlong > -99:
                if min_dlong == 0 or dlong < min_dlong:
                    min_dlong = dlong
                if max_dlong == 0 or dlong > max_dlong:
                    max_dlong = dlong
            if dlat < 99 and dlat > -99:
                if min_dlat == 0 or dlat < min_dlat:
                    min_dlat = dlat
                if max_dlat == 0 or dlat > max_dlat:
                    max_dlat = dlat

        n+=1
    print(f"Min and Max of Pickup_Longitude :{min_plong} and {max_plog} ")
    print(f"Min and Max of Pickup_Latitude :{min_plat} and {max_plat} ")
    print(f"Min and Max of dropoff_Longitude :{min_dlong} and {max_dlong} ")
    print(f"Min and Max of dropoff_Longitude :{min_dlat} and {max_dlat} ")

def question6(data):
    pass


csvname="trip_data_1.csv"
if __name__ == '__main__':
    #readcsv()
    starttime=datetime.datetime.now()
    Dataset=ReadCsv()
    question1(Dataset)
    question5(Dataset)
    question6(Dataset)
    endtime=datetime.datetime.now()-starttime
    print(f"{endtime} : Time Taken")