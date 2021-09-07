from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    data = 'Hello from {}'.format(os.getenv('ENV', 'dev'))
    return jsonify({
        'data': data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
