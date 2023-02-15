from flask import *
from datetime import datetime
import mysql.connector


app = Flask(__name__)



connection = mysql.connector.connect(
                              host = 'localhost',
                              user = 'root',
                              password = '',
                              database = 'bdmain')

cursor = connection.cursor()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/traitement", methods=['POST', 'GET'])
def traitement():
    if request.method == 'POST':
        donnee = request.form
        mail = request.form.get('mail')
        pseudo = request.form.get('pseudo')
        mdp = request.form.get('password')
        date = datetime.now()
        val = mail, pseudo, mdp, date
        sql = "INSERT INTO user (mail, pseudo, password, date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, val)
        connection.commit()
        return render_template('index.html')
    else:
        return redirect(url_for('index'))
        
if __name__=='__main__':
    app.run(debug= True)

connection.close()



