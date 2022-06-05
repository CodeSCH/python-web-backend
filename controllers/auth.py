from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from model.Users import *
from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness

import os
import time

def login_user(): #Puede ser considerar solo POST
    if request.method == 'POST':
        card = request.form['card']
        dni = request.form['dni']
        password = request.form['password']
        user = Users.query.filter_by(
            card=card, dni=dni).first()

        # print(user.id)
        if user and check_password_hash(user.password, password):
            detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                             'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                             'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                             'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                             confidence=0.5)
            if user.fullname == detected_name and label_name == 'real':
                session['id'] = user.id
                session['fullname'] = user.fullname
                return redirect(url_for('main'))
            else:
                return render_template('login_page.html', invalid_user=True, username=user.fullname)
        else:
            return render_template('login_page.html', incorrect=True)
    return render_template('login_page.html')

def register_user():
    if request.method == 'POST':
        # img = request.files['image']
        card = request.form['card']
        fullname = request.form['fullname']
        email = request.form["email"]
        dni = request.form['dni']
        password = request.form['password']
        token = int(round(time.time() * 1000))
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = Users(fullname=fullname, email=email,
                         dni=dni, card=card, password=hashed_password)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        print("registradoooo")

        os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{fullname}')

        return redirect(url_for('login'))
    return render_template('register.html')