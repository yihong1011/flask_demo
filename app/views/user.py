from flask import render_template, request
from app.models.user import User, _create

class views:
    def index():
        return render_template("users/index.html")

    def new():
        user = User()
        return render_template("users/new.html", user=user)

    def create():
        username = request.form["username"]
        email = request.form["email"]
        _create(username, email)

        return "User creation successful"

    def edit(id):
        user = User.query.filter_by(id=id).first()
        return render_template("users/edit.html", user=user)