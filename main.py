from flask import Flask

app = Flask(__name__)
@app.route('/'):
def default():
    return 'This is default API'


if __name__ == '__main__':
    app.run(debug=True)