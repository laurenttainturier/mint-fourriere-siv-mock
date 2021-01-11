import logging
import random
import string
from datetime import datetime, timezone

import xmltodict
from flask import Flask, request, render_template

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route('/hello-world')
def hello_world():
    return 'hello world'


@app.route('/consultation', methods=['GET', 'POST'])
def consultation():
    date_reception = datetime.now().replace(microsecond=0, tzinfo=timezone.utc).isoformat()
    dossier = VehiculeInfo(
        immatriculation='AA-001-AA',
        vin='ZAR93700005138320')

    return render_template('consultation_ko_response', date_reception=date_reception, dossier=dossier), 200, {
        'Content-Type': "text/xml; charset=utf-8"}


@app.route('/interdiction-circuler', methods=['GET', 'POST'])
def interdiction_circuler():
    declaration_expert = get_declaration_expert_from_xml(request.data)
    vehicule_info = VehiculeInfo.get_from_xml(declaration_expert)

    if vehicule_info.immatriculation == "ZA-726-DQ":
        return render_template('ic_error_26.xml'), 200, {
            'Content-Type': "text/xml; charset=utf-8"}

    if vehicule_info.immatriculation == "ZA-727-DQ":
        return render_template('ic_error_27.xml'), 200, {
            'Content-Type': "text/xml; charset=utf-8"}

    return render_template('ic_success.xml', dossier=vehicule_info), 200, {
        'Content-Type': "text/xml; charset=utf-8"}


class VehiculeInfo:
    def __init__(self, immatriculation: str, vin: str = None, numero: str = None):
        self.immatriculation = immatriculation
        self.VIN = vin
        self.numero = numero or random_string(15)

    @staticmethod
    def get_from_xml(declaration_expert_xml: dict):
        vehicule_expertise = declaration_expert_xml['ns2:vehicule_expertise']
        immatriculation = vehicule_expertise['ns2:numero_immatriculation']
        vin = vehicule_expertise['ns2:numero_vin']

        return VehiculeInfo(immatriculation, vin)


def get_declaration_expert_from_xml(xml_response: bytes) -> dict:
    dict_request = xmltodict.parse(xml_response)
    return dict_request['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns2:req_declaration_expert']['ns2:declaration_expert']


def random_string(length: int):
    return ''.join(random.choices(string.hexdigits + string.digits, k=length))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
