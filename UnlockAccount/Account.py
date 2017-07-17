import active_directory, sys , getopt, argparse

def main(account_details):
    ad = active_directory.ActiveDirectory()
    user = ad.search_by_account_name(account_details.account_name)
    dn = user[0]
   # ad.change_password('woodj22','Hello123')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--password',type = str , dest='password')
    p = parser.add_argument('--username',type = str, dest='account_name')
    args = parser.parse_args()
    main(args)


