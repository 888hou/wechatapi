import sys

sys.path.append("../src/")
from api.src.CorpApi import *
from api.src.AbstractApi import *
from api.examples.TestConf import *

api = CorpApi(TestConf['CORP_ID'], TestConf['CONTACT_SYNC_SECRET'])

try:
    # response = api.httpCall(
    #     CORP_API_TYPE['USER_CREATE'],
    #     {
    #         "userid": "apiceshi",
    #         "name": "api测试",
    #         "alias": "randolph",
    #         "mobile": "13970970002",
    #         "department": [1],
    #         "order": [2],
    #         "position": "技术",
    #         "gender": "1",
    #         "email": "yinggang.cai@hand-china.com",
    #         "is_leader_in_dept": [0],       # 是不是部门领导
    #         "enable": 1,
    #         "avatar_mediaid": "",           # 上传头像的id，默认空
    #         "telephone": "020-123456",
    #         "address": "上海市青浦区豪车汇10F",
    #         "main_department": 1,
    #         "to_invite": "",            # 默认邀请
    #         "external_position": "技术顾问",
    #     })
    # print(response)

    response = api.httpCall(
            CORP_API_TYPE['USER_GET'],
            {
                'userid': 'apiceshi',
            })
    print(response)

    # response = api.httpCall(
    #         CORP_API_TYPE['USER_DELETE'],
    #         { 
    #             'userid': 'apiceshi',
    #         })
    # print(response)

except ApiException as e:
    print(e.errCode, e.errMsg)

    response = api.httpCall(
        CORP_API_TYPE['USER_DELETE'],
        {
            'userid': 'apiceshi',
        })
    print(response)
