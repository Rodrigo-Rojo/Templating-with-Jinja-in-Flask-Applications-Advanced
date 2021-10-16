from flask import Flask, render_template
import datetime
from data import data

today = datetime.datetime.today()
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
