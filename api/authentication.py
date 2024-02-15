from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthenticationAugmented(BaseTokenAuth):
    # ! Standard Convention
    keyword = 'Bearer'