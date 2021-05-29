import os
import requests

from flask import Flask, session, render_template, request, redirect, flash, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/assign")
def assign():
    # db.execute("INSERT INTO users (username, gender, year, department) VALUES ('Abraham', 'M', '3', 'software')")
    # db.execute("INSERT INTO users (username, gender, year, department) VALUES ('Zack', 'M', '3', 'software')")
    # db.execute("INSERT INTO users (username, gender, year, department) VALUES ('Bemnet', 'M', '2', 'software')")
    # db.execute("INSERT INTO users (username, gender, year, department) VALUES ('Abel', 'M', '3', 'software')")
    five = db.execute("SELECT * FROM users WHERE year = 5").fetchall()
    five.sort()
    # five.query.order_by(five.year.desc(),five.username.desc()).limit(10).all()
    for i in range(len(five)):
        db.execute("INSERT INTO Fkilo (username, gender, year, department) VALUES (:username, :gender, :year, :department)",
                    {"username":five[i][1], 
                    "gender":five[i][2],
                    "year":five[i][3],
                    "department":five[i][4]})

    six = db.execute("SELECT * FROM users WHERE year != 5 AND gender = 'M'").fetchall()
    six.sort(key=srt1)
    six.sort(key=srt2)
    six.sort(key=srt3)
    for i in range(len(six)):
        db.execute("INSERT INTO Skilo (username, gender, year, department) VALUES (:username, :gender, :year, :department)",
                    {"username":six[i][1], 
                    "gender":six[i][2],
                    "year":six[i][3],
                    "department":six[i][4]})

    fbe = db.execute("SELECT * FROM users WHERE gender = 'F'").fetchall()
    fbe.sort()
    for i in range(len(fbe)):
        db.execute("INSERT INTO Fbekilo (username, gender, year, department) VALUES (:username, :gender, :year, :department)",
                    {"username":fbe[i][1], 
                    "gender":fbe[i][2],
                    "year":fbe[i][3],
                    "department":fbe[i][4]})


    db.commit()

    return render_template("index.html", x=six)

def srt1(k):
    return k[1]

def srt2(k):
    return k[3]

def srt3(k):
    return k[4]