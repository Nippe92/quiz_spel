from flask import current_app as app
from flask import render_template, request, redirect, url_for, session, flash
from app import db
from app.models import User, Score
from config import Url
from app.play_game import PlayGame
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import random


@app.route("/")
#first site where you can choose to log in or create account
def home(): 
    login =request.args.get("login")
    create_account = request.args.get("create_account")
    return render_template("home_page.html", login=login, create_account=create_account)

@app.route("/login", methods=["GET", "POST"])
def login():
    #check to see if username/passwords match and are in the database
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            
            user = User.query.filter_by(username=username).first()

            if user:
                print("User found")
                
                #if it match send user to the quiz_page otherwise below flash messages will appear
                if check_password_hash(user.password, password):
                    
                    session["user_id"] = user.id  
                    session["username"] = user.username  
                    return redirect(url_for("quiz_page"))
                else:
                    flash("Wrong password!")
                    return render_template("login.html")
            else:
                flash("username does not exist")
                return render_template("login.html")
        else:
            flash("Please fill in all fields")
            return render_template("login.html")
    
    
    return render_template("login.html")




@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                flash("Username taken")
                return redirect(url_for("create_account"))
            
            #hashing the password
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            user = User(username=username, password=hashed_password)
            
            #adds user to the database and sends user to login page.
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login", create_account="success"))
        

    return render_template("create_account.html")


@app.route("/quiz_choice", methods=["GET", "POST"])
def quiz_page():
    if "user_id" not in session:
        return redirect(url_for("login"))

    choice = PlayGame() #makes an instance of the PlayGame class

    category, difficulty, question_amount = choice.fetch_choices()

    return render_template("quiz_choice.html", category=category, difficulty=difficulty, question_amount=question_amount)

@app.route("/playgame", methods=["GET", "POST"])
def quiz_play():

    amount = request.args.get("amount")  
    category = request.args.get("category")
    difficulty = request.args.get("difficulty")

    #builds the Url after user choices
    url_builder = Url()
    quiz_url = url_builder.build_url(amount, category, difficulty) 

    response = requests.get(quiz_url)  
    questions = response.json()


    session["questions"] = questions["results"]
    
    # combine right and wrong answers and save them.
    for index, question in enumerate(session["questions"]):
        all_answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(all_answers)  
        question["shuffled_answers"] = all_answers
        question["index"] = index

    return render_template("playgame.html", questions=questions)


@app.route("/score", methods=["POST"])
def add_score():

    user_answers = request.form  
    correct_answers = 0  

    if "questions" in session: # check to see if there is any questions in the session.
        for index, question in enumerate(session["questions"]):  
            correct_answer = question["correct_answer"] #fetch the right answer
            user_answer = user_answers.get(f"q{index}") # get the user answer from the dictionary.

            if user_answer == correct_answer:
                correct_answers += 1  

    user_id = session["user_id"]

    new_score = Score(user_id=user_id, score=correct_answers)
    db.session.add(new_score)
    db.session.commit()

    user_score = Score.query.filter_by(user_id=user_id).order_by(Score.id.desc()).first()

    return render_template("scores.html", user_score=user_score)



@app.route("/highscore", methods=["GET", "POST"])
def highscore():

    user_id = session["user_id"]

    #Joining in User database to be able to show username in highscores.
    top_scores = Score.query.join(User).order_by(Score.score.desc()).limit(15).all()

    user_score = Score.query.join(User).filter(User.id == user_id).order_by(Score.id.desc()).first()

    return render_template("highscores.html", user_score=user_score, top_scores=top_scores)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))