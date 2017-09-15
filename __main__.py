import argparse
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL

def main(account_details):
    server = Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL)
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    ad = ActiveDirectory(server, baseDN)
    if account_details.new_password :
        return ad.change_password(account_name=account_details.account_name , new_password=account_details.new_password)
    else:
        print(ad.search_by_account_name(account_name=account_details.account_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--new_password',type = str , dest='new_password')
    p = parser.add_argument('--username',type = str, dest='account_name')
    args = parser.parse_args()
    main(args)


