from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["SECRET_KEY"] = "password2Password"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "boochip02@gmail.com"
app.config["MAIL_PASSWORD"] = os.getenv("JobApplicationForm")

db = SQLAlchemy(app)
mail = Mail(app)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        # model = Job(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=occupation)
        # db.session.add(model)
        # db.session.commit()

        flash(f"Hey {first_name}, your job is now live!", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
