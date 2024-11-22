from flask import Flask, request, render_template
import requests 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fact = ''
    if request.method == 'POST':
        number = request.form['number']
        response = requests.get(f'http://numbersapi.com/{number}')
        if response.status_code == 200:
            fact = response.text
        else:
            fact = "sorry  machuuu....."

    return render_template('index.html', fact=fact)

if __name__ == '__main__':
    app.run(debug=True)