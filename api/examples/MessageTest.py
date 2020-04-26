import sys
import random
sys.path.append("../src/")
from api.src.CorpApi import *
from api.examples.TestConf import *
from api.src.AbstractApi import ApiException

api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try:
    response = api.httpCall(
        CORP_API_TYPE['MESSAGE_SEND'],
        {
            "touser": "ZhuShengBen",
            "agentid": 1000002,
            'msgtype': 'text',
            'climsgid': 'climsgidclimsgid_%f' % (random.random()),
            'text': {
                'content': '方法论',
            },
            'safe': 0,
        })
    print(response)
except ApiException as e:
    print(e.errCode, e.errMsg)
