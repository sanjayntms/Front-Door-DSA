from flask import Flask, request, render_template
import socket
import datetime
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = message = latency = None
    start_time = time.time()

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

    server = socket.gethostname()
    current_time = datetime.datetime.utcnow().isoformat()
    end_time = time.time()
    latency = round((end_time - start_time) * 1000, 2)

    return render_template(
        'index.html',
        name=name,
        message=message,
        server=server,
        time=current_time,
        latency=latency
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
