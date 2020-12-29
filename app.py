import logging
from datetime import datetime, timezone

from flask import Flask, render_template

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


class Dossier:
    def __init__(self, immatriculation: str, vin: str = None):
        self.immatriculation = immatriculation
        self.vin = vin


@app.route('/hello_world')
def hello_world():
    return 'hello world'


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def error():
    date_reception = datetime.now().replace(microsecond=0, tzinfo=timezone.utc).isoformat()
    dossier = Dossier(
        immatriculation='AA-001-AA',
        vin='ZAR93700005138320')

    return render_template('consultation_ko_response', date_reception=date_reception, dossier=dossier)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
