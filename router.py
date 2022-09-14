from app import app
from app.views.user import views

@app.route("/",methods=["GET"])
def index():
    return views.index()

@app.route("/new", methods=["GET"])
def new():
    return  views.new()

@app.route("/create", methods=["POST"])
def create():
    return views.create()

@app.route("/<int:id>/edit",methods=["GET"])
def edit(id):
    return views.edit(id)