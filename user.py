class User: 
    '''
    class that generates new instances of users accounts
    '''
    user_list = []#user list
    def save_user(self):
        '''
        save_user method saves users
        '''
        User.user_list.append(self)