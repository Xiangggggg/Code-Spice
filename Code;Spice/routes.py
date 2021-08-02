from flask import *

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html", title="Home")

@main.route("/home")
def redirect_home():
    return redirect(url_for("main.home"))

@main.route("/search")
def redirect_s():
    return redirect("http://www.google.com")

@main.route("/about")
def about():
    return render_template("about.html", title="About")

@main.route("/signup")
def signup():
    return render_template("signup.html", title="Sign Up!")