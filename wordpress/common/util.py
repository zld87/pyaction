import json
import os

import oss2
import requests
import yaml


def push_oss_file(config, file_path):
    """:# 向阿里oss服务器上传文件
     阿里云主账号AccessKey拥有所有API的访问权限，风险很高。
     强烈建议您创建并使用RAM账号进行API访问或日常运维，
     请登录 https://ram.console.aliyun.com 创建RAM账号。
     模块参考文档：
     # https://aliyun-oss-python-sdk.readthedocs.io/en/latest/api.html#id11
    """
    try:
        auth = oss2.Auth(config.OSS_ACCESS_KEY_ID, config.OSS_ACCESS_KEY_SECRET)
        bucket = oss2.Bucket(auth, config.OSS_ENDPOINT, config.OSS_BUCKET_NAME)
        img_name = os.path.basename(file_path)
        bucket.put_object_from_file(img_name, file_path)  # 上传文件
        jpg_url = bucket.sign_url('GET', img_name, 30 * 60)  # 30分钟有效

    except Exception:  # 异常返回None
        return False

    else:
        return jpg_url  # 正常返回jpg_url


def now(scheme="%Y-%m-%d"):
    """:获取当前系统时间
     参考官方文档：
     https://docs.python.org/zh-cn/3/library/datetime.html
    ?highlight=strftime#strftime-strptime-behavior
    """
    import datetime
    generated = datetime.datetime.now().strftime(scheme)
    return generated


def load_yaml(yaml_file):
    """加载 yaml 文件并检查文件内容格式"""
    with open(yaml_file, mode="rb") as stream:
        try:
            yaml_content = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as ex:
            err_msg = f"YAMLError:\nfile: {yaml_file}\nerror: {ex}"
            raise err_msg

        return yaml_content


def get_pram(url_txt, key):
    """ 根据参数名获取url中对应的参数值
    :param url_txt: 具体url字符串
    :param key: 参数名
    :return: 参数值
    """
    from urllib.parse import parse_qs, urlparse
    param_dict = parse_qs(urlparse(url_txt).query)
    return param_dict[key][0]


def req_db(url, *, method, headers, payload, expected):
    if 'POST' in method:
        response = requests.request(
            'POST', url,
            headers=headers,
            data=json.dumps(payload)
        )
    if 'GET' in method:
        response = requests.request(
            'GET', url,
            headers=headers,
            params=payload,
        )
    # 如果回放请求的状态码和数据库中预期的状态一致就返回True 反之返回False
    return True if response.status_code == int(expected) else False


# 自动下载chrome 为utils脚本所在的路径。
def get_driver(comm_driver_path):
    from webdriver_manager.chrome import ChromeDriverManager
    import shutil
    down_driver_path = ChromeDriverManager().install()
    return shutil.move(down_driver_path, comm_driver_path)