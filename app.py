import os
from flask import Flask

app = Flask(__name__)

def hello_code():
    target = os.environ.get('TARGET', 'python')
    return 'Hello {}!n'.format(target)

@app.route('/')
def greeting():
    'Hello Code, welcome to Puthon Serverless'

if "__name__" == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

