from config import LDAP_ADMIN_USERNAME, LDAP_ADMIN_PASSWORD, LDAP_SERVER_DEFAULT_ADDRESS, LDAP_SERVER_DEFAULT_DN, LDAP_SERVER_DETAILS
from activedirectory.active_directory import ActiveDirectory
from ldap3 import Server, ALL
import click


def get_domain_server(domain):
    if domain in LDAP_SERVER_DETAILS:
        return Server(LDAP_SERVER_DETAILS.get(domain)[0], get_info=ALL), LDAP_SERVER_DETAILS.get(domain)[1]
    else:
        return Server(LDAP_SERVER_DEFAULT_ADDRESS, get_info=ALL), LDAP_SERVER_DEFAULT_DN

pass_ad = click.make_pass_decorator(ActiveDirectory)

@click.group()
@click.option('--admin_user', help='The account name of the administrator.')
@click.option('--admin_password', help='The password of the administrator.')
@click.option('--account_name', help='sam account name of the user.', required=True)
@click.option('--domain', help='The domain of the user.', default='national',  type=click.Choice(['national', 'international', 'worldwide']))
@click.option('--base_dn', help='The base dn of the active direction server connection.')
@click.option('--server_address', help='The server address of the active directory connection.')
@click.pass_context
def cli(ctx, admin_user, admin_password, account_name, domain, base_dn, server_address):
    if None not in (base_dn, server_address):
        server = Server(server_address, get_info=ALL), base_dn
    else:
        server = get_domain_server(domain)
    if admin_user is None:
        admin_user = LDAP_ADMIN_USERNAME
        admin_password = LDAP_ADMIN_PASSWORD
    ctx.obj = ActiveDirectory(*server, admin_user, admin_password)
    ctx.obj.accountName = account_name


@cli.command()
@pass_ad
@click.option('--new_password', prompt=True, hide_input=True)
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

