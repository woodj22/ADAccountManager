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
    ad = ActiveDirectory(*server, admin_user, admin_password)
    ctx.obj['ad'] = ad
    ctx.obj['accountName'] = account_name


@cli.command()
@click.pass_context
@click.argument('new_password')
def change_password(ctx, new_password):
    if ctx.obj['ad'].change_password(account_name=ctx.obj['accountName'], new_password=new_password):
        print("Your password has been changed. You just saved your company some money.")
        return
    print("your password has not been changed.")

@cli.command()
@click.pass_context
def get_person_details(ctx):
    print(ctx.obj['ad'].search_by_account_name(account_name=ctx.obj['accountName']))


@cli.command()
@click.pass_context
def unlock_account(ctx):
    if ctx.obj['ad'].unlock_account(account_name=ctx.obj['accountName']):
        print("Your account has been unlocked.")
        return
    print("Your password has not been unlocked.")

if __name__ == "__main__":
    cli(obj={})

