# ADAccountManager
Manage an active directory user's account using an admin account.


### Motiviation

When developing internal tools at the BBC I am forever locking an active directory account out. So why not build a tool that can fix this? Although We use PHP here and we have a tool that does this job, I just wanted to show myself what python can do compared to PHP and have a real world project I could sink my teeth into while i learn python. 

### Requirements

python3 
pip3

### Installation 

This requires that you have pip3 installed.

I have tried to make the installation as simple as possible while still keeping some things baked into configuration file and thus need manually setting up. 

1) Clone this repository. 
2) From inside the repository rename the file `config.example.py` into `config.py`.
3)  Edit this config file by adding admin LDAP accounts to be used for all active directory operations. THIS IS AN IMPORTANT STEP fill them all in to make it work really well. 
    This is so that you don't need to add the admin user and password every time you run the command.
4) From inside the repository run the command `sudo pip3 install .` This installs the package using the setuputils package and will build a global console command. 
5) Test that it works by runnning `ADAccountManager` from anywhere other than the repository. 
  Use the correct flags as described in the usage section of this readme file to use all its functionalities correctly. 
  
  
### Usage 
 
It is used as a command line tool where all the options go first followed by the function and its arguments. By default I have set the `domain` to 'National' This is because this is the most used domain within my company and makes it easier for me to use (sorry guys, forgive me).

#### Unlock Account
`ADAccountManager --account_name=woodj22 unlock_account`

#### Change Password
`ADAccountManager --account_name=woodj22 change_password`
 
 This will then ask for a password via a secure prompt. Enter in your new password and away you go!
 
#### Additional Options
When using the tool without a config file you MUST add in the details as options. They work as follows:
`ADAccountManager --account_name=woodj22 --domain=nat --admin_user=svc-ac-1 --addmin_password=P@ss1 --base_dn=DC=nat,DC=c,DC=bcd,DC=co,DC=uk --server_address=http:ldap.nat.bcd.co.uk`

This will otherwise throw an error saying which credentials have not been entered correctly. 

For any help just run `ADAccountManager` and it will return a list of all the commands, options and arguments.

### Contribution 

I would be happy for anyone to contribute or suggest any tweaks that should be done. You can contact me via email at joe.wood@bbc.co.uk or use github to create an issue.

If you would like more functionalities to be added just let me know and i can add them when ever I get a minute.


### Development

to development run venv using `source venv/bin/activate` Everything is installed their so it should work fine.
 running `flask run` will start the development server. the variables `FLASK_APP` and `FLASK_DEBUG` will have to be exported. using the `export` command
`FLASK_APP` should equal `start.py` and the debug option is optional. but to turn on make it equal 1. Debug is pretty useful though. 