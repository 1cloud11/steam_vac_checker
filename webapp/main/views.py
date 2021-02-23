from flask import Blueprint, flash, redirect, render_template, url_for

from webapp.main.forms import MainForm


bp = Blueprint('main', __name__, url_prefix=None)


@bp.route('/', methods=['GET', 'POST'])
def index():
    title = 'Faceit Stats'
    form = MainForm()

    if form.validate_on_submit():
        string = form.value.data

    return render_template('main/index.html', title=title, form=form)

    