from config import LDAP_ADMIN_USERNAME, LDAP_ADMIN_PASSWORD, LDAP_SERVER_DEFAULT_ADDRESS, LDAP_SERVER_DEFAULT_DN, LDAP_SERVER_DETAILS
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL
from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS

from exceptions.InvalidUsage import InvalidUsage


def get_domain_server(domain):
    if domain in LDAP_SERVER_DETAILS:
        return Server(LDAP_SERVER_DETAILS.get(domain)[0], get_info=ALL), LDAP_SERVER_DETAILS.get(domain)[1]
    else:
        return Server(LDAP_SERVER_DEFAULT_ADDRESS, get_info=ALL), LDAP_SERVER_DEFAULT_DN


app = Flask(__name__)
CORS(app)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def adConnection(domain, admin_user=LDAP_ADMIN_USERNAME, admin_password=LDAP_ADMIN_PASSWORD, base_dn=None, server_address=None):
    if None not in (base_dn, server_address):
        server = Server(server_address, get_info=ALL), base_dn
    else:
        server = get_domain_server(domain)
    return ActiveDirectory(*server, admin_user, admin_password)

@app.route('/<domain>/<account_name>/changepassword', methods=['POST'])
def change_password(domain, account_name):
    new_password = request.json.get('new_password')
    print('new password: ' + new_password)
    # if new_password is None:
    #     raise InvalidUsage('new_password field not found in json POST content.')
    try :
        adConnection(domain).change_password(account_name=account_name, new_password=new_password)
    except Exception as e:
        print(str(e))
    # if adConnection(domain).change_password(account_name=account_name, new_password=new_password):
    #     print("Your password has been changed. You just saved your company some money.")
    #     return
    return Response('Your password has been changed', status=201)

@app.route('/<domain>/<account_name>')
def get_person_details(domain, account_name):
        result = adConnection(domain=domain).search_by_account_name(account_name=account_name)
        return json.dumps(dict(result))

@app.route('/user')
def return_simple_json():
    return Response(jsonify({'username': 'woodj22'}), content_type='application/json')

@app.route('/')
def hello():
    # return 'No need to rebuild image'
    return 'hello world'
def unlock_account(ad):
    if ad.unlock_account(account_name=ad.accountName):
        print("Your account has been unlocked.")
        return
    print("Your password has not been unlocked.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)