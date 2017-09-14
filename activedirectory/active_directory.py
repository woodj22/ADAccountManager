from config import LDAP_PASSWORD, LDAP_USERNAME
from ldap3 import Server, Connection, ALL

class ActiveDirectory(Connection):
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    retrieveAttributes = None

    def __init__(self):

        server = Server("ldap://ldap.national.core.bbc.co.uk", get_info=ALL)
        super().__init__(server, user=LDAP_USERNAME, password=LDAP_PASSWORD, auto_bind=True)

        self.start_tls()

    def search(self, search_filter, attributes):
        ldap_result_id = self.search(self.baseDN, search_filter, attributes=attributes)
        self.USER_DN = self.response[0].get('dn')
        return ldap_result_id[0]


    def search_by_account_name(self, account_name):
        searchFilter = "(&(objectCategory=Person)(objectClass=User)(samaccountname=" + account_name + "))"
        return self.search(searchFilter)

    def search_by_user_dn(self, user_dn):
        search_filter = "(distinguishedname=" + user_dn +")"
        return self.search(search_filter)


    def change_password(self, user_dn, new_password):

        self.extend.microsoft.modify_password(self.USER_DN, new_password, None)

    def __del__(self):
        self.unbind()


