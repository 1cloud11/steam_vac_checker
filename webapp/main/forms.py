from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class MainForm(FlaskForm):
    value = StringField(validators=[DataRequired()],
                        render_kw={"class": "form-control",
                                   "placeholder": "Steam Nickname / Faceit Nickname / Room ID"
                                   })

    submit = SubmitField('Check!', render_kw={"class": "btn btn-primary"})