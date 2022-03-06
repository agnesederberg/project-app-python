from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# These are our dataclasses that represent the tables in our database modeling. They are commented out because we  
# are working to connecting our user, folder and note class in three steps. These steps are not finished yet but our classes are defined.

class Folder(db.Model):
   id= db.Column(db.Integer, primary_key=True)
   data= db.Column(db.String(50))
   date= db.Column(db.DateTime(timezone=True), default=func.now())
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   note = db.relationship('Note')
#   category_id= db.Column(db.Integer, db.ForeignKey('category.id'))
#   folder = db.relationship('Folder')

#class Category(db.Model):
#   id= db.Column(db.Integer, primary_key=True)
#   name= db.Column(db.String(50))


#class Note(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #   data = db.Column(db.String(10000))
   # date = db.Column(db.DateTime(timezone=True), default=func.now())
   # folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
   # folder = db.relationship('Folder')


#class User(db.Model, UserMixin):
 #   id = db.Column(db.Integer, primary_key=True)
  #  email = db.Column(db.String(150), unique=True)
   # password = db.Column(db.String(150))
   # first_name = db.Column(db.String(150))
   # folder = db.relationship('Folder') 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('folder.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    folder = db.relationship('Folder') #ändra till folder-relationship







    # ändra user_id till typ folder_id på class note, sammankopplar folder till id, sammankollar note till folder och då blir alla sammankopplat till user    
# gör en klass för folder, data= string - gör datan till en knapp i html

