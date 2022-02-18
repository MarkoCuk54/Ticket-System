from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from send_mail import send_mail
import psycopg2
from datetime import datetime
from datetime import date


app = Flask(__name__)
con = psycopg2.connect(database="lexus", user="postgres", password="emerus2705", host="127.0.0.1", port="5432")
cursor = con.cursor()

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:emerus2705@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bwtagambfndfyn:afcb2c1ae42fd106227a08e721391f332a5b197540afee7a37f408c9574ecce6@ec2-3-227-195-74.compute-1.amazonaws.com:5432/d2dqog8c0rni4q'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Feedback(db.Model):
    __tablename__ = 'prijava'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.String(3))
    comments = db.Column(db.Text())
    date = db.Column(db.Text())
    time = db.Column(db.Text())


    def __init__(self, customer, dealer, rating, comments, date, time):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
        self.date = date
        self.time = time


@app.route('/')
def index():
    return render_template('home.html')

@app.route("/index")
def it():
    return render_template("index.html")
    

@app.route("/odrzavanje")
def odrzavanje():
    return render_template("odrzavanje.html")
    

@app.route('/submit', methods=['POST'])
def submit():
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

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'emerus159':
            error = 'niste ovlašteni koristiti ovu značajku'
        else:
              cursor.execute("SELECT * FROM prijava ORDER BY id DESC")
              result = cursor.fetchall()
              #print(result)
              return render_template("admin.html", data=result)
    return render_template('login.html', error=error)

    


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)