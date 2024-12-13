from datetime import datetime
from mitmproxy import ctx
from conrds import *

# def response(flow):
#     if r'user/captcha/generate' in flow.request.url:
#         # id = flow.response.json()['data']['id']
#         # print(id)
#         print(flow.request.url)
#         url = 'https://www.163.com'
#         flow.request.url = url
#         # print(flow.request.headers.add(('name', 'zhouliudong')))
#         print(1111111111111111111111111111111111111111111111111111)
#         print(flow.response.text)
#
#
#     if 'https://www.baidu.com' in flow.request.url:
#         print('这是百度响应+111111111111111111111111111111111')
#         print(flow.response.headers)
#
#     if 'https://www.163.com' in flow.request.url:
#         url = 'https://www.baidu.com'
#         flow.request.url = url
#         print('这是163请求头+111111111111111111111111111111111')
#         print(flow.request.headers)
#         print('这是163响应+111111111111111111111111111111111')
#         print(flow.response.headers)
#
#     # if 'https://www.baidu.com' in flow.request.url:
#     #     print('这是百度响应+111111111111111111111111111111111')
#     #     print(flow.response.headers)

# numb = 1

def response(flow):
    # global numb
    if r'user/captcha/check' in flow.request.url:
        pic_id = flow.request.query.get('id')
        print(f'这是获取的pic_id:  ' + pic_id, '已经存入redis')

        # rc = Redis_Cli().con_type()
        # rc.set('pic_name', pic_id)
