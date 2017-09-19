# ADAccountManager
Manage a active directory user's account using an admin account.

### Requirements

python3 
pip3

### Installation 

This requires that you have pip3 installed.

I have tried to make the installation as simple as possible while still keeping some things baked into configuration file and thus need manually setting up. 

1) Clone this repository. 
2) From inside the repository rename the file `config.example.py` into `config.py`.
3)  Edit this config file by adding admin LDAP accounts to be used for all active directory operations. 
    This is so that you don't need to add the admin user and password every time you run the command.
4) From inside the repository run the command `sudo pip3 install .` This installs the package using the setuputils package and will build a global console command. 
5) Test that it works by runnning `ADAccountManager` from anywhere other than the repository. 
  Use the correct flags as described in the usage section of this readme file to use all its functionalities correctly. 
  
  
 ### Usage 
 