from flask import Flask

app = Flask(__name__)


class WebRequest:
    def __init__(self, filename):
        self.filename = filename

        @app.route('/file')
        def logger_data():
            file_obj=open(self.filename,'r')
            return file_obj.readlines()

    @staticmethod
    def run(host="localhost", port=4321):
        app.run(host=host, port=port)
