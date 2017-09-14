import argparse
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL


def main(account_details):
    server = Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL)
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    ad = ActiveDirectory(server, baseDN)

    user = ad.search_by_account_name(account_name=account_details.account_name)
    exit(user)
    ad.change_password('woodj22' ,new_password='Hello123')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--password',type = str , dest='password')
    p = parser.add_argument('--username',type = str, dest='account_name')
    args = parser.parse_args()
    main(args)


