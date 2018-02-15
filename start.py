from config import LDAP_ADMIN_USERNAME, LDAP_ADMIN_PASSWORD, LDAP_SERVER_DEFAULT_ADDRESS, LDAP_SERVER_DEFAULT_DN, LDAP_SERVER_DETAILS
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL
from flask import Flask


def get_domain_server(domain):
    if domain in LDAP_SERVER_DETAILS:
        return Server(LDAP_SERVER_DETAILS.get(domain)[0], get_info=ALL), LDAP_SERVER_DETAILS.get(domain)[1]
    else:
        return Server(LDAP_SERVER_DEFAULT_ADDRESS, get_info=ALL), LDAP_SERVER_DEFAULT_DN



app = Flask(__name__)


def adConnection(admin_user, admin_password, domain, base_dn, server_address):
    if None not in (base_dn, server_address):
        server = Server(server_address, get_info=ALL), base_dn
    else:
        server = get_domain_server(domain)
    return ActiveDirectory(*server, admin_user, admin_password)

def change_password(ad, new_password):
    if ad.change_password(account_name=ad.accountName, new_password=new_password):
        print("Your password has been changed. You just saved your company some money.")
        return
    print("your password has not been changed.")

@app.route('/<domain>/<account_name>')
def get_person_details(domain, account_name):
        return "user %s" % account_name
        result = adConnection(domain=domain).search_by_account_name(account_name=account_name)
        return result

@app.route('/')
def hello():
    return 'hello world'
def unlock_account(ad):
    if ad.unlock_account(account_name=ad.accountName):
        print("Your account has been unlocked.")
        return
    print("Your password has not been unlocked.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)