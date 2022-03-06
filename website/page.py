from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Folder, User
from . import db
import json

page = Blueprint('page', __name__)


@page.route('/ny', methods=['GET', 'POST'])
def ny():
    currentFolder = Folder.query.filter_by()
    
    if request.method == 'POST':
           
        note = request.form.get('note')

        if len(note) < 1:
                flash('Note is too short!', category='error')
        else:
                new_note = Note(data=note, user_id=Folder.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')
        
    return render_template("page.html", user=current_user, folder = currentFolder)

@page.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
