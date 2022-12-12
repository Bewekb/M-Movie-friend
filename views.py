from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import pyttsx3
import datetime
import speech_recognition as sr
#from sentimentchatbot import wishMe,takeCommand
from sentimentchatbot import sentiment
import pandas as pd

    
views = Blueprint('views', __name__)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        notesentiment = sentiment(note)

        if len(note) < 1:#
            flash('Note is too short!', category='error')
        else:
            if note.lower() == 'thank you':
                msg = 'anytime,see you soon'
                speak(msg)
                new_note = Note(data=note, sentiment= msg, recommendation = '', user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                # chatlogdf = pd.DataFrame(note, columns=['note', 'notesentiment', 'recommendation'])
                # chatlogdf.to_csv('chatlog.csv', index= False)
            else:
                new_note = Note(data=note, sentiment= notesentiment[0], recommendation = notesentiment[1], user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                speak(note)
                speak(notesentiment[0])
                flash('Note added!', category='success')
        


    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
