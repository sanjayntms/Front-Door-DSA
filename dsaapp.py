from flask import Flask, jsonify, render_template
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def api():
    return jsonify({
        'server': socket.gethostname(),
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
