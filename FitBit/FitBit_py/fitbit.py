"""
A Python library for accessing the FitBit API.

This library provides a wrapper to the FitBit API and does not provide storage of tokens or caching if that is required.

Most of the code has been adapted from: https://groups.google.com/group/fitbit-api/browse_thread/thread/0a45d0ebed3ebccb

5/22/2012 - JCF - Updated to work with python-oauth2 https://github.com/dgouldin/python-oauth2
10/22/2015 - JG - Removed use of oauth2 library (singing is not necessary anymore),
                  updated to use /oauth2/ authentication infrastructure to get access to more stats.
"""
import os, base64, requests, urllib

class Fitbit():

    # All information must be as on the https://dev.fitbit.com/apps page.
    CLIENT_ID     = ''
    CLIENT_SECRET = ''
    REDIRECT_URI  = 'http://localhost:8000/signin'

    # Decide which information the FitBit.py should have access to.
    # Options: 'activity', 'heartrate', 'location', 'nutrition',
    #          'profile', 'settings', 'sleep', 'social', 'weight'
    #API_SCOPES    = ('activity', 'heartrate', 'location', 'nutrition', 'profile', 'settings', 'sleep', 'social', 'weight')
    API_SCOPES    = ('activity', 'profile')

    # These settings should probably not be changed.
    API_SERVER    = 'api.fitbit.com'
    WWW_SERVER    = 'www.fitbit.com'
    AUTHORIZE_URL = 'https://%s/oauth2/authorize' % WWW_SERVER
    TOKEN_URL     = 'https://%s/oauth2/token' % API_SERVER

    def GetAuthorizationUri(self):

        # Parameters for authorization, make sure to select 
        params = {
            'client_id': self.CLIENT_ID,
            'response_type':  'code',
            'scope': ' '.join(self.API_SCOPES),
            'redirect_uri': self.REDIRECT_URI
        }

        # Encode parameters and construct authorization url to be returned to user.
        urlparams = urllib.urlencode(params)
        return "%s?%s" % (self.AUTHORIZE_URL, urlparams)

    # Tokes are requested based on access code. Access code must be fresh (10 minutes)
    def GetAccessToken(self, access_code):

        # Construct the authentication header
        auth_header = base64.b64encode(self.CLIENT_ID + ':' + self.CLIENT_SECRET)
        headers = {
            'Authorization': 'Basic %s' % auth_header,
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        # Paramaters for requesting tokens (auth + refresh)
        params = {
            'code': access_code,
            'grant_type': 'authorization_code',
            'client_id': self.CLIENT_ID,
            'redirect_uri': self.REDIRECT_URI
        }

        # Place request
        resp = requests.post(self.TOKEN_URL, data=params, headers=headers)
        status_code = resp.status_code
        resp = resp.json()

        if status_code != 200:
            raise Exception("Something went wrong exchanging code for token (%s): %s" % (resp['errors'][0]['errorType'], resp['errors'][0]['message']))

        # Strip the goodies
        token = dict()
        token['access_token']  = resp['access_token']
        token['refresh_token'] = resp['refresh_token']

        return token

    # Get new tokens based if authentication token is expired
    def RefAccessToken(self, token):

        # Construct the authentication header
        auth_header = base64.b64encode(self.CLIENT_ID + ':' + self.CLIENT_SECRET)
        headers = {
            'Authorization': 'Basic %s' % auth_header,
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        # Set up parameters for refresh request
        params = {
            'grant_type': 'refresh_token',
            'refresh_token': token['refresh_token']
        }

        # Place request
        resp = requests.post(self.TOKEN_URL, data=params, headers=headers)

        status_code = resp.status_code
        resp = resp.json()

        if status_code != 200:
            raise Exception("Something went wrong refreshing (%s): %s" % (resp['errors'][0]['errorType'], resp['errors'][0]['message']))

        # Distil
        token['access_token']  = resp['access_token']
        token['refresh_token'] = resp['refresh_token']

        return token

    # Place api call to retrieve data
    def ApiCall(self, token, apiCall='/1/user/-/activities/log/steps/date/today/1d.json'):
        # Other API Calls possible, or read the FitBit documentation for the full list
        # (https://dev.fitbit.com/docs/), e.g.:
        # apiCall = '/1/user/-/devices.json'
        # apiCall = '/1/user/-/profile.json'
        # apiCall = '/1/user/-/activities/date/2015-10-22.json'

        headers = {
            'Authorization': 'Bearer %s' % token['access_token']
        }

        final_url = 'https://' + self.API_SERVER + apiCall

        resp = requests.get(final_url, headers=headers)

        status_code = resp.status_code

        resp = resp.json()
        resp['token'] = token

        if status_code == 200:
            return resp
        elif status_code == 401:
            print "The access token you provided has been expired let me refresh that for you."
            # Refresh the access token with the refresh token if expired. Access tokens should be good for 1 hour.
            token = self.RefAccessToken(token)
            self.ApiCall(token, apiCall)
        else:
            raise Exception("Something went wrong requesting (%s): %s" % (resp['errors'][0]['errorType'], resp['errors'][0]['message']))

z = Fitbit()
auth_url = z.GetAuthorizationUri()
print("\nRemove '+' from AUTH URL and paste on the browser to get access token: ")
print(auth_url)

# TODO: 
# 1. From auth_url remove '+' from the Scope
#    https://www.fitbit.com/oauth2/authorize?scope=a+c+t+i+v+i+t+y&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fsignin&response_type=code&client_id=
# 2. Copy the auth_url in the browser. It will ask permissions to access Fitbit. Once you give ok, URL of  the new page will have access_code
# 3. Access code is all numbers and remove the last few characters from #
# 4. Same URL below
#    http://localhost:8000/signin?code=63ba7c4e264b9f70aefa1699a9959d2101383484#_=_
access_code = '008288d790b3a975d8db6c4cac828c5da9845dcc'
print("\nACCESS CODE:")
print(access_code)
token = z.GetAccessToken(access_code)
print("\nACCESS TOKEN:")
print(token)
# {'access_token': u'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyN1g2MlQiLCJhdWQiOiIyMjhHTUoiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3YWN0IiwiZXhwIjoxNDk5MTg1MTg5LCJpYXQiOjE0OTkxNTYzODl9.0wO8puAfAyWOjiTZmRBBNTMDhtVvehCx5zujeq4-6M8', 'refresh_token': u'dd019e8051f9de18554152c16fe14c9236a53cff620a881e52c4788c77a4685a'}

# Sample API call
response = z.ApiCall(token, '/1/user/-/profile.json')
