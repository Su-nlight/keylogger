from flask import Flask

app = Flask(__name__)


class WebRequest:
    def __init__(self, filename):
        self.filename = filename

        @app.route('/file')
        def logger_data():
            with open(self.filename, 'r') as file_obj:
                return file_obj.read()

    @staticmethod
    def run(host="localhost", port=4321):
        app.run(host=host, port=port)
