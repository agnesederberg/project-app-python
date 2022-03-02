from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# gör en klass för folder, data= string - göt datan till en knapp i html


#class Folder(db.Model):
#   id=
#   data= db.Column(db.String(100))
#   user_id = foreinkey
#   date= ska vi ha date här?
#   user = db.relationship('User')
#   content = data?? se ovan 
# ändra user_id till typ folder_id på class note, sammankopplar folder till id, sammankollar note till folder och då blir alla sammankopplat till user    

#class Category(db.Model):
#   id=
#   data=
#   folder_id= foreinkey?

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #ändra till folder-relationship