from flask import Flask, render_template, request
import datetime
from data import data
import smtplib
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
today = datetime.datetime.today()
app = Flask(__name__)

def send_email(name, email, number, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=email,
            msg=f"Subject: SoriOner's Blog Website Contact\n\n"
                f"{name} want to hear from you\n"
                f"{name} Phone Number: {number}\n"
                f"message: {message}"
        )


@app.route('/')
def home():
    return render_template("index.html", data=data, date=today)


@app.route('/about')
def about():
    return render_template("about.html", date=today)


@app.route('/contact')
def contact():
    return render_template("contact.html", date=today)


@app.route('/post/<id>')
def post(id):
    return render_template("post.html", data=data[int(id) - 1], date=today)


def footer():
    return render_template("footer.html", date=today)


@app.route('/message', methods=['POST'])
def message():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    try:
        send_email(name, email, phone, message)
    except Exception as e:
        print(e)

    return render_template("true.html", date=today)


if __name__ == "__main__":
    app.run(debug=True)
