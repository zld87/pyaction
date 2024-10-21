import re
from mitmproxy import ctx

def request(flow):
    #if re.match(r'https://m.baidu.com', flow.request.url):
        #flow.request.headers['User-Agent'] = 'zldcccc'
        #flow.request.url = '123'
    print(dir(flow))
    ctx.log.info(flow.request.json)
    ctx.log.error("bbbbb" + str(flow.response))


