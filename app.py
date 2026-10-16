import mysql.connector
from flask import Flask, app, redirect, render_template, request, session

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
    user="root",
    password="",
    database="account"
)

mycursor = mydb.cursor()

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "INSERT INTO users (name, pass) VALUES (%s, %s)"
        val = (username, password)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
    return render_template("signin.html")

#result = mycursor.fetchall()
#for x in result: print(x)
#mydb.commit()

if __name__=='__main__': 
   app.run(debug=True, port=5000, host='0.0.0.0')