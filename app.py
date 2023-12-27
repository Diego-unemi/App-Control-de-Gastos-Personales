from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/newco/OneDrive/Escritorio/ProyectoED/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String)
    amount = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.now)


@app.route('/')
def home():
    bills = Bill.query.order_by(Bill.date.asc()).all()
    total=0
    for bill in bills:
        total += float(bill.amount)
    total = round(total, 2)
    return render_template('index.html', bills=bills, total=total)


@app.route('/registro')
def registro():
    return render_template('record.html')


@app.route('/graficos')
def graficos():
    return render_template('graphics.html')


if __name__ == '__main__':
    app.run(debug=True)

