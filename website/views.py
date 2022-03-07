from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Folder
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        folder = request.form.get('folder')

        if len(folder) < 1:
            flash('Folder name is too short!', category='error')
        else:
            new_folder = Folder(name=folder, user_id=current_user.id)
            db.session.add(new_folder)
            db.session.commit()
            flash('Folder added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-folder', methods=['POST'])
def delete_folder():
    folder = json.loads(request.data)
    folderId = folder['folderId']
    folder = Folder.query.get(folderId)
    if folder:
        if folder.user_id == current_user.id:
            db.session.delete(folder)
            db.session.commit()

    return jsonify({})


# Försöker öppna unikt fönster/unik route efter folder id
# Olika folder.id ska öppna olika sidor där notes sparas
# Vi får en unik url men varför tillåts inte metoden?

@views.route('/home/<int:folder_id>', methods=['POST, GET'])
def note_view(folder_id):
    folder = Folder.query.get_or_404(folder_id)

    return render_template('page.html', title = folder.name, folder = folder)





   # @views.route('/folder', methods = ['GET, POST'])
#def folder():
        
  #  if request.method == 'POST':
  #         pass
 #           note = request.form.get('note')
    
     #   if len(note) < 1:
     ##       flash('Note is too short!', category='error')
   ##     else:
     #       new_note = Note(data=note, user_id=Folder.id)
      #      db.session.add(new_note)
       #     db.session.commit()
        #    flash('Note added!', category='success')
        
    #return render_template("folder.html")