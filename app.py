import calendar
from flask import Flask, render_template, request

app =Flask(__name__)

myclendar = calendar.Calendar()
dates = myclendar.itermonthdates(2021,1)
dates = list(dates)
@app.route('/months')
def index():
    months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
    return render_template(
        'calendar.html', months = months
        
    )
@app.route('/')
def result():
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    print(dates)
    return render_template(
        'month.html', dates = dates , days = days
    )

if __name__ == '__main__':
    app.run(debug=True)