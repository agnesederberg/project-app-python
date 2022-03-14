from werkzeug.security import generate_password_hash
from .models import Note, Folder, Category, User


def setup(db):

        new_category = Category(id=1, name="Work")
        db.session.add(new_category)
        db.session.commit()
        new_category = Category(id=2, name="Hiking")
        db.session.add(new_category)
        db.session.commit()
        new_category = Category(id=3, name="Parties")
        db.session.add(new_category)
        db.session.commit()
        new_category = Category(id=4, name="Wedding")
        db.session.add(new_category)
        db.session.commit()
        new_category = Category(id=5, name="Other")
        db.session.add(new_category)
        db.session.commit()

        new_user = User(email="test@test.test", password=generate_password_hash("1234567", method='sha256'), first_name="test")
        db.session.add(new_user)
        db.session.commit()

        new_folder = Folder(name="work", category_id=1, user_id=1)
        db.session.add(new_folder)
        db.session.commit()
        new_folder = Folder(name="Mount everest", category_id=2, user_id=1)
        db.session.add(new_folder)
        db.session.commit()

        new_note = Note(data="11/04-21: Today was boring, I hope next week will be better", folder_id=1)
        db.session.add(new_note)
        db.session.commit()
        new_note = Note(data="16/04-21: Next week was NOT better", folder_id=1)
        db.session.add(new_note)
        db.session.commit()
        new_note = Note(data="The highest mountain, so beautiful!", folder_id=2)
        db.session.add(new_note)
        db.session.commit()
        new_note = Note(data="I hope that french guy made it back home", folder_id=2)
        db.session.add(new_note)
        db.session.commit()

     