import argparse
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL
global server

def get_domain_server(domain):
    if domain is 'national':
        return (Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL), 'DC=national,DC=core,DC=bbc,DC=co,DC=uk')

    if domain is 'international':
        return (Server("ldap://ldap.international.core.bbc.co.uk", get_info=ALL), 'DC=international,DC=core,DC=bbc,DC=co,DC=uk')

    if domain is 'worldwide':
        return (Server("ldap://ldap.worldwide.core.bbc.co.uk", get_info=ALL), 'DC=worldwide,DC=core,DC=bbc,DC=co,DC=uk')

    if not domain:
        return (Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL), 'DC=national,DC=core,DC=bbc,DC=co,DC=uk')

def main(account_details):
    server = get_domain_server(account_details.domain)
    ad = ActiveDirectory(*server)

    if account_details.new_password :
        return ad.change_password(account_name=account_details.account_name , new_password=account_details.new_password)
    else:
        print(ad.search_by_account_name(account_name=account_details.account_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--new_password',type = str , dest='new_password')
    p = parser.add_argument('--username',type = str, dest='account_name')
    p = parser.add_argument('--domain',type = str, dest='domain')
    args = parser.parse_args()
    main(args)


