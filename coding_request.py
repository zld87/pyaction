import urllib.request
import requests
import json
from dateutil.rrule import *
from dateutil.parser import parse
import time
import os
#34a08dc42899fadb97098ef74be023050e7ae0a5 全部权限
#6f49725d4b02f2a292a810984f4f9a45c8695fec 自己的账号
#84b901800da9735a180352ba3f8facb3e6296cde 张利强账号
header = {"Authorization": "token 6f49725d4b02f2a292a810984f4f9a45c8695fec"}
url = "https://di-matrix.coding.net/open-api"

# 获取用户个人信息
DescribeCodingCurrentUser = {"Action": "DescribeCodingCurrentUser"}
# 查询成员所在项目列表
DescribeUserProjects = {"Action": "DescribeUserProjects", 'UserId': 8409987}
# 查询项目协同事项事务事实表
DescribeIssuesDataset = {"Action": "DescribeIssuesDataset", 'PageNumber': 1, "PageSize": 10}
# 删除事项
i =[2140, 2151, 2150, 2149, 2148, 2147, 2146, 2145, 2144, 2143, 2142, 2141]
DeleteIssue = {"Action": "DeleteIssue", "ProjectName": "Di-AIOps", "IssueCode": i}
# 事项列表（新）
DescribeIssueListWithPage = {"Action": "DescribeIssueListWithPage", "ProjectName": "Di-AIOps", "IssueType": "DEFECT", "PageNumber": 1, "PageSize": 500}
DescribeProjectIssueTypeList = {"Action": "DescribeProjectIssueTypeList","ProjectName": "Di-AIOps"}


#创建事项
CreateIssue = {
    "Action": "CreateIssue",
    "ProjectName": "Di-AIOps",
    "Type": "DEFECT",
    "Name": "Auto——test缺陷1",
    "Priority": "1",
    "Description": "123",
    "AssigneeId": 8409987,
    "DefectTypeId": 32008707,
    "CustomFieldValues": [
        {
            "Id": 36813120,
            "content": "364043"
        }
    ]
}

for y in range(2087, 2090):
    DeleteIssue = {"Action": "DeleteIssue", "ProjectName": "Di-AIOps", "IssueCode": y}
    #requests.session()
    resp = requests.post(url=url, json=DeleteIssue, headers=header)
    print(resp.json())
#print(resp.json()['Response']['User']['Id'])
#print(json.loads(resp.text)["Response"]['Data']['List'])
'''for i in json.loads(resp.text)["Response"]['Data']['List']:
    if i["Name"] == '123':
        print(i['Code'])'''


'''e = list(rrule(MONTHLY, dtstart=parse('2018.5.1'), until=parse('2018.8.7')))  # 按月输出
print(e)
for i in e:
    print(i)'''

open("rematch1.py", "w+")

requests.request('post', url=url, headers=header)
