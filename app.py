from flask import Flask, render_template, url_for, redirect
from Forms import E2Form, AForm, DForm, GForm, BForm, E1Form
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def home():
    form1 = E2Form()
    form2 = AForm()
    form3 = DForm()
    form4 = GForm()
    form5 = BForm()
    form6 = E1Form()
    if form1.submit.data and form1.validate_on_submit():
        sound_file= 'static/flyin_high.wav'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file))

    if form2.submit2.data and form2.validate_on_submit():
        sound_file = 'static\\' + '5th_String_A_64kb.mp3'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file))

    if form3.submit3.data and form3.validate_on_submit():
        sound_file = 'static\\' + '4th_String_D_64kb.mp3'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,
                                sound_file=sound_file))

    if form4.submit4.data and form4.validate_on_submit():
        sound_file = 'static\\' + '3rd_String_G_64kb.mp3'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,
                                sound_file=sound_file))

    if form5.submit5.data and form5.validate_on_submit():
        sound_file = 'static\\' + '2nd_String_B__64kb.mp3'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,
                                sound_file=sound_file))

    if form6.submit6.data and form6.validate_on_submit():
        sound_file = 'static\\' + '1st_String_E_64kb.mp3'
        return redirect(url_for('home', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,
                                sound_file=sound_file))

    sound_file = "static/"

    return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)



if __name__ == '__index__':
    app.run()

