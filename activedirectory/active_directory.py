from ldap3 import Connection, MODIFY_REPLACE


class ActiveDirectory(Connection):

    def __init__(self, server, base_dn, admin_username, admin_password):
        self.baseDN = base_dn
        super(ActiveDirectory, self).__init__(server=server, user=admin_username, password=admin_password, auto_bind=True)
        self.start_tls()

    def formatted_search(self, search_filter):
        self.search(self.baseDN, search_filter, attributes=self.attributes)
        return self.response[0]

    def search_by_account_name(self, account_name):
        search_filter = "(&(objectCategory=Person)(objectClass=User)(samaccountname=" + account_name + "))"
        return self.formatted_search(search_filter)

    def search_by_user_dn(self, user_dn):
        search_filter = "(distinguishedname=" + user_dn +")"
        return self.formatted_search(search_filter)

    def unlock_account(self, account_name):
        return self.modify(dn=self.get_user_dn(account_name=account_name),changes={'lockouttime': [MODIFY_REPLACE, [0]]})

    def get_user_dn(self, account_name):
        return self.search_by_account_name(account_name).get('dn')

    def change_password(self, account_name, new_password):
        return self.extend.microsoft.modify_password(self.get_user_dn(account_name=account_name), new_password, None)

    # def __del__(self):
        # print('unbind')
        # self.unbind()

    @property
    def attributes(self):
        return  [
            'samaccountname',
            'distinguishedname',
            'cn',
            'givenname',
            'displayname',
            'personalTitle',
            'sn',
            'company',
            'employeeid',
            'employeetype',
            'division',
            'department',
            'title',
            'physicaldeliveryofficename',
            'extensionattribute13',
            'telephonenumber',
            'mobile',
            'mail',
            'msrtcsip-line',
            'bbct-slacode',
            'bbct-costcentre',
            'memberof',
            'msexchextensioncustomattribute5',
            'msexchhidefromaddresslists',
            'lastlogon',
            'useraccountcontrol',
            'whenchanged',
            'whencreated',
        ]