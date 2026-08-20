from flask import Blueprint , render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


# main_blueprint = Blueprint('main', __name__)


# @main_blueprint.route('/')
# def home():
# 	return 'Home Page'
