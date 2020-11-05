from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from flask_sqlalchemy import SQLAlchemy
import sys


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DataBase.db"

db = SQLAlchemy(app) 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'hello'


bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'SUPER SECRETO'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(),Length(min=4, max=15)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4, max=10)])
    remember = BooleanField('remember me')

    submit = SubmitField('Enviar')



class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)




@app.route('/')
def index():
    

    response = make_response(redirect('/login'))
    

    return response





@app.route('/static/cargaMasiva.html')
@login_required
def cargaMasiva():
    return render_template('cargaMasiva.html')



@app.route('/static/cartillas.html')

def cartillas():
    return render_template('cartillas.html')




@app.route('/static/perfil.html')
@login_required

def Perfil():
    return render_template('perfil.html',name=current_user.username)




@app.route('/static/Signup.html')
def crearUsuario():
    return render_template('Signup.html')




@app.route('/login', methods=['GET', 'POST'])
def hello():
    
    login_form = LoginForm()
    username = session.get('username')

    context = {
        
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
       user =User.query.filter_by(username=login_form.username.data).first()
       if user:
           if user.password == login_form.password.data:
               login_user(user, remember=login_form.remember.data)
               return render_template('perfil.html')  

           flash('Nombre de usuario o contraseña incorrecta') 
                  
    # return'<h1>nombre de usuario o contraseña incorrecta</h1>'    

    

    return render_template('Login.html', **context,form=login_form)

@app.route('/signup', methods=['GET', 'POST'])
def singup():
    form = RegisterForm()

    if form.validate_on_submit():

    
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)

       
        db.session.add(new_user)
        db.session.commit()
       # return '<h1>' + form.username.data +' ' +form.email.data + ' ' +form.password.data '</h1>'
        return '<h1>New user has been created!</h1>'

    return render_template('Signup.html', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

    






if __name__ == "__main__":
    start_db = sys.argv[1] if len(sys.argv) > 1 else ""
    db.create_all() if start_db == "start_db" else None
    print("===== Database Created =====") if start_db == "start_db" else None





app.run(debug = True, port= 8000)# Se encarga de ejecutar el servidor 5000

