import logging

from pathlib import Path

from email_validator import validate_email, EmailNotValidError 

from flask import (
        Flask, render_template, request, redirect, url_for, flash,
        make_response, session
)

from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def configure_app(app):

    @app.route("/")
    def index():
        return "Hello, Flask!"

    @app.route("/hello", endpoint="hello-endpoint")
    def hello():
        return "Hello, world!"

    @app.route("/name/<name>")
    def name(name: str):
        return render_template("index.html", name=name)

    @app.route("/contact")
    def contact():
        response = make_response(render_template("contact.html"))
        
        response.set_cookie("flashbook key", "flashbook value")

        session["username"] = "ichiro"

        return response


    @app.route("/contact/complete", methods=["GET", "POST"])
    def contact_complete():
        if request.method == "POST":
            username = request.form["username"] 
            email = request.form["email"] 
            description = request.form["description"] 

            is_valid = True
            if not username:
                flash("ユーザ名は必須です。")
                is_valid = False

            if not email:
                flash("メールアドレスは必須です。")
                is_valid = False

            try:
                validate_email(email) 
            except EmailNotValidError:
                flash("メールアドレスの形式で入力してください。")
                is_valid = False

            if not description:
                flash("問い合わせ内容は必須です。")
                is_valid = False

            if not is_valid:
                return redirect(url_for("contact"))

            flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")
            return redirect(url_for("contact_complete"))

        return render_template("contact_complete.html")



def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)
    app.config.from_mapping(
            SECRET_KEY="hogehogehogehogeohge", # don't use in production!!
            SQLALCHEMY_DATABASE_URI= f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO=True,
            WTF_CSRF_SECRET_KEY="hogehogehogehoge"
    )

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)

    from .crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # リダイレクトを中断しないようにする
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    # DebugToolbarExtensionにアプリケーションをセットする
    toolbar = DebugToolbarExtension(app)

    configure_app(app)

    return app

