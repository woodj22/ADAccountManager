import active_directory, sys , getopt, argparse

def main(account_details):
    ad = active_directory.ActiveDirectory()
    user = ad.search_by_account_name(account_details.account_name)
    ad.change_password(user[0], account_details.password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    p = parser.add_argument('--password', dest='password')
    p = parser.add_argument('--username', dest='account_name')
    args = parser.parse_args()
    main(args)


