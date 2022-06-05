from flask_sqlalchemy import SQLAlchemy

from controllers.auth import *

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
    return login_user()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_user()

@app.route('/main', methods=['GET']) #estoy en duda
def main():
    try:
        id = session['id']
        fullname = session['fullname']
        print(f'Este es el iddddd {id}')
        return render_template('main_page.html', id=id, fullname=fullname)
    except Exception as e:
        return redirect(url_for('login'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
