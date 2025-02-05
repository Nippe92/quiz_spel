from flask import current_app as app
from flask import render_template, request, redirect, url_for, session
from app import db
from app.models import User, Score
from config import Url
from app.play_game import PlayGame, Scoreboard
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import random


@app.route("/")
def home():
    login =request.args.get("login")
    create_account = request.args.get("create_account")
    return render_template("home_page.html", login=login, create_account=create_account)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            
            user = User.query.filter_by(username=username).first()

            if user:
                print("User found")
                
                if check_password_hash(user.password, password):
                    
                    session["user_id"] = user.id  
                    session["username"] = user.username  
                    return redirect(url_for("quiz_page"))
                else:
                    
                    return render_template("login.html", error="Wrong password, please try again")
            else:
                
                return render_template("login.html", error="username does not exist")
        else:
            return render_template("login.html", error="Please fill in all fields")
    
    
    return render_template("login.html")




@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                return "That username is already taken", 400
            
            
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            user = User(username=username, password=hashed_password)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login", create_account="success"))
        

    return render_template("create_account.html")


@app.route("/quiz_choice", methods=["GET", "POST"])
def quiz_page():
    if "user_id" not in session:
        return redirect(url_for("login"))

    choice = PlayGame()

    category, difficulty, question_amount = choice.fetch_choices()

    return render_template("quiz_choice.html", category=category, difficulty=difficulty, question_amount=question_amount)

@app.route("/playgame", methods=["GET", "POST"])
def quiz_play():

    amount = request.args.get("amount")  
    category = request.args.get("category")
    difficulty = request.args.get("difficulty")

    url_builder = Url()
    quiz_url = url_builder.build_url(amount, category, difficulty) 

    response = requests.get(quiz_url)  
    questions = response.json()  

    for index, question in enumerate(questions["results"]):
        all_answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(all_answers)  
        question["shuffled_answers"] = all_answers
        question["index"] = index 

    return render_template("playgame.html", questions=questions)  

@app.route("/score", methods=["GET", "POST"])
def score():
    
    return render_template("scores.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))