import ldap
from config import LDAP_PASSWORD, LDAP_USERNAME

class ActiveDirectory(object):
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None

    def __init__(self):
        self.l = ldap.initialize("ldap://ldap.national.core.bbc.co.uk:3268")
        self.l.bind_s(LDAP_USERNAME, LDAP_PASSWORD)

    def search(self, search_filter):
        try:
            ldap_result_id = self.l.search_s(self.baseDN, self.searchScope, search_filter, self.retrieveAttributes)
            return ldap_result_id[0]
        except ldap.LDAPError, e:
            print e
        self.l.unbind()

    def search_by_account_name(self, accountName):
        searchFilter = "(&(objectCategory=Person)(objectClass=User)(samaccountname=" + accountName + "))"
        return self.search(searchFilter)

    def search_by_user_dn(self, user_dn):
        search_filter = "(distinguishedname=" + user_dn +")"
        return self.search(search_filter)


    def change_password(self,user_dn ,new_password):

        #For test purposes i have spoofed the user_dn and new_password values
        user_dn = "CN=joe.wood,OU=london,OU=deputy director general group,OU=Atos London,OU=Roaming,OU=Interactive,OU=Users,OU=Standard,OU=Business,DC=national,DC=core,DC=bbc,DC=co,DC=uk"
        new_password = "Hello123"
        unicode_pass = unicode('\"' + str(new_password) + '\"', 'iso-8859-1')
        password_value = unicode_pass.encode('utf-16-le')
        add_pass = [(ldap.MOD_REPLACE, 'unicodePwd', [password_value])]
        try:
            self.l.modify_s(user_dn, add_pass)
        except ldap.LDAPError, e:
            self.l.unbind_ext_s()
            print e

        self.l.unbind_ext_s()
