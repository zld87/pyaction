from jira import *

#jira访问
server='http://jira.lechebang.com/'
# 用户名密码以元祖的方式传递。uesrname、passwd填写真实的账号密码
jiraClinet=JIRA(server=server,basic_auth=('zhouliudong','lcb@1234'))

jiraids=jiraClinet.projects()
print(jiraids)

for jiraid in jiraids:
    key=jiraid.key
    name=jiraid.name
    #print(dir(jiraid))
    print(key,name)



# 创建单个issue
issue_dict = {
    # key 是项目空间的关键字，将issue记录到此空间
    'project': {'key': 'TEST'},
    'issuetype': {'name': 'Task'},
    'summary': '测试自动提交',
    'description': '描述',
    'assignee': {'name': 'zhouliudong'},
    'customfield_10601':{'value':'乐车邦'},
    # 'priority': {'id': 3},
    # 'customfield_10403':{'value':'研发中心'},
    # 'customfield_11349':{'value':'业务需求'}
}
#返回 issueId 创建问题
#issue_id=jiraClinet.create_issue(issue_dict)

project=jiraClinet.project(10407)
print(project.raw)
print(dir(project))

## 查询issue信息，传入参数issueId
issus=jiraClinet.issue('TEST-23')
#获取问题工作流
print(jiraClinet.transitions(issue=issus))
#修改问题状态
#jiraClinet.transition_issue(issus,4)
print(issus.fields.status)
print(dir(issus))
#添加附件
#jiraClinet.add_attachment(issue=issus,attachment='/Users/zhouliudong/Pictures/测试图片/742922242-1.jpg')
#添加评论
#jiraClinet.add_comment(issue=issus,body='zldmelove')
#添加关注者
#jiraClinet.add_watcher(issue=issus,watcher='gaoman')
#添加评论
#jiraClinet.add_comment(issus,"test1")
#查看所有评论
pingluns=jiraClinet.comments(issue=issus)
print(dir(pingluns))
print(pingluns)
'''for pinglun in pingluns:
    print(pinglun.id)
    print(dir(pinglun))
    pinglun.delete()'''
#pinglun1=jiraClinet.comment(issue=issus,comment=pinglun.id)
#pinglun1.delete()
#issus.delete()
#fields=issus.id
#print(pinglun1.body)
#print(dir(pinglun1))
#print(issus.fields.customfield_10601)
