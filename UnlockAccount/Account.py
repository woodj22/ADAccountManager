import argparse
from activedirectory import ActiveDirectory
def main(account_details):
    ad = ActiveDirectory()
    # user = ad.search_by_account_name(accountName=account_details.account_name)
    # dn = user[0]
    ad.change_password('woodj22' ,new_password='Hello123')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--password',type = str , dest='password')
    p = parser.add_argument('--username',type = str, dest='account_name')
    args = parser.parse_args()
    main(args)


