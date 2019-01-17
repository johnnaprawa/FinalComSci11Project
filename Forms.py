from flask_wtf import FlaskForm
from wtforms import SubmitField
import app

class E2Form(FlaskForm):
    submit = SubmitField('Play E2 Chord')

class AForm(FlaskForm):
    submit2 = SubmitField('Play A Chord')

class DForm(FlaskForm):
    submit3 = SubmitField('Play D Chord')

class GForm(FlaskForm):
    submit4 = SubmitField('Play G Chord')

class BForm(FlaskForm):
    submit5 = SubmitField('Play B Chord')

class E1Form(FlaskForm):
    submit6 = SubmitField('Play E1 Chord')
