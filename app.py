from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from send_mail import send_mail
import psycopg2

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

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Molim vas popunite obavezna polja')
        data = Feedback(customer, dealer, rating, comments)
        db.session.add(data)
        db.session.commit()
        # send_mail(customer, dealer, rating, comments)
        return render_template('success.html')

@app.route("/admin")
def admin_panel():
    cursor.execute("select * from prijava")
    result = cursor.fetchall()
    #print(result)
    return render_template("admin.html", data=result)
    


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)