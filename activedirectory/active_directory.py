from config import LDAP_PASSWORD, LDAP_USERNAME
from ldap3 import Connection

class ActiveDirectory(Connection):


    def __init__(self, server, base_dn):
        self.baseDN = base_dn
        super(ActiveDirectory, self).__init__(server=server, user=LDAP_USERNAME, password=LDAP_PASSWORD, auto_bind=True)

    def formatted_search(self, search_filter):
        self.search(self.baseDN, search_filter)
        return self.response[0]

    def search_by_account_name(self, account_name):
        searchFilter = "(&(objectCategory=Person)(objectClass=User)(samaccountname=" + account_name + "))"
        return self.formatted_search(searchFilter)

    def search_by_user_dn(self, user_dn):
        search_filter = "(distinguishedname=" + user_dn +")"
        return self.formatted_search(search_filter)

    def change_password(self, user_dn, new_password):
        self.extend.microsoft.modify_password(user_dn, new_password, None)

    def __del__(self):
       self.unbind()


