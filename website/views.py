from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Folder, Category
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    category = Category.query.all()

    if request.method == 'POST':
        folder = request.form.get('folder')
        category = request.form.get('category')
        if len(folder) < 1:
            flash('Folder name is too short!', category='error')
        else:
            new_folder = Folder(name=folder, category_id=category, user_id=current_user.id)
            db.session.add(new_folder)
            db.session.commit()
            flash('Folder added!', category='success')

        category = Category.query.all()

    return render_template("home.html", user=current_user, category=category)


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


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        db.session.delete(note)
        db.session.commit()

    return jsonify({})


@views.route('/home/<int:folder_id>', methods=['POST', 'GET'])
def note_view(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    search = None
    if request.method == 'POST':
        if request.form['submit'] == 'addNote':
            note = request.form.get('note')
            if len(note) < 1:
                flash('Note name is too short!', category='error')
            else:
                new_note = Note(data=note, folder_id=folder.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')
        elif request.form['submit'] == 'search':
            search = request.form.get('search')
        elif request.form['submit'] == 'clearSearch':
            search = None


    return render_template('notes.html', title=folder.name, folder=folder, user=current_user, search=search)