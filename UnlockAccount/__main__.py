import active_directory, sys , getopt
def main(account_name):
	active_directory.ActiveDirectory(account_name[0]).main()


if __name__ == "__main__":
    arguements = sys.argv[1:]
    main(arguements)


