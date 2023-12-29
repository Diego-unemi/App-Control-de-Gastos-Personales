from flask import Flask, render_template, request, redirect
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
    today = datetime.now().date()
    bills_today = [bill for bill in bills if bill.date.date() == today]
    total = 0
    for bill in bills_today:
        total += float(bill.amount)
    total = round(total, 2)
    total = '{:.2f}'.format(total)
    return render_template('index.html', bills_today=bills_today, total=total)


@app.route('/registro')
def registro():
    bills = Bill.query.order_by(Bill.date.asc()).all()
    today = datetime.now().date()
    bills_today = [bill for bill in bills if bill.date.date() == today]
    return render_template('record.html', bills_today=bills_today)


@app.route('/add', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    categoria = request.form.get('categoria')
    monto = request.form.get('monto')
    bill = Bill(name=nombre, description=descripcion, category=categoria, amount=monto)
    db.session.add(bill)
    db.session.commit()
    return redirect('/registro')


@app.route('/del', methods=['POST'])
def eliminar():
    bill_id = request.form.get('bill-id')
    bill = db.session.query(Bill).filter(Bill.id == bill_id).first()
    db.session.delete(bill)
    db.session.commit()
    return redirect('/registro')


@app.route('/edit', methods=['POST'])
def editar():
    bill_id = request.form.get('bill_id')
    print(bill_id)
    new_name = request.form.get('new_nombre')
    new_description = request.form.get('new_descripcion')
    new_category = request.form.get('new_categoria')
    new_amount = request.form.get('new_monto')
    bill = db.session.query(Bill).filter(Bill.id == bill_id).first()
    bill.name = new_name
    bill.description = new_description
    bill.category = new_category
    bill.amount = new_amount
    db.session.commit()
    return redirect('/registro')


@app.route('/graficos')
def graficos():
    return render_template('graphics.html')


if __name__ == '__main__':
    app.run(debug=True)

