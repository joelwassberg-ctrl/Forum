import mysql.connector
from flask import Flask, app, redirect, render_template, request, session

app = Flask(__name__)

app.secret_key = "your_secret_key"

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
        except mysql.connector.Error:
            error = "Username already exists. Please choose a different username."
            return render_template("signup.html", error=error)
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "SELECT * FROM users WHERE name = %s AND pass = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            session["username"] = username
            return redirect("home")

        else:
            return "Invalid username or password."
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("login")

@app.route("/home")
def home():
    if "username" in session:
        username = session["username"]
        return render_template("home.html", username=username)
    else:
        return redirect("login")

#result = mycursor.fetchall()
#for x in result: print(x)
#mydb.commit()

if __name__=='__main__': 
   app.run(debug=True, port=5000, host='0.0.0.0')