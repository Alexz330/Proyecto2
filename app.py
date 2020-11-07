from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap



from flask_sqlalchemy import SQLAlchemy

import mysql.connector
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
app = Flask(__name__)





# Mysql Connection
app.config['MYSQL_HOST'] = 'us-cdbr-east-02.cleardb.com' 
app.config['MYSQL_USER'] = 'b54ba59849d9d1'
app.config['MYSQL_PASSWORD'] = 'e2d9526a'
app.config['MYSQL_DB'] = 'heroku_08ae2456d7f7f1d'

mysql = MySQL(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DataBase.db"

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DataBase.db"

# db = SQLAlchemy(app) 
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'hello'


bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'SUPER SECRETO'

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))



# class LoginForm(FlaskForm):
#     username = StringField('Nombre de usuario', validators=[DataRequired(),Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[DataRequired(),Length(min=4, max=10)])
#     remember = BooleanField('remember me')

#     submit = SubmitField('Enviar')



# class RegisterForm(FlaskForm):
#     email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
#     username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)




@app.route('/',methods=['GET', 'POST'])
def index():
    

    response = make_response(redirect('/login'))
    

    return response





@app.route('/static/cargaMasiva.html')

def cargaMasiva():
    return render_template('cargaMasiva.html')



@app.route('/static/cartillas.html')

def cartillas():
    return render_template('cartillas.html')




@app.route('/static/perfil.html')


def Perfil():
    return render_template('perfil.html',)




@app.route('/static/Signup.html')
def crearUsuario():
    return render_template('Signup.html')




@app.route('/login', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM usu WHERE email=%s",(email,))
        usu = curl.fetchone()
        curl.close()

        if len(usu) > 0:
            if bcrypt.hashpw(password, usu["password"].encode('utf-8')) == usu["password"].encode('utf-8'):
                session['name'] = usu['name']
                session['email'] = usu['email']
                return render_template("perfil.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")
    
     

    return render_template('login.html')

       # return'<h1>nombre de usuario o contraseña incorrecta</h1>'    


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("Signup.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        
        print(name)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usu (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('index'))
  

    


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("cartillas.html")





if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug = True, port= 8000)# Se encarga de ejecutar el servidor 5000



