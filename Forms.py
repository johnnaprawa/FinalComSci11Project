from flask_wtf import FlaskForm
from wtforms import SubmitField
import app

class E2Form(FlaskForm):
    submit = SubmitField('Play E2 Chord')

class AForm(FlaskForm):
    submit = SubmitField('Play A Chord')

class DForm(FlaskForm):
    submit = SubmitField('Play D Chord')

class GForm(FlaskForm):
    submit = SubmitField('Play G Chord')

class BForm(FlaskForm):
    submit = SubmitField('Play B Chord')

class E1Form(FlaskForm):
    submit = SubmitField('Play E1 Chord')
