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


pass_ad = click.make_pass_decorator(ActiveDirectory)


@click.group()
@click.option('--admin_user', help='The account name of the administrator.')
@click.option('--admin_password', help='The password of the administrator.')
@click.option('--account_name', help='The username of the account to be managed.', required=True)
@click.option('--domain', help='The domain of the user to be managed.', default='national',  type=click.Choice(['national', 'international', 'worldwide']))
@click.pass_context
def cli(ctx, admin_user, admin_password, account_name, domain):
    server = get_domain_server(domain)
    if admin_user is None:
        admin_user = LDAP_ADMIN_USERNAME
        admin_password = LDAP_ADMIN_PASSWORD
    ctx.obj = ActiveDirectory(*server, admin_user, admin_password)
    ctx.obj.accountName = account_name


@cli.command()
@pass_ad
@click.argument('new_password')
def change_password(ad, new_password):
    if ad.change_password(account_name=ad.accountName, new_password=new_password):
        print("Your password has been changed. You just saved your company some money.")
        return
    print("your password has not been changed.")

@cli.command()
@pass_ad
def get_person_details(ad):
    print(ad.search_by_account_name(account_name=ad.accountName))


@cli.command()
@pass_ad
def unlock_account(ad):
    if ad.unlock_account(account_name=ad.accountName):
        print("Your account has been unlocked.")
        return
    print("Your password has not been unlocked.")

if __name__ == "__main__":
    cli(obj={})

def main():
    cli(obj={})