import calendar, datetime
from flask import Flask, render_template, request, redirect, url_for
from models import create_post, get_reserveList

app =Flask(__name__)

myclendar = calendar.Calendar(calendar.SUNDAY)
year = datetime.datetime.today().year
month = datetime.datetime.today().month
dates = list(myclendar.itermonthdates(year,month))
months = {
    1 :'January'   ,
    2 :'February'  ,
    3 :'March'     ,
    4 :'April'     ,
    5 :'May'       ,
    6 :'June'      ,
    7 :'July'      ,
    8 :'August'    ,
    9 :'September' ,
    10 :'October'  ,
    11 :'November' ,
    12 :'December' 
}

days = ['Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
        ]

@app.route('/')
def index():
    return render_template(
        'calendar.html', months = months, dates = dates, days = days, month=month, year=year
        )

@app.route('/prevyear', methods=['GET', 'POST'])
def prevYear():
    global year, dates, month
    if request.method == 'POST':
        year = year-1
        dates = list(myclendar.itermonthdates(year, month))
    return redirect(url_for('index'))

@app.route('/nextyear', methods=['GET', 'POST'])
def nextYear():
    global year, dates, month
    if request.method == 'POST':
        year = year+1
        dates = list(myclendar.itermonthdates(year, month))
    return redirect(url_for('index'))

@app.route('/setMonth',methods=['GET','POST'])
def setMonth():
    if request.method == 'POST':
        global dates, year, month
        month = int(request.form.get('monthNum'))
        dates = list(myclendar.itermonthdates(year, month))
    return redirect(url_for('index'))


@app.route("/postreserve",methods=['GET','POST'])
def postReserve():
    if request.method == 'POST':
        datesNum = request.form.get('datesnum')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        
        create_post(datesNum,fname,lname,email)
    
    return redirect(url_for('index'))


@app.route("/reserve", methods=['GET','POST'])
def reserve():

    if request.method == 'POST':
        date = request.form.get('datesnum')
    reserveList = get_reserveList(date)
    return render_template('reserve.html', dateName = date, reserveList=reserveList)

    

if __name__ == '__main__':
    app.run(debug=True)