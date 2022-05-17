from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import datetime
from datetime import date
from db import Feedback, Feedback1, db


app = Flask(__name__)
con = psycopg2.connect(database="tiketSystem", user="postgres", password="emerus2705", host="127.0.0.1", port="5432")
cursor = con.cursor()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:emerus2705@localhost/tiketSystem'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/index")
def it():
    return render_template("index.html")


@app.route("/odrzavanje")
def odrzavanje():
    return render_template("odrzavanje.html")


@app.route('/submit_it', methods=['POST'])
def submitIt():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        date = datetime.today().strftime('%Y-%m-%d')
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        # print(customer, dealer, rating, comments)
        # adding here an if statement to see is it it or odrzavanje
        # when "it" make a query to see just it stuff and vica versa
        if customer == '' or dealer == '':
            return render_template('index.html', message='Molim vas popunite obavezna polja')
        data = Feedback( customer, dealer, rating, comments, date, time)
        db.session.add(data)
        db.session.commit()
        # send_mail(customer, dealer, rating, comments)
        return render_template('success.html')


@app.route('/submit_odrzavanje', methods=['POST'])
def submitOdrzavanje():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        date = datetime.today().strftime('%Y-%m-%d')
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        # print(customer, dealer, rating, comments)
        # adding here an if statement to see is it it or odrzavanje
        # when "it" make a query to see just it stuff and vica versa
        if customer == '' or dealer == '':
            return render_template('index.html', message='Molim vas popunite obavezna polja')
        data = Feedback1( customer, dealer, rating, comments, date, time)
        db.session.add(data)
        db.session.commit()
        # send_mail(customer, dealer, rating, comments)
        return render_template('success.html')



# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'emerus159':
            cursor.execute("SELECT * FROM prijava ORDER BY id DESC")
            result = cursor.fetchall()
            #print(result)
            return render_template("admin.html", data=result)
        elif request.form['username'] == 'slaven' and request.form['password'] == 'Emerus2022':
            cursor.execute("SELECT * FROM odrzavanje ORDER BY id DESC")
            result = cursor.fetchall()
            #print(result)
            return render_template("admin.html", data=result)
        else:
            error = 'niste ovlašteni koristiti ovu značajku'

    return render_template('login.html', error=error)




if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
