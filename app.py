from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

from controllers.auth import *
from model.Users import *
from db.db import *

app = Flask(__name__)
app.secret_key = 'web_app_for_face_recognition_and_liveness'  #SECRET KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    return login_user()

@app.route('/register', methods=['GET', 'POST'])
def register():
    session.clear() 
    return register_user()

@app.route('/client', methods=['GET', 'POST'])
def client():
    try:
        id = session['id']
        fullname = session['fullname']
        if id:
            return render_template('client_page.html', id=id, fullname=fullname)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        print(e)
        return redirect(url_for('login'))

@app.route('/admin', methods=['GET'])
def admin():
    try:
        id = session['id']
        fullname = session['fullname']
        return render_template('admin_page.html', id=id, fullname=fullname)
    except Exception as e:
        return redirect(url_for('login'))

@app.route('/admin/manage/profile', methods=['GET', 'POST'])
def manageprofileAdmin():
    try:
        id = session['id']
        fullname = session['fullname']
        return render_template('admin_crud_profile_page.html', id=id, fullname=fullname)
    except Exception as e:
        return redirect(url_for('admin'))

@app.route('/admin/manage/listEmpl', methods=['GET', 'POST'])
def listAdmin():
    try:
        id = session['id']
        fullname = session['fullname']
        user = Users.query.all()
        return render_template('admin_crud_page.html', id=id, fullname=fullname, users=user)
    except Exception as e:
        print(e)
        return redirect(url_for('admin'))

@app.route('/admin/manage/addEmpl', methods=['POST'])
def addAdmin():
    try:
        id = session['id']
        fullname = session['fullname']
        user = Users.query.filter(Users.rol == 1)

        #Add Admin
        img = request.files['photo']
        fullname=request.form["fullname"]
        email=request.form["email"]
        dni=request.form["dni"]
        password=request.form["password"]
        rol = request.form["rol"]
        hashed_password = generate_password_hash(password, method='sha256')
        phone=request.form["phone"]

        os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')

        filename = secure_filename(img.filename) #Nombre original del archivo
     
        upload_path = os.path.join (f'face_recognition_and_liveness/face_recognition/dataset/{dni}', filename) 
        img.save(upload_path) #Nombre original del archivo  

        newUser = Users(fullname=fullname, email=email, dni=dni, password=hashed_password, rol=rol, phone=phone)
        db.session.add(newUser)
        db.session.commit()
        db.session.close()

        return render_template('admin_crud_page.html', id=id, fullname=fullname, users=user)
    except Exception as e:
        print(e)
        return redirect(url_for('admin'))

@app.route('/admin/manage/deleteEmpl/<idE>')
def deleteAdmin(idE):
    try:
        user = Users.query.all()
        #Add Admin
        userId = Users.query.get(idE)
        db.session.delete(userId)
        db.session.commit()

        return render_template('admin_crud_page.html', users=user)
    except Exception as e:
        print(e)
        return redirect(url_for('admin'))

"""
@app.route('/client/manage', methods=['GET', 'POST'])
def manageClient():

    return manage_client()

"""
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
