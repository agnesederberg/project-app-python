from unicodedata import name
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

@views.route('/home/<int:folder_id>', methods=['GET', 'POST'])
def note_view(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, folder_id=folder.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template('notes.html', title = folder.name, folder = folder, user=current_user)
