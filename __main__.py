from config import LDAP_ADMIN_USERNAME, LDAP_ADMIN_PASSWORD
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL
import click


def get_domain_server(domain):
    if domain in ('national', None):
        return Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL), 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'

    if domain is 'international':
        return Server("ldap://ldap.international.core.bbc.co.uk", get_info=ALL), 'DC=international,DC=core,DC=bbc,DC=co,DC=uk'

    if domain is 'worldwide':
        return Server("ldap://ldap.worldwide.core.bbc.co.uk", get_info=ALL), 'DC=worldwide,DC=core,DC=bbc,DC=co,DC=uk'

@click.command()
@click.option('--admin_user', help='The account name of the administrator.')
@click.option('--admin_password', help='The password of the administrator.')
@click.option('--account_name', help='The username of the account to be managed.')
@click.option('--domain', help='The domain of the user to be managed.', default='national',  type=click.Choice(['national', 'international', 'worldwide']))
@click.option('--new_password', help='The domain of the user to be managed.')
def main(admin_user, admin_password, account_name, domain, new_password):
    server = get_domain_server(domain)
    if admin_user is None:
        admin_user = LDAP_ADMIN_USERNAME
        admin_password = LDAP_ADMIN_PASSWORD
    ad = ActiveDirectory(*server, admin_user, admin_password)

    if new_password:
        return ad.change_password(account_name=account_name, new_password=new_password)
    else:
        print(ad.search_by_account_name(account_name=account_name))

if __name__ == "__main__":
    main()


