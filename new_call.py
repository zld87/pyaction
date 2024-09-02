from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import random
import ssl, sys
import requests
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
from dateutil.rrule import *
import time



ssl._create_default_https_context = ssl._create_unverified_context

#使用腾讯云发送手机6位随机验证码
class TestQCloudSMS(object):
    def __init__(self, phone_num):
        self.appid = '1400817774'
        self.appkey = '60954ac02b83b3a79838108a45b001ac'
        self.phone_num = phone_num
        self.sign = '过来兜兜公众号'

    def make_code(self):
        code = ''
        for item in range(6):
            code += str(random.randint(0, 9))
        return code

    def send_msg(self, temp_id):
        ssender = SmsSingleSender(self.appid, self.appkey)
        try:
            rzb = ssender.send_with_param(86, self.phone_num, temp_id, [self.make_code()], sign=self.sign, extend='', ext='')
            print(rzb)
        except HTTPError as http:
            print("HTTPError", http)
        except Exception as e:
            print(e)


def sendmsg():
    phone_num = ['13916843740']
    temp_id = [1785827, 1785476]
    sendmsg = TestQCloudSMS(random.choices(phone_num)[0])
    sendmsg.send_msg(random.choices(temp_id)[0])


if __name__ == '__main__':
    while True:
        time_now = datetime.now().strftime("%H:%M:%S")
        start_time = parse("00:00:00").strftime("%H:%M:%S")
        end_time = parse("16:20:00").strftime("%H:%M:%S")
        if time_now > start_time and time_now < end_time:
            for i in range(5):
                inter = random.randint(5, 10)
                sendmsg()
                print(inter)
                time.sleep(inter*60)
        time.sleep(60)

    #sendmsg.send_msg(random.choices(temp_id)[0])
    # 需传入发送短信的手机号，单发 sendmsg.send_msg


sys.argv[0]
# 13917629498
# hearder = {
#     "Accept": "application/json;charset=utf-8",
#     "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
# }
#
# url = "https://sms.yunpian.com/v2/sms/single_send.json"
#
# new_data = {
#     "apikey": "d0fe14c49144fa0c2f770aaec77e57a1",
#     "mobile": "13916843740",
#     "text": "哈哈 你好"
# }
#
# resule = requests.post(url=url, headers=hearder, json= new_data)
# print(resule.text)


