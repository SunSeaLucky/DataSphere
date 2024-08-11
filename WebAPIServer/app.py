from flask import Flask

app = Flask(__name__)


@app.route('/data-shpere/web-api-server')
def hello_world():  # put application's code here
    return 'DataSphere Web API Server is RUNNING'


if __name__ == '__main__':
    app.run()
