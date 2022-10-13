import csv
import pandas as pd
import datetime


def readcsv():
    fl=open(csvname,'r')
    reader=csv.reader(fl)
    Tlen=0
    for row in reader:
        #print(row)
        Tlen+=1
    print(Tlen)

def ReadCsv():
    return(pd.read_csv(csvname))
    #print(pd_resultset)
    #print(len(pd_resultset))

def question1(df):
    ''' Question 1 '''
    print("##### Question 1 ##### ")
    print(len(df))
    ##print (df.head(10))
    print(f"Min pickup time: {df.pickup_datetime.min()}")
    print(f"Max pickup time: {df.pickup_datetime.max()}")
    print(f"Min dropoff time: {df.dropoff_datetime.min()}")
    print(f"Max dropoff time: {df.dropoff_datetime.max()}")
    print(f"Datetime Range between: {df.pickup_datetime.min()} and {df.dropoff_datetime.max()} ")

def question2(df):
    ''' Question 2 '''
    print ("##### Question 2 ##### ")
    print(f"Number of columns: {len(list(df.columns.values))}")
    print(list(df.columns.values))

def question3(df):
    ''' Question 3 '''
    print ("##### Question 3 ##### ")
    print(df.head(5).to_string())



csvname="trip_data_1.csv"
if __name__ == '__main__':
    #readcsv()
    starttime=datetime.datetime.now()
    pd_resultset=ReadCsv()
    question1(pd_resultset)
    question2(pd_resultset)
    question3(pd_resultset)
    endtime=datetime.datetime.now()-starttime
    print(f"{endtime} : Time Taken")