# -*- coding: utf-8 -*-

import os
import json
from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models


app_key_ = os.environ["APP_KEY"] 
app_secret_ = os.environ["APP_SECRET"] 
robot_code_ = os.environ["ROBOT_CODE"] 

def vget(a,b,c):
    try:
        return a[b]
    except:
        return c
class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = "https"
        config.region_id = "central"
        return dingtalkrobot_1_0Client(config)

    @staticmethod
    def getToken():
        config = open_api_models.Config()
        config.protocol = "https"
        config.region_id = "central"
        client = dingtalkoauth2_1_0Client(config)

        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=app_key_,
            app_secret=app_secret_,
        )
        try:
            token = client.get_access_token(
                get_access_token_request).body.access_token
            print(token)
            return token
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    def main(data) -> None:
        try:
            json.dumps(data)
            par = data
        except:
            try:
                par = json.loads(data)
            except Exception as err:
                par = json.loads('{"msg":'+data+'}')
        print(par)
        token = Sample.getToken()
        msgtype = vget(par,'msgtype','sampleText')
        if msgtype == "sampleText":
            msgs = '{"content":"'+vget(par,'msg', par)+'"}'
        if msgtype == "sampleImageMsg":
            msgs = '{"photoURL":"'+vget(par,'msg', 'Nokey')+'"}'
        if msgtype == "sampleLink":
            msgs = '{"text":"点击跳转链接","title":"接口消息","picUrl":"@lADOADmaWMzazQKA"\
                ,"messageUrl":"' + vget(par,'url', 'https://www.lorzl.cn')+'"}'
        if msgtype == "sampleMarkdown":
            msgs = '{"title": "Markdown消息","text": "'+vget(par,'msg', 'Nokey')+'"}'
        if msgtype == "sampleActionCard":
            msgs = '{"title": "有新消息啦","text":"' + vget(par,'msg', 'Nokey') + '",\
                "singleTitle":"查看详情","singleURL": "' + vget(par,'url', 'https://www.lorzl.cn')+'"}'
        if msgtype == "sampleActionCard2":
            msgs = '{"title": "有新消息啦","text":"' + vget(par,'msg', 'Nokey') + '",\
                "actionTitle1":"按钮1","actionURL1": "' + vget(par,'url', 'https://www.lorzl.cn')+'",\
                "actionTitle2":"按钮2","actionURL2": "' + vget(par,'url1', 'https://www.lorzl.cn')+'"}'
        if msgtype == "sampleAudio":
            msgs = '{"mediaId": "@IR_PADOADmaWnFkfhsisbf4A","duration": "'+vget(par,'msg', 'Nokey')+'"}'

        print(msgs)
        client = Sample.create_client()
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = token
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=robot_code_,
            user_ids=["manager8531"],
            msg_key=msgtype,
            msg_param=msgs,
        )
        try:
            a = client.batch_send_otowith_options(
                batch_send_otorequest,
                batch_send_otoheaders,
                util_models.RuntimeOptions(),
            )
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                print(err.message)
                pass


if __name__ == "__main__":
    a = json.loads('{"msg":"测试","":""}')
    Sample.main(a)
