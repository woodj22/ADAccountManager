import ldap
from config import LDAP_PASSWORD, LDAP_USERNAME

class ActiveDirectory():
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None

    def __init__(self):
        self.l = ldap.initialize("ldap://ldap.national.core.bbc.co.uk:3268")
        self.l.set_option(ldap.OPT_REFERRALS, 0)
        self.l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
        self.l.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
        self.l.set_option(ldap.OPT_X_TLS_DEMAND, True)
        self.l.set_option(ldap.OPT_DEBUG_LEVEL, 255)
        self.l.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)

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


    def change_password(self, user_dn ,new_password):
        #For test purposes i have spoofed the user_dn and new_password values
        user_dn = "CN=joe.wood,OU=london,OU=deputy director general group,OU=Atos London,OU=Roaming,OU=Interactive,OU=Users,OU=Standard,OU=Business,DC=national,DC=core,DC=bbc,DC=co,DC=uk"
        new_password = "HelloMe123"
        unicode_pass = unicode('\"' + str(new_password) + '\"', 'iso-8859-1')
        print unicode_pass
        password_value = unicode_pass.encode('utf-16-le')
        print password_value
        add_pass = [(ldap.MOD_REPLACE, 'unicodepwd', password_value)]
        print add_pass
        try:
            self.l.passwd(user=user_dn, oldpw=None, newpw=new_password)
        except ldap.LDAPError, e:
            print e
        self.l.unbind_ext_s()