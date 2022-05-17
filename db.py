from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2



app = Flask(__name__)
con = psycopg2.connect(database="tiketSystem", user="postgres", password="emerus2705", host="127.0.0.1", port="5432")
cursor = con.cursor()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:emerus2705@localhost/tiketSystem'

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

class Feedback1(db.Model):
    __tablename__ = 'odrzavanje'
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
