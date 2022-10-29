import datetime
import json,pymysql,time
from flask import Flask
from flask import request,redirect


app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    res = {}
    res['code'] = 2
    res['msg'] = 'Hi My Test'
    res['req'] = '/test'
    print("Hi My Test")
    return json.dumps(res, indent=4)

def getdatadb(sdate,edate,sqlno):
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='ia626', passwd='ia626clarkson', db='ia626',
                           autocommit=True)  # setup our credentials
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if sqlno == 1:
        sql = 'SELECT DISTINCT `Date` , `Depth` from  `conlontj_snow` WHERE `date` between %s AND %s'
    else:
        sql = 'SELECT MIN(depth) as mindepth , MAX(depth) as maxdepth from  `conlontj_snow` WHERE `date` between %s AND %s'
    starttime = datetime.datetime.now()
    cur.execute(sql, (sdate,edate))
    endtime = datetime.datetime.now() - starttime
    return(cur,endtime)


@app.route("/getData", methods=['GET'])
def getData():
    datalist=[]
    res={}
    if request.args.get('key') is None:
        res['data'] = None
        res['code'] = 0
        res['req'] = 'getData'
        res['msg'] = 'Key not provided'
        return json.dumps(res, indent=4)
    elif request.args.get('key') != '123':
        res['data'] = None
        res['code'] = 0
        res['req'] = 'getData'
        res['msg'] = 'Incorrect Keys'
        return json.dumps(res, indent=4)

    curdata,runtime=getdatadb(request.args.get('start'),request.args.get('end'),1)
    for row in curdata:
        tempdic = {}
        tempdic['Date'] = datetime.date.strftime(row['Date'],'%Y-%m-%d')
        tempdic['Depth'] = row['Depth']
        datalist.append(tempdic)
    res['code'] = 1
    res['msg'] = 'Request OK'
    res['sqltime'] = str(runtime)
    res['req'] = 'getData'
    res['data'] = datalist
    print(res)
    return json.dumps(res, indent=4)

@app.route("/getMinMax", methods=['GET'])
def getMinMax():
    datalist=[]
    res={}
    if request.args.get('key') is None:
        res['data'] = None
        res['code'] = 0
        res['req'] = 'getData'
        res['msg'] = 'Key not provided'
        return json.dumps(res, indent=4)
    elif request.args.get('key') != '123':
        res['data'] = None
        res['code'] = 0
        res['req'] = 'getData'
        res['msg'] = 'Incorrect Keys'
        return json.dumps(res, indent=4)

    curdata,runtime=getdatadb(request.args.get('start'),request.args.get('end'),2)
    print(type(runtime))
    for row in curdata:
        print(row)
        res['code'] = 1
        res['msg'] = 'Request OK'
        res['sqltime'] = str(runtime)
        res['req'] = 'getMinMax'
        res['data'] = row
    #print(res)
    return json.dumps(res, indent=4)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)