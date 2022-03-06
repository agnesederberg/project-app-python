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
        note = request.form.get('folder')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Folder(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)
#lägg till def om folder, folder ska vara en knapp eller länk

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

#@views.route('/folder', methods = ['GET, POST'])
#def folder():
        
    #if request.method == 'POST':
    #       pass
    #        note = request.form.get('note')
    #
    #    if len(note) < 1:
    #        flash('Note is too short!', category='error')
    #    else:
    #        new_note = Note(data=note, user_id=Folder.id)
    #        db.session.add(new_note)
    #        db.session.commit()
    #        flash('Note added!', category='success')
        
   # return render_template("folder.html")