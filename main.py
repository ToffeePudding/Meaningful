from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    name = None
    gender = None
    color = None
    hobbies = None
    feedback = None
    if request.form == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        color = request.form['color']
        hobbies = request.form.getlist('hobbies')
        feedback = request.form['feedback']
      return render_template('index.html', name=name, gender=gender, color=color, hobbies=hobbies, feedback=feedback)



app.run(host='0.0.0.0', port=81)
