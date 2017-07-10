import ldap
from config import LDAP_PASSWORD, LDAP_USERNAME

class ActiveDirectory(object):
    baseDN = 'DC=national,DC=core,DC=bbc,DC=co,DC=uk'
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None

    def __init__(self, accountName):
        self.l = ldap.initialize("ldap://ldap.national.core.bbc.co.uk:3268")
        self.l.simple_bind(LDAP_USERNAME, LDAP_PASSWORD)
        self.searchFilter = "(&(objectCategory=Person)(objectClass=User)(samaccountname="+accountName+"))"
    def main(self):
        try:
            ldap_result_id = self.l.search(self.baseDN,  self.searchScope,  self.searchFilter,  self.retrieveAttributes)
            result_set = []
            while 1:
                result_type, result_data = self.l.result(ldap_result_id, 0)
                if (result_data == []):
                    break
                else:
                    ## here you don't have to append to a list
                    ## you could do whatever you want with the individual entry
                    ## The appending to list is just for illustration.
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)
            print result_set
        except ldap.LDAPError, e:
            print e
        self.l.unbind()
