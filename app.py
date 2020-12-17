import logging
from flask import Flask, Response

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

KO_BODY = """
<?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><siv:rep_consulter_dossier xmlns:siv="http://siv.mi.fr/DefinitionsServices/2007-06">
<siv:control>
<siv:code_partenaire>127344</siv:code_partenaire>
<siv:code_miat>QSIV</siv:code_miat>
<siv:date_envoi>2020-12-04T10:51:41+01:00</siv:date_envoi>
<siv:type_operation>Consultation Dossier</siv:type_operation>
<siv:numero_session>3294ae7d-e1d8-458b-82ac-60356b80a261</siv:numero_session>
<siv:code_traitement>0</siv:code_traitement>
<siv:code_operation>1830959</siv:code_operation>
<siv:date_reception>2020-12-04T10:51:46+01:00</siv:date_reception>
<siv:type_fichier_joint>xml</siv:type_fichier_joint>
</siv:control>
<siv:reponse>
<siv:dossier>
<siv:immatriculation>
<siv:num_immat>CV-773-KC</siv:num_immat>
<siv:date_prem_immat>2013-06-03</siv:date_prem_immat>
<siv:date_att_immat>2013-06-03</siv:date_att_immat>
<siv:code_type_immat>N</siv:code_type_immat>
<siv:libelle_type_immat>Normale</siv:libelle_type_immat>
</siv:immatriculation>
<siv:vehicule>
<siv:caracteristiques_techniques>
<siv:marque_vehicule>ALFA ROMEO</siv:marque_vehicule>
<siv:tvv>937BXA1A05C</siv:tvv>
<siv:cnit>MAL1302JP364</siv:cnit>
<siv:denomination_com>147</siv:denomination_com>
<siv:vin>ZAR93700005138320</siv:vin>
<siv:code_couleur>99</siv:code_couleur>
<siv:libelle_couleur>INCONNU</siv:libelle_couleur>
<siv:pt>1730</siv:pt>
<siv:ptac>1730</siv:ptac>
<siv:ptra>3030</siv:ptra>
<siv:ptav>1285</siv:ptav>
<siv:categorie_ce>M1</siv:categorie_ce>
<siv:genre_national>VP</siv:genre_national>
<siv:carrosserie_ce>AB</siv:carrosserie_ce>
<siv:carrosserie_national>CI</siv:carrosserie_national>
<siv:num_reception>e3*98/14*0070*03</siv:num_reception>
<siv:type_reception>CE</siv:type_reception>
<siv:cylindree>1598</siv:cylindree>
<siv:puissance_nette_max>77</siv:puissance_nette_max>
<siv:energie>ES</siv:energie>
<siv:puissance_cv>7</siv:puissance_cv>
<siv:places_assises>5</siv:places_assises>
<siv:niveau_sonore>82</siv:niveau_sonore>
<siv:vitesse>4200</siv:vitesse>
<siv:co2>192</siv:co2>
<siv:classe_environnement_ce>70/220*2001/1EURO3</siv:classe_environnement_ce>
</siv:caracteristiques_techniques>
</siv:vehicule>
<siv:personne>
<siv:nb_cotitulaires>0</siv:nb_cotitulaires>
<siv:liste_personnes>
<siv:personne>
<siv:code_type_personne>TIT</siv:code_type_personne>
<siv:libelle_type_personne>titulaire</siv:libelle_type_personne>
<siv:identite_personne>
<siv:flag_pers_physique>oui</siv:flag_pers_physique>
<siv:nom_naiss>NIAMKE</siv:nom_naiss>
<siv:prenom>XAVIER</siv:prenom>
<siv:sexe>M</siv:sexe>
<siv:date_naissance>1984-09-29</siv:date_naissance>
<siv:lieu_naissance>ABIDJAN</siv:lieu_naissance>
<siv:pays_naissance>COTE D IVOIRE</siv:pays_naissance>
</siv:identite_personne>
<siv:adresse_personne>
<siv:point_remise>ESC 23 APPT 559</siv:point_remise>
<siv:compl_adresse>BAT K</siv:compl_adresse>
<siv:num_voie>23</siv:num_voie>
<siv:type_voie>ALL..E</siv:type_voie>
<siv:libelle_voie>DU PARC LE NOTRE</siv:libelle_voie>
<siv:code_postal>95310</siv:code_postal>
<siv:libelle_commune>ST OUEN L AUMONE</siv:libelle_commune>
</siv:adresse_personne>
</siv:personne>
<siv:personne>
<siv:code_type_personne>ACQ</siv:code_type_personne>
<siv:libelle_type_personne>acqu..reur</siv:libelle_type_personne>
<siv:identite_personne>
<siv:flag_pers_physique>oui</siv:flag_pers_physique>
<siv:nom_naiss>LAPILUS</siv:nom_naiss>
<siv:prenom>LAURENT</siv:prenom>
<siv:sexe>M</siv:sexe>
</siv:identite_personne>
<siv:adresse_personne>
<siv:num_voie>11</siv:num_voie>
<siv:type_voie>AVENUE</siv:type_voie>
<siv:libelle_voie>DU GENERAL DE GAULLE</siv:libelle_voie>
<siv:code_postal>95310</siv:code_postal>
<siv:libelle_commune>ST OUEN L AUMONE</siv:libelle_commune>
</siv:adresse_personne>
</siv:personne>
</siv:liste_personnes>
<siv:acquisition>
<siv:dca_date_ca>2013-08-12</siv:dca_date_ca>
<siv:dca_date_enr_ca>2014-01-31</siv:dca_date_enr_ca>
<siv:dca_code_type_ca>C</siv:dca_code_type_ca>
<siv:dca_code_type_nd>N</siv:dca_code_type_nd>
<siv:dca_qualite_acheteur>LAURENT LAPILUS</siv:dca_qualite_acheteur>
</siv:acquisition>
</siv:personne>
<siv:titres>
<siv:document>
<siv:code_type_document>CPI</siv:code_type_document>
<siv:libelle_type_document>certificat provisoire d'immatriculation</siv:libelle_type_document>
<siv:date_emission_cpi>2013-06-03</siv:date_emission_cpi>
<siv:date_fin_cpi>2013-07-02</siv:date_fin_cpi>
<siv:num_cpi>10067322114</siv:num_cpi>
<siv:mode_expedition>TIT</siv:mode_expedition>
</siv:document>
<siv:document>
<siv:code_type_document>CI</siv:code_type_document>
<siv:libelle_type_document>certificat d'immatriculation</siv:libelle_type_document>
<siv:date_ci>2013-07-15</siv:date_ci>
<siv:num_formule>2013DD95586</siv:num_formule>
<siv:etat_vol_titre>non</siv:etat_vol_titre>
<siv:etat_perte_titre>non</siv:etat_perte_titre>
<siv:etat_prod_titre>4</siv:etat_prod_titre>
<siv:etat_remise>FO</siv:etat_remise>
<siv:duplicata>non</siv:duplicata>
<siv:mode_expedition>TIT</siv:mode_expedition>
<siv:adresse_expedition>
<siv:num_voie>11</siv:num_voie>
<siv:type_voie>AVENUE</siv:type_voie>
<siv:libelle_voie>DU GENERAL DE GAULLE</siv:libelle_voie>
<siv:code_postal>95310</siv:code_postal>
<siv:libelle_commune>ST OUEN L AUMONE</siv:libelle_commune>
</siv:adresse_expedition>
</siv:document>
</siv:titres>
<siv:situation_administrative>
<siv:flag_situation>
<siv:flag_vehicule_vole>false</siv:flag_vehicule_vole>
<siv:flag_gage>false</siv:flag_gage>
<siv:flag_pve>false</siv:flag_pve>
<siv:flag_dvs>false</siv:flag_dvs>
<siv:flag_ove>false</siv:flag_ove>
<siv:flag_otci>false</siv:flag_otci>
<siv:flag_suspendu>true</siv:flag_suspendu>
<siv:flag_destruction>false</siv:flag_destruction>
<siv:flag_immobilisation>true</siv:flag_immobilisation>
</siv:flag_situation>
<siv:suspension>
<siv:date_suspension>2015-11-11</siv:date_suspension>
<siv:type_suspension>PJU</siv:type_suspension>
<siv:motif>immobilisation par la police judiciaire</siv:motif>
</siv:suspension>
<siv:immobilisation>
<siv:date_enregistrement>2015-11-12</siv:date_enregistrement>
<siv:date_decision_retrait_ci>2015-11-11</siv:date_decision_retrait_ci>
<siv:type_immobilisation>PJU</siv:type_immobilisation>
<siv:unite>SR NUIT</siv:unite>
<siv:code_postal_unite>95000</siv:code_postal_unite>
<siv:commune_unite>CERGY</siv:commune_unite>
</siv:immobilisation>
</siv:situation_administrative>
</siv:dossier>
</siv:reponse>
</siv:rep_consulter_dossier></soapenv:Body></soapenv:Envelope>
"""


@app.route('/hello_world')
def hello_world():
    return 'hello world'


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def error():
    return Response(KO_BODY, mimetype='text/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
