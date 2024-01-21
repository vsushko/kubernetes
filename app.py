from flask import Flask
import os

app = Flask(__name__)

@app.route('/handler')
def handler():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('HTTP_PORT', 8081))
