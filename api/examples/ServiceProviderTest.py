import sys
sys.path.append("../src/")
from api.src.ServiceProviderApi import *
from api.examples.TestConf import *

api = ServiceProviderApi('CORPID', 'PROVIDER_SECRET')

try:
    response = api.httpCall(
        SERVICE_PROVIDER_API_TYPE['GET_LOGIN_INFO'],
        {
            'auth_code': 'XXXXXXX',
        })
    print(response)
except ApiException as e:
    print(e.errCode, e.errMsg)
