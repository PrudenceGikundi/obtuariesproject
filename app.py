from flask_wtf import CSRFProtect
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import Obituary, db
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
csrf = CSRFProtect(app)

@app.route("/")
def home():
    return render_template("obituary_form.html")

@app.route("/submit_obituary", methods=["POST"])
def submit_obituary():
    try:
        name = request.form["name"]
        date_of_birth = datetime.strptime(request.form["date_of_birth"], "%Y-%m-%d")
        date_of_death = datetime.strptime(request.form["date_of_death"], "%Y-%m-%d")
        content = request.form["content"]
        author = request.form["author"]
        submission_date = datetime.now()

        new_obituary = Obituary(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, content=content, author=author, submission_date=submission_date)
        db.session.add(new_obituary)
        db.session.commit()

        flash("Obituary submitted successfully!", "success")
        return redirect(url_for("home"))
    except ValueError as e:
        flash(f"Invalid date format: {str(e)}", "danger")
        return render_template("obituary_form.html")
    except Exception as e:
        flash(f"Error submitting obituary: {str(e)}", "danger")
        return render_template("obituary_form.html")

@app.route("/obituaries")
def view_obituaries():
    obituaries = Obituary.query.all()
    return render_template("view_obituaries.html", obituaries=obituaries)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)