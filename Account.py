import requests

class Account:
    """ conainer for user account data """

    __URL = "http://api.scrumsaga.com/v1"
    __pathLogin = "/login"
    __pathViewData = "/acctData"
    __pathUpdateData = "/acctDataUpdate"
    __pathRmData = "/acctDataRm"
    __pathViewLicense = "/acctLicense"

    def __init__(self, acct_email, acct_password):
        
        self.acct_email = acct_email
        self.acct_password = acct_password
        self.token = 'token'

    def login(self):
        URI = Account.__URL +  Account.__pathLogin
        payload = {"email":self.acct_email, "password":self.acct_password}
        try:
            r = requests.post(URI, data=payload)
            self.token = r.json()['token']
            print(r.json()['msg'])
        except:
            print('there was a problem')

    def view_data(self):
        URI = Account.__URL +  Account.__pathViewData
        hdr={'Authorization': 'JWT '+self.token }
        try:
            r = requests.post(URI, headers=hdr)
            print( r.json()['data'] )
        except:
            print('there was a problem')

            