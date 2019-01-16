from flask import Flask, render_template
from Forms import E2Form, AForm, DForm, GForm, BForm, E1Form

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
    if form1.validate_on_submit():
        sound_file= 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)

    if form2.validate_on_submit():
        sound_file = 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)
    if form3.validate_on_submit():
        sound_file = 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)

    if form4.validate_on_submit():
        sound_file = 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)

    if form5.validate_on_submit():
        sound_file = 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)

    if form6.validate_on_submit():
        sound_file = 'static\\' + 'flyin_high.wav'
        return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)

    sound_file="static/flyin_high.wav"

    return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, sound_file=sound_file)



if __name__ == '__index__':
    app.run()

