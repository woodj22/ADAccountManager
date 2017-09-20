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
 
It is used as a command line tool where all the options go first followed by the function and its arguments.

for example:
`ADAccountManager --account_name=woodj22 unlock_account`
will unlock an account.

`ADAccountManager --account_name=woodj22 change_password 'newP@ssword'`
Will set a new password for that user. 


For any help just run `ADAccountManager` and it will return a list of all the commands, options and arguments.

### Contribution 

I would be happy for anyone to contribute or suggest any tweaks that should be done. You can contact me via email at joe.wood@bbc.co.uk or use github to create an issue.

If you would like more functionalities to be added just let me know and i can add them. 
