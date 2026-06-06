#coding=utf-8
import zmq, time, random
import copy, os, json
from threading import Thread
from datetime import datetime

num = 1
# 故障物编号
id = 0
LB_json_load = None
# LB总共次数
LB_range_index = 0
# 获取LB次数
get_lb_count = 0
emb_file = r'/Users/zhouliudong/date/date/LB.json'
# 故障代码
fault_code = ['1-1-20', '1-1-31', '2-1-1', '2-1-2', '2-1-3', '2-1-4', '2-1-5', '3-1-1', '3-1-10', '5-1-1', '5-1-2']

# LB_out_file = r'/Users/zhouliudong/date/fulldata_L58ZC5VC9ND003096.json'


# 获取经纬度
def get_lB():
    with open(emb_file, 'r', encoding='utf-8') as f:
        json_load_date = json.load(f)
        LB_Len = len(json_load_date)

    return json_load_date, LB_Len




# 障碍物坐标信息
def outpoint():
    num = random.randint(3, 6)
    point_num = num
    outlinepoint = []
    LRrandom = ['left', 'right']
    if random.choice(LRrandom) == 'left':
        while num > 0:
            X1 = random.randint(10, 30)
            Y1 = random.randint(10, 30)
            left = {'X': X1, 'Y': Y1}
            outlinepoint.append(left)
            num -= 1
    else:
        while num > 0:
            X2 = random.randint(-20, -5)
            Y2 = random.randint(-20, -5)
            right = {'X': X2, 'Y': Y2}
            outlinepoint.append(right)
            num -= 1
    return point_num, outlinepoint

# point_num, OUTLINEPOINT = outpoint()
# print(point_num, OUTLINEPOINT)


def msg(count, default_msg, b_Start):
    global id
    global LB_json_load
    global LB_range_index
    global get_lb_count

    if count == 5:
        default_msg = {
            "TYPE": "REP_HMIRunStatus",
            'time': str(format(time.time(), '.0f')),
            "DATA": {
                    # 辅助功能：0为未开启，1为倒垃圾，2为充电，3为加水。
                    "AUXOPERATE": random.choices([0, 1, 2, 3], weights=[1, 10, 10, 10], k=1)[0],
                     # 车辆档位， 0为P档，1为N档，2为R档，3为D档。
                     "GEAR": random.choices([0, 1, 2, 3], weights=[1, 1, 1, 10], k=1)[0],
                     # 车辆模式：1 自动驾驶 2 本地驾驶 3 远程遥控。
                     "MODE": 2,
                     # 车辆自检状态：0为检测中，1为自检完成。
                     "RUNSTATE": random.choices([0, 1], weights=[1, 1], k=1)[0],
                     # 清扫作业启动状态：0为未清扫，1为清扫。（后续细分清扫模式可扩展）
                     "SWEEP": random.choices([0, 1], weights=[10, 5], k=1)[0],
                     # 红绿灯识别结果：0为未识别，1为绿灯，2为黄灯，3为红灯。
                     "TRAFFICLIGHT": random.choices([0, 1, 2, 3], weights=[10, 5, 1, 10], k=1)[0],
                     # 转向信号，0为直行，1为左转，2为右转。
                     "TURNROUND": random.choices([0, 1, 2], weights=[10, 1, 1], k=1)[0],
                     # 车速，单位为km/h
                     "VCAR": random.randint(10, 30),
                     # 启/停自动驾驶信号，false为停止，true为启动。
                     "bStart": b_Start,
                     # 车辆故障的故障码，多个故障码之间用“|”符号隔离。
                     "ERROR": ""
                     }
        }


    default_msg['time'] = str(format(time.time(), '.0f'))
    default_msg['DATA']['OBSTACLES'] = []
    # 偏航角：范围 -90度到90度
    default_msg['DATA']["DirectionAngle"] = float(format(random.uniform(-90, 90), '.1f'))




    if b_Start and default_msg['DATA']['RUNSTATE'] == 1:
        default_msg['DATA']['bStart'] = b_Start
        default_msg['DATA']['MODE'] = 1
    else:
        default_msg['DATA']['bStart'] = b_Start
        default_msg['DATA']['MODE'] = 2

    if get_lb_count == LB_range_index:
        LB_json_load, LB_range_index = get_lB()
        get_lb_count = 0
        LB_date = LB_json_load[get_lb_count]
        L = LB_date['longitude']
        B = LB_date['latitude']
        heading_Angle = LB_date['headingAngle']
        default_msg['DATA']['L'] = L
        default_msg['DATA']['B'] = B
        default_msg['DATA']['headingAngle'] = heading_Angle

        get_lb_count += 1
    else:
        LB_date = LB_json_load[get_lb_count]
        L = LB_date['longitude']
        B = LB_date['latitude']
        heading_Angle = LB_date['headingAngle']
        default_msg['DATA']['L'] = L
        default_msg['DATA']['B'] = B
        default_msg['DATA']['headingAngle'] = heading_Angle

        get_lb_count += 1

    # 设置是否有故障
    if is_fault := random.choices([True, False], weights=[1, 1], k=1)[0]:
        fluat_codes = ''
        fault_count = random.choices(fault_code, weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=random.randint(1, 3))
        for fluat_code in fault_count:
            fluat_codes = fluat_codes + fluat_code + '|'
        default_msg['DATA']['ERROR'] = fluat_codes.rstrip('|')
    else:
        default_msg['DATA']['ERROR'] = ''




    # 设置障碍物数量
    for i in range(1, random.randint(2, 5)):
        id += 1
        point_num, outlinepoint = outpoint()
        olp = {'ID': id, 'OUTLINEPOINTNUM': point_num, 'OUTLINEPOINTS': outlinepoint}
        default_msg['DATA']['OBSTACLES'].append(olp)


    return default_msg



# msg = msg()
# print(msg)


def Zmq_repServer():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:8900')
    # socket.connect("tcp://localhost:8800")

    # 客户端必须要先发送消息，然后在接收消息
    global num
    default_msg = None
    # socket.recv_json()
    # msg1 = msg(count=20, default_msg=default_msg, b_Start=False)
    # socket.send_json(msg1)
    # print(msg1)
    try:
        while True:
            # 控制msg基础信息变更
            count = 5
            while count > 0:
                message = socket.recv_json()
                bStart = bool(message['DATA']['bStart'])
                print(bStart)
                # bStart = bool(str(message['name']))
                # print(bStart, type(bStart))
                print('接受内容     ', end='\n')
                print(message)
                print('接受完毕')
                if len(message) <= 0:
                    print('客户端链接关闭')
                    continue
                print('发送时间' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='\n')
                default_msg = msg(count=count, default_msg=default_msg, b_Start=bStart)
                print(default_msg)
                socket.send_json(default_msg)
                print(f'发送第{num}次完毕')
                count -= 1
                num += 1
                time.sleep(10)

    except Exception as error:
        print(error)

    finally:
        socket.close()



# def Zmq_pubServer(topic: str):
#     context = zmq.Context()
#     socket = context.socket(zmq.PUB)
#     socket.bind("tcp://*:5555")
#
#     print("发布者启动.....")
#     time.sleep(2)
#     # for i in range(1000):
#     tempterature = random.randint(-10, 40)
#     message = "我是publisher！今日温度{}".format(tempterature)
#     socket.send_string(f'{topic} {message}')



if __name__ == '__main__':
    # topic = 'seasonTopic'
    while True:
        zs = Thread(target=Zmq_repServer)
        zs.start()
        zs.join()
