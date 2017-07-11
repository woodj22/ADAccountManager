import active_directory, sys , getopt

def main(account_name):
	user = active_directory.ActiveDirectory().search_by_account_name(account_name[0])
        active_directory.ActiveDirectory().change_password(user[0], 'Hello12345')


if __name__ == "__main__":
    arguments = sys.argv[1:]
    main(arguments)


