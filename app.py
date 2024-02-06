from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!!!'




if __name__ == '__main__':
    app.run()