from flask import Flask,render_template

app = Flask(__name__)
@app.route('/'):
def default():
    return 'This is default API'

@app.route('/predict')
def predict():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)