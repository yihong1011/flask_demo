from app import app
from app.views.user import views

@app.route("/",methods=["GET"])
def index():
    return views.index()