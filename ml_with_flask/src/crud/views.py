from flask import Blueprint, render_template, redirect, url_for

from sqlalchemy.orm import Session

from ..app import db
from .models import User
from .forms import UserForm

import logging

logger = logging.getLogger(__name__)

crud = Blueprint(
        "crud", 
        __name__,
        template_folder="templates",
        static_folder="static",
        )

@crud.route('/')
def index():
    return render_template("crud/index.html")

@crud.route('/users')
def users():
    """ユーザーの一覧を取得する。"""
    users = User.query.all()
    return render_template('crud/index.html', users=users)


@crud.route("/users/new", methods=['GET', 'POST'])
def create_user():
    form = UserForm()

    try:
        if form.validate_on_submit():
            user = User(
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data,
            )
            logger.info('0')
            db.session.add(user)
            logger.info('1')
            db.session.commit()
            logger.info('2')
            return redirect(url_for('crud.users'))
    except Exception as e:
        logger.error(e)

    return render_template('crud/create.html', form=form)


