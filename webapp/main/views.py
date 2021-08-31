from flask import Blueprint, flash, redirect, render_template, url_for

from webapp.main.forms import MainForm
from get_userinfo import get_userinfo

bp = Blueprint('main', __name__, url_prefix=None)


@bp.route('/', methods=['GET', 'POST'])
def index():
    title = 'Faceit Stats'
    form = MainForm()

    if form.validate_on_submit():
        steam_user = form.value.data
        get_userinfo(form.value.data)

    return render_template('main/index.html', title=title, form=form)

    