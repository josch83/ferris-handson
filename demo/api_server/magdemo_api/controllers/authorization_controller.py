import os
import re
from ferris import Keycloak
from magdemo_api.models.sqla_models import roles

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

 # Allow an environment var to switch off security
 # But keep security, if it isn't set, or set to anything whose lower() isn't false
SECURITY = not bool(os.environ.get('SECURITY', 'True').lower() == 'false')
# print('SECURITY =', SECURITY,flush=True)
if SECURITY:
    kc = Keycloak()
else:
    try:
        kc = Keycloak()
    except:
        print('WARNING failed to connect to keycloak, keycloak-token will produce errors', flush=True)
        kc = None
    print('WARNING SECURITY checking of token is switched off', flush=True)


def check_sso_auth(access_token):
    if isinstance(access_token, bytes):
        access_token = access_token.decode('utf-8')
    prefix = "Bearer "
    if access_token.startswith(prefix):
        access_token = access_token[len(prefix):]

    # For easier testing, allow an email address as token
    if (not SECURITY) and re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+[.][a-z]{1,3}$", access_token):
        # Return a fake token using the  given email to lookup user.id
        return {
            'jti': 'db5ca30a-c50d-4c57-a3fd-aaa3c006583b',
            'exp': 1653295969,
            'nbf': 0,
            'iat': 1653295669,
            'iss': 'Test Issuer',
            'aud': 'account',
            'sub': '1638ea38-8a17-4e58-8f78-5c3ae17a1869',
            'typ': 'Bearer',
            'azp': 'test-client',
            'auth_time': 0,
            'session_state': '8dca8441-6600-4baa-8081-8fffecec896e',
            'acr': '1',
            'allowed-origins': ['*'],
            'realm_access': {'roles': ['offline_access', 'uma_authorization', 'user']},
            'scope': 'openid email profile',
            'email_verified': True,
            'roles': roles,
            'name': 'Test Test',
            'preferred_username': access_token,
            'given_name': 'Test',
            'family_name': 'Test',
            'email': access_token,
        }

    return kc.check_token(access_token)
