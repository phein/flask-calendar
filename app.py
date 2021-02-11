import calendar, datetime
from flask import Flask, render_template, request, redirect, url_for
from models import create_post, get_reserveList

app =Flask(__name__)

myclendar = calendar.Calendar(calendar.SUNDAY)
# year = datetime.datetime.today().year
# month = datetime.datetime.today().month
# dates = list(myclendar.itermonthdates(year,month))
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
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    dates = list(myclendar.itermonthdates(year,month))
    return render_template(
        'calendar.html', months = months, dates = dates, days = days, month=month, year=year
        )


@app.route('/newcalendar/<int:month>/<int:year>')
def newCalendar(month, year):
    dates = list(myclendar.itermonthdates(year,month))
    return render_template(
        'calendar.html', months = months, dates = dates, days = days, month=month, year=year
        )


@app.route('/prevyear/<int:month>/<int:year>', methods=['GET', 'POST'])
def prevYear(month, year):
    if request.method == 'POST':
        new_year = year-1
    return redirect(url_for('newCalendar', year=new_year, month=month))

@app.route('/nextyear/<int:month>/<int:year>', methods=['GET', 'POST'])
def nextYear(month, year):
    if request.method == 'POST':
        new_year = year+1
    return redirect(url_for('newCalendar', year=new_year, month=month))

@app.route('/setMonth/<int:month>/<int:year>',methods=['GET','POST'])
def setMonth(month, year):
    if request.method == 'POST':
        new_month = month
    return redirect(url_for('newCalendar', month=new_month, year=year))


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