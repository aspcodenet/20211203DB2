from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/databas20210203'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(10), unique=False, nullable=False)
    cards = db.relationship('Creditcard', backref='person', lazy=True)

class Creditcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(20), unique=False, nullable=False)
    cardnumber = db.Column(db.String(30), unique=True, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)    

if __name__ == "__main__":
    with app.app_context():
        upgrade()
    print("1. Skapa ny person")
    sel= input("val:")
    if sel == "1":
        p = Person()
        p.namn = input("Ange namn:")
        p.city = input("Ange stad:")     
        p.postalcode = input("Ange postalcode:")     
        c = Creditcard()
        c.cardnumber = input("Ange cardnumber:")     
        c.typ = input("Ange typ:")     
        p.cards.append(c)
        c = Creditcard()
        c.cardnumber = input("Ange cardnumber 2:")     
        c.typ = input("Ange typ 2:")     
        p.cards.append(c)

        db.session.add(p)
        db.session.commit()