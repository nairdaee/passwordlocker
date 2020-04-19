class Credential:
    '''
    class that generates new instaces of credentials information
    '''
    credential_list = [] #credential list
    def save_credential(self):
        '''
        save_credential method saves object in credential list
        '''
        Credential.credential_list.append(self)
    def __init__(self,account_name,passkey):
        self.account_name = account_name
        self.passkey = passkey
    @classmethod
    def display_credentials(cls):
        '''
        method that returns credentials of a user
        '''
        return cls.credential_list
    @classmethod
    def delete_credential(cls,account):
        '''
        delete a credential
        '''
        for credential in cls.credential_list:
            if credential.account_name == account:
                return credential