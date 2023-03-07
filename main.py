from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    numbers = [1,2,3,4,5]
    with open('intro.txt', 'r') as file:
      intro =file.read()

  #Open CSV file for reading
    with open('Games.csv'ames.csv', 'r') as file:
      reader=csv.reader
      songs=reader
      #Loop through each row in the file 
      #for row in reader:
          #Do something with the row
      #print(row)
    data = None
    if request.method == 'POST':
      data = request.form['data']
      data = data.upper() #whatever magic
      with open('secret.txt', 'a') as file:
        file.write(data + '\n')
    return render_template('index.html', data=data, intro=intro, nums=numbers, songs=songs)



app.run(host='0.0.0.0', port=81)
