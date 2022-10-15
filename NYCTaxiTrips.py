import csv
import datetime
from math import radians, cos, sin, asin, sqrt


def ReadCsv():
    fl=open(csvname,'r')
    reader=csv.reader(fl)
    n = 0
    for row in reader:
       if n < 6:
           print (row)
       n+=1
    #return(reader)


def question1():
    fl = open(csvname, 'r')
    data = csv.reader(fl)
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


def question5():
    fl = open(csvname, 'r')
    data = csv.reader(fl)
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

def question6():
    fl = open(csvname, 'r')
    data = csv.reader(fl)
    outputlist=[]
    n = 0
    for row in data:
        if n >0:
            try:
                plong = float(row[10])
                plat = float(row[11])
                dlong = float(row[12])
                dlat = float(row[13])
            except Exception as e:
                print (e)
            plong, plat, dlong, dlat = map(radians, [plong, plat, dlong, dlat])
            if plong < 99 and plong > -99:
                dlon = dlong - plong
                dlat = dlat - plat
                a = sin(dlat / 2) ** 2 + cos(plat) * cos(dlat) * sin(dlon / 2) ** 2
                print(a)
                c = 2 * asin(sqrt(a))
                r = 6371
                out=c*r
                outputlist.append[out]
        n=+1
    print (outputlist)

def question7():

    distinctdict={}
    header = ['vendor_id','rate_code','store_and_fwd_flag','passenger_count']

    i=0
    for H in header:
        print(H)
        if H == 'vendor_id':
            index = 2
        elif H == 'rate_code':
            index = 3
        elif H == 'store_and_fwd_flag':
            index = 4
        elif H == 'passenger_count':
            index = 7

        fl = open(csvname, 'r')
        data = csv.reader(fl)
        distinctValues = []
        n = 0
        for row in data:
            if n > 0:
                #print(index)
                H_value = row[index]
                if H_value not in distinctValues:
                    distinctValues.append(H_value)
            n+=1
        distinctdict[H] = distinctValues

    print(distinctdict)

def question8():
    header = ['passenger_count', 'trip_time_in_secs', 'trip_distance']
    #, 'trip_time_in_secs', 'trip_distance'
    for H in header:
        print (H)
        if H == 'passenger_count':
            index = 7
        elif H == 'trip_time_in_secs':
            index = 8
        elif H == 'trip_distance':
            index = 9
        fl = open(csvname, 'r')
        data = csv.reader(fl)
        n = 0
        min_h=0
        max_h=0
        dict={}
        distinctValues={}
        for row in data:
            if n > 0:
                H_value = float(row[index])
                if min_h == 0 and min_h > H_value:
                    min_h = H_value
                    #dict['min']=min_h
                if max_h == 0 and max_h < H_value:
                    max_h = H_value
                    #dict['max'] = max_h
            n+=1
            dict['min'] = min_h
            dict['max'] = max_h
        distinctValues[H] = dict
        print (distinctValues)

def question9():
    fl = open("split_file_14776.csv", 'r')
    data = csv.reader(fl)
    hrs=[]
    n =0
    fdict={}
    for row in data:
        if n > 0:
            d = datetime.datetime.strptime(row[5],'%Y-%m-%d %H:%M:%S')
            hour = str(d.time())[0:2]
            if hour not in hrs:
                hrs.append(hour)
        n+=1
    print(hrs)
    for h in hrs:
        print(h)
        fl = open(csvname, 'r')
        data = csv.reader(fl)
        n=0
        cnt=0
        passsum=0
        for row in data:
            if n > 0:
                d = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
                hour = str(d.time())[0:2]
                if hour == h:
                    cnt+=1
                    passcnt = int(row[7])
                    passsum = passsum + passcnt
            n+=1
        passavg = passsum / cnt
        fdict[h]=passavg
        print(fdict)
    print (fdict)

def question10():
    fl = open(csvname, 'r')
    data = csv.reader(fl)
    n=0
    linecnt=0
    filecnt=1
    tmpdata=[]
    for row in data:
        if n == 0:
            header = row
            print (header)
        elif n > 0:
            fname = (f"split_file_{filecnt}.csv")
            tmpdata.append(row)
            linecnt += 1
            #print(linecnt)
            if linecnt == 1000:
                #print(linecnt)
                writetocsv(tmpdata, fname,header)
                filecnt +=1
                fname = (f"split_file_{filecnt}")
                linecnt=0
                tmpdata=[]
            #fname=(f"split_file_{filecnt}")
        n+=1

def writetocsv(wdata,fname,header):
    with open(fname, 'w', encoding='UTF8', newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow(header)
        writer.writerows(wdata)



csvname="trip_data_1.csv"
if __name__ == '__main__':
    #readcsv()
    starttime=datetime.datetime.now()
    #ReadCsv()
    #question1()
    #question5()
    ##question6()
    ##question7()
    ##question8()
    question9()
    ##question10()
    endtime=datetime.datetime.now()-starttime
    print(f"{endtime} : Time Taken")