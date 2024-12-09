import datetime
import os
import subprocess
import json
import sys
import time
import requests
import random
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from threading import Thread
import argparse


# FOLDER_PATH = r'D:\data\faultdatagz\faultdatagz'
# OUT_FILE_PATH = r'D:\data\faultdatagz'
# IN_FILE_NAME = os.listdir(FOLDER_PATH)
# print(IN_FILE_NAME)

perf_full_save = "http://192.16.11.11:31316/full/save"
perf_full_saveQB = "http://192.16.11.11:31316/full/saveQB"
perf_fault_save = 'http://192.16.11.11:31316/fault/save'

perf_sweep_saveSweep = 'http://192.16.11.11:31316/sweep/saveSweep'
perf_mixer_saveMixer = 'http://192.16.11.11:31316/mixer/saveMixer'

uat_full_save = "http://192.16.11.11:32135/full/save"
uat_full_saveQB = "http://192.16.11.11:32135//full/saveQB"
uat_fault_save = 'http://192.16.11.11:32135/fault/save'

headers = {'Content-Type': 'application/json;charset=utf-8'}

#搅拌和扫刷造数
def mix_sweep(io_date, work_mix, work_sweep, ws, mix_sweep_count, vin, collec_time):
    if mix_sweep_count == 0:
        if io_date['chargingState'] == 'OUTAGE' and ws == 1:  # 搅拌和扫刷参数
            mix_sweep_count = random.randint(1, 70)  # 搅拌和扫刷次数
            direction = random.randint(0, 2)
            sweep = random.randint(0, 1)
            work_mix = [{"collectTime": collec_time, "direction": direction, "vin": vin}]
            work_sweep = [{"recordTime": io_date["recordTime"],
                      "vin": vin,
                      "workStatus": sweep,
                      "workStatusSweep": sweep}]
            mix_sweep_count -= 1
            return mix_sweep_count, work_mix, work_sweep
        elif io_date['chargingState'] == 'OUTAGE' and ws == 2:  # 搅拌参数
            mix_sweep_count = random.randint(1, 70)
            direction = random.randint(0, 2)
            work_mix = [{"collectTime": collec_time, "direction": direction, "vin": vin}]
            mix_sweep_count -= 1
            return mix_sweep_count, work_mix
        elif io_date['chargingState'] == 'OUTAGE' and ws == 3:  # 扫刷参数
            mix_sweep_count = random.randint(1, 70)
            sweep = random.randint(0, 1)
            work_sweep = [{"recordTime": io_date["recordTime"],
                           "vin": vin,
                           "workStatus": sweep,
                           "workStatusSweep": sweep}]
            mix_sweep_count -= 1
            return mix_sweep_count, work_sweep
        else:
            pass

    elif mix_sweep_count != 0:
        if io_date['chargingState'] == 'OUTAGE' and ws == 1:  # 搅拌和扫刷参数
            work_mix[0]['collectTime'] = collec_time
            work_sweep[0]['recordTime'] = io_date["recordTime"]
            mix_sweep_count -= 1
            return mix_sweep_count, work_mix, work_sweep
        elif io_date['chargingState'] == 'OUTAGE' and ws == 2:  # 搅拌参数
            work_mix[0]['collectTime'] = collec_time
            mix_sweep_count -= 1
            return mix_sweep_count, work_mix
        elif io_date['chargingState'] == 'OUTAGE' and ws == 3:  # 扫刷参数
            work_sweep[0]['recordTime'] = io_date["recordTime"]
            mix_sweep_count -= 1
            return mix_sweep_count, work_sweep
        else:
            pass


#转换时间戳
def get_time_stp(new_time):
    time_Array = time.strptime(new_time, "%Y-%m-%d %H:%M:%S")
    time_stamp = time.mktime(time_Array)
    return time_stamp

#车辆绑定机构
def vin_with_organizationId(in_file, io_date):
    # print(type(in_file))
    if 'HDL7C1GA0P1003607' in in_file or 'L58ZC5VC0ND003214' in in_file:
        io_date['organizationId'] = 88
    elif 'L58ZC5VC4ND003099' in in_file or 'L58ZC5VC2ND003084' in in_file:
        io_date['organizationId'] = 97
    elif 'LEWUMC1B2MF146752' in in_file or 'L58ZC5VCXND003219' in in_file:
        io_date['organizationId'] = 98
    elif 'LEWUMC185MF146765' in in_file or 'LEWUMC187MF146721' in in_file:
        io_date['organizationId'] = 100
        io_date['customerName'] = '托普新能源1号第二分公司'
    elif 'L58ZC5VC9ND003096' in in_file or 'LEWUMC180PF101060' in in_file:
        io_date['organizationId'] = 99
        io_date['customerName'] = '托普新能源2号有限公司'

    # print(io_date)
    return io_date

def fault_Level(io_date):
    if io_date['thirdSourceType'] == 1:
        io_date['faultLevel'] = str(random.randint(1,3))
    elif io_date['thirdSourceType'] == 2:
        io_date['faultLevel'] = str(random.randint(1, 5))
    else:
        io_date['faultLevel'] = '未定义'
    return io_date

def randem_nember(a, b, long):
    reslut = ''
    for i in range(long):
        reslut += str(random.randint(a, b))
    return reslut


def new_key(io_date):
    for key in list(io_date.keys()):
        # print(key[0].lower())
        new_key = key.replace(key[0], key[0].lower())
        # print(new_key)
        value = io_date.pop(key)
        io_date[new_key] = value
        # print(io_date)
    try:
        subSystem_Number = io_date.pop('subsystemNumber')
        subsystemFrameStart_BatterySeq = io_date.pop('subsystemFramestartBatteryseq')
        io_date['subSystemNumber'] = subSystem_Number
        io_date['subsystemFrameStartBatterySeq'] = subsystemFrameStart_BatterySeq
    except Exception:
        pass
    return io_date


def mileage(io_date, start_mlieages):
    if io_date['operatingState'] == "RUN":
        m_lieages = float(format(random.uniform(0.1, 0.5), '.1f'))
        m_lieages += start_mlieages
        print(m_lieages)
        io_date['mileage'] = m_lieages
        io_date['speed'] = float(random.randint(30, 100))
        return io_date, m_lieages
    else:
        io_date['mileage'] = start_mlieages
        io_date['speed'] = float(0)
        return io_date, start_mlieages







Num = 0


def fault_save():
    FOLDER_PATH = r'D:\data\faultdatagz\faultdatagz'
    OUT_FILE_PATH = r'D:\data\faultdatagz'
    IN_FILE_NAME = os.listdir(FOLDER_PATH)
    type_car = ['清洗车', '扫路车', '垃圾车', '抑灰车', '电动车']
    print(IN_FILE_NAME)

    for in_file in IN_FILE_NAME:
        global Num
        Num += 1
        vehicleNo = "沪Ful" + f'{Num:03}'
        vehicleType = random.choice(type_car)
        emb_file = FOLDER_PATH + '\\' + in_file
        out_flie = OUT_FILE_PATH + '\\' + in_file
        new_time_2 = parse('2024-01-10 14:00:00')
        print(emb_file, out_flie)
        print(vehicleNo)
        print(vehicleType)

        with open(emb_file, 'r', encoding='utf-8') as f:
            #print(len(f.readlines()))
            #for i in f.readlines()[0:2]:
            json_load = json.load(f)
            for io_date in json_load[-1::-1]:
                fault_type_count = ['通用告警', '整车故障', '上装故障']
                # new_time_1 = io_date["time"][0:10] + " " + io_date["time"][11:19]
                tc = relativedelta(minutes=random.randint(20, 300))
                over_t = relativedelta(minutes=random.randint(20, 300))
                # print(new_time)
                # time_stp = format(get_time_stp(new_time), '.0f')
                # time_stp = int(time_stp)
                # print(time_stp)
                io_date.pop("time")
                vin_Code = io_date.pop("vin")
                io_date["occurredDate"] = new_time_2.strftime("%Y-%m-%d %H:%M:%S")
                io_date['vinCode'] = vin_Code
                io_date['vehicleType'] = vehicleType
                if io_date['vinCode'] == 'L58ZC5VC9ND003096':
                    io_date['vehicleNo'] = '沪Ful789'
                elif io_date['vinCode'] == 'LEWUMC180PF101060':
                    io_date['vehicleNo'] = '川A17590D'
                elif io_date['vinCode'] == 'LEWUMC187MF146721':
                    io_date['vehicleNo'] = '豫E01128D'
                else:
                    io_date['vehicleNo'] = vehicleNo
                new_fault_Type = random.choice(fault_type_count)
                # print(fault_Type)
                if new_fault_Type == '上装故障':
                    io_date['faultType'] = new_fault_Type
                    io_date['faultType2'] = random.randint(0, 2)
                    io_date['motorType'] = random.randint(1, 9)
                    io_date['thirdSourceType'] = 2
                elif new_fault_Type == '通用告警':
                    io_date['faultType'] = new_fault_Type
                    io_date['faultType2'] = ''
                    io_date['motorType'] = ''
                    io_date['thirdSourceType'] = 1
                elif new_fault_Type == '整车故障':
                    io_date['faultType'] = new_fault_Type
                    io_date['faultType2'] = ''
                    io_date['motorType'] = ''
                    io_date['thirdSourceType'] = 2
                io_date = vin_with_organizationId(in_file, io_date)
                io_date = fault_Level(io_date)
                if random.randint(1, 2) == 2:
                    remove_Date = new_time_2 + over_t
                    io_date['removeDate'] = remove_Date.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    io_date['removeDate'] = ''
                list_io_data= []
                list_io_data.append(io_date)
                print(type(io_date))
                # print(list_io_data)
                #str_io_data = json.dumps(io_date)
                #print(type(str_io_data))
                try:
                    req = requests.post(url=perf_fault_save, json=list_io_data, headers=headers)
                    print(req.text)
                except Exception as error:
                    print(error)
                else:
                    with open(out_flie, 'a+', encoding='utf-8') as newFile:
                        newFile.write(json.dumps(io_date) + '\n')

                new_time_2 += tc



def full_saveQB(vin):
    FOLDER_PATH = r'D:\data\fulldataqb\fulldataqb'
    OUT_FILE_PATH = r'D:\data\fulldataqb'
    IN_FILE_NAME = os.listdir(FOLDER_PATH)
    print(IN_FILE_NAME)

    for in_file in IN_FILE_NAME:
        if vin in in_file:
            emb_file = FOLDER_PATH + '\\' + in_file
            out_flie = OUT_FILE_PATH + '\\' + in_file
            # new_time_2 = parse('2023-12-02 14:00:00')
            print(emb_file, out_flie)
            software_Version = "31.1." + str(random.randint(80, 99))
            iviVersion = '10.1.' + str(random.randint(80, 99))
            vehicleType = random.randint(1, 14)
            #上装工作状态
            workStatus_count = 0
            Renumber_WorkStatus = 0

            with open(emb_file, 'r', encoding='utf-8') as f:
                #print(len(f.readlines()))
                #for i in f.readlines()[0:2]:
                json_load = json.load(f)
                for io_date in json_load[-1::-1]:
                    new_time_1 = io_date["time"][0:10] + " " + io_date["time"][11:19]
                    # tc = relativedelta(minutes=random.randint(20, 300))
                    # over_t = relativedelta(minutes=random.randint(300, 500))
                    # new_time_2 += tc
                    new_time_3 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    #print(new_time_3)
                    time_stp = format(get_time_stp(new_time_3), '.0f')
                    time_stp = int(time_stp)
                    # print(time_stp)
                    io_date.pop("time")
                    io_date["recordTime"] = time_stp
                    io_date['count'] = random.randint(1, 5)
                    io_date['format'] = random.randint(0, 1)
                    io_date['canId1'] = '0x0C0DE6D0'
                    io_date['canId2'] = '0x0C10E628'
                    io_date['can1No'] = 1
                    io_date['can2No'] = 2
                    io_date['lockLimitStatus'] = randem_nember(0, 1, 3).ljust(8, '0')
                    if workStatus_count == 0:
                        Renumber_WorkStatus = random.randint(0, 1)
                        io_date['workStatus'] = Renumber_WorkStatus
                        ws_count = random.randint(1,100)
                        workStatus_count += 1
                    elif workStatus_count != 0 and workStatus_count < ws_count:
                        workStatus_count += 1
                        io_date['workStatus'] = Renumber_WorkStatus
                    elif workStatus_count >= ws_count:
                        workStatus_count = 0
                        io_date['workStatus'] = Renumber_WorkStatus
                    io_date['softwareVersion'] = software_Version
                    io_date['vehicleType'] = vehicleType
                    io_date['iviVersion'] = iviVersion
                    io_date['vehicleType'] = vehicleType
                    io_date['faultType'] = random.randint(0, 2)
                    if io_date['faultType'] != 0:
                        io_date['motorType'] = random.randint(1, 9)
                        io_date['motorFault'] = random.randint(0, 255)
                    else:
                        io_date['motorType'] = 0
                        io_date['motorFault'] = 0
                    print(io_date)
                    print(type(io_date))
                    try:
                        req = requests.post(url=perf_full_saveQB, json=io_date, headers=headers)
                        print(req.text)
                    except Exception as error:
                        print(error)
                    else:
                        with open(out_flie, 'a+', encoding='utf-8') as newFile:
                            newFile.write(json.dumps(io_date) + '\n')
                    time.sleep(10)


# full_saveQB()


def full_save(vin, ws=4):
    FOLDER_PATH = r'D:\data\fulldata\fulldata'
    OUT_FILE_PATH = r'D:\data\fulldata'
    IN_FILE_NAME = os.listdir(FOLDER_PATH)
    print(IN_FILE_NAME)
    print(vin)
    for in_file in IN_FILE_NAME:
        if vin in in_file:
            emb_file = FOLDER_PATH + '\\' + in_file
            out_flie = OUT_FILE_PATH + '\\' + in_file
            is_PARKING = None
            PARKING_count = 0
            stateOf_Charge = car_args.sc
            reb_soc = 0
            mlieages = car_args.mli
            #挡位使用次数
            gearPosition_count = 0
            gpc = 0
            renember_gearPosition = 0
            #搅拌和扫刷参数上传次数
            mix_sweep_count = 0
            #扫刷和搅拌的具体参数
            work_mix = None
            work_sweep = None
            # new_time_2 = parse('2023-12-02 14:00:00')
            print(emb_file, out_flie)

            with open(emb_file, 'r', encoding='utf-8') as f:
                #print(len(f.readlines()))
                #for i in f.readlines()[0:2]:
                json_load = json.load(f)
                for io_date in json_load[-1::-1]:
                    io_date = new_key(io_date)
                    new_time_1 = io_date["time"][0:10] + " " + io_date["time"][11:19]
                    # tc = relativedelta(minutes=random.randint(20, 300))
                    # over_t = relativedelta(minutes=random.randint(300, 500))
                    # new_time_2 += tc
                    new_time_3 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # print(new_time_3)
                    time_stp = int(format(get_time_stp(new_time_3), '.0f'))
                    # print(time_stp)
                    io_date.pop("time")
                    io_date["recordTime"] = time_stp
                    io_date['subSystemProbeTemperatureCount'] = '35|35'
                    charging_State = ['PARKING', 'DRIVING', 'OUTAGE', 'COMPLETED', 'OP_EXCEPTION', 'OP_INVALID']
                    operating_PARKING = ['CLOSE', 'OTHER', 'OP_EXCEPTION', 'OP_INVALID']
                    operating_OUTAGE = ['RUN', 'OTHER', 'OP_EXCEPTION', 'OP_INVALID']
                    operating_OTHER = ['OTHER', 'OP_EXCEPTION', 'OP_INVALID']
                    if is_PARKING == 'PARKING' or is_PARKING == 'OUTAGE':
                        if PARKING_count > 50:
                            PARKING_count = 1
                            io_date['stateOfCharge'] = reb_soc
                            is_PARKING = random.choices(charging_State, weights=[1, 1, 1, 1, 1, 1], k=1)[0]
                            io_date['chargingState'] = is_PARKING

                            if is_PARKING == 'PARKING':
                                io_date['operatingState'] = random.choices(operating_PARKING, weights=[10, 1, 1, 1], k=1)[0]
                            elif is_PARKING == 'OUTAGE':
                                io_date['operatingState'] = random.choices(operating_OUTAGE, weights=[10, 1, 1, 1], k=1)[0]
                            else:
                                io_date['operatingState'] = random.choices(operating_OTHER, weights=[1, 1, 1], k=1)[0]

                        elif is_PARKING == 'PARKING' and PARKING_count % 2 == 0:
                            stateOf_Charge += 1
                            if stateOf_Charge <= 100:
                                io_date['stateOfCharge'] = stateOf_Charge
                                io_date['chargingState'] = is_PARKING
                                io_date['operatingState'] = random.choices(operating_PARKING, weights=[10, 1, 1, 1], k=1)[0]
                                if PARKING_count == 50:
                                    reb_soc = stateOf_Charge
                            else:
                                io_date['stateOfCharge'] = 100
                                stateOf_Charge = 100
                                reb_soc = 100
                                io_date['chargingState'] = is_PARKING
                                io_date['operatingState'] = random.choices(operating_PARKING, weights=[10, 1, 1, 1], k=1)[0]
                            PARKING_count += 1

                        elif is_PARKING == 'OUTAGE' and PARKING_count % 2 == 0:
                            stateOf_Charge -= 1
                            if stateOf_Charge >= 0:
                                io_date['stateOfCharge'] = stateOf_Charge
                                io_date['chargingState'] = is_PARKING
                                io_date['operatingState'] = random.choices(operating_OUTAGE, weights=[10, 1, 1, 1], k=1)[0]
                                if PARKING_count == 50:
                                    reb_soc = stateOf_Charge
                            else:
                                io_date['stateOfCharge'] = 0
                                stateOf_Charge = 0
                                reb_soc = 0
                                io_date['chargingState'] = is_PARKING
                                io_date['operatingState'] = random.choices(operating_OUTAGE, weights=[10, 1, 1, 1], k=1)[0]
                            PARKING_count += 1

                        else:
                            if stateOf_Charge <= 100 and stateOf_Charge >= 0:
                                io_date['stateOfCharge'] = stateOf_Charge
                                reb_soc = stateOf_Charge
                            elif stateOf_Charge < 0:
                                io_date['stateOfCharge'] = 0
                                stateOf_Charge = 0
                                reb_soc = 0
                            elif stateOf_Charge > 100:
                                io_date['stateOfCharge'] = 100
                                stateOf_Charge = 100
                                reb_soc = 100

                            if is_PARKING == 'PARKING':
                                io_date['operatingState'] = random.choices(operating_PARKING, weights=[10, 1, 1, 1], k=1)[0]
                            elif is_PARKING == 'OUTAGE':
                                io_date['operatingState'] = random.choices(operating_OUTAGE, weights=[10, 1, 1, 1], k=1)[0]
                            else:
                                io_date['operatingState'] = random.choices(operating_OTHER, weights=[1, 1, 1], k=1)[0]

                            io_date['chargingState'] = is_PARKING

                            PARKING_count += 1
                    else:
                        is_PARKING = random.choices(charging_State, weights=[1, 1, 1, 1, 1, 1], k=1)[0]
                        io_date['chargingState'] = is_PARKING

                        if PARKING_count == 0:
                            io_date['stateOfCharge'] = stateOf_Charge
                        else:
                            io_date['stateOfCharge'] = reb_soc

                        if is_PARKING == 'PARKING':
                            io_date['operatingState'] = random.choices(operating_PARKING, weights=[10, 1, 1, 1], k=1)[0]
                        elif is_PARKING == 'OUTAGE':
                            io_date['operatingState'] = random.choices(operating_OUTAGE, weights=[10, 1, 1, 1], k=1)[0]
                        else:
                            io_date['operatingState'] = random.choices(operating_OTHER, weights=[1, 1, 1], k=1)[0]

                    io_date['alarmBitIdentify'] = randem_nember(0, 1, 19) + '0000000000000'
                    io_date['brakeTravel'] = random.randint(0, 100)
                    io_date['acceleratorTravel'] = random.randint(0, 100)
                    io_date['operationMode'] = 'ELECTRIC_ONLY'
                    io_date['controllerCurrent'] = format(random.uniform(100, 350), f'.{random.randint(1, 3)}f')
                    if gearPosition_count == 0:
                        gpc = random.randint(1, 100)
                        renember_gearPosition = randem_nember(0, 1, 4) + '0000'
                        io_date['gearPosition'] = int(renember_gearPosition, 2)
                        gearPosition_count += 1
                    elif gearPosition_count != 0 and gearPosition_count < gpc:
                        io_date['gearPosition'] = int(renember_gearPosition, 2)
                        gearPosition_count += 1
                    elif gearPosition_count >= gpc:
                        gearPosition_count = 0
                        io_date['gearPosition'] = int(renember_gearPosition, 2)
                    io_date, mlieages = mileage(io_date, mlieages)
                    list_io_date = []
                    list_io_date.append(io_date)
                    print(list_io_date)
                    print(type(list_io_date))
                    # print(io_date['gearPosition'])
                    try:
                        full_save = requests.post(url=perf_full_save, json=list_io_date, headers=headers)
                        print(full_save.text)
                        if io_date['chargingState'] == 'OUTAGE' and ws == 1:
                            mix_sweep_count, work_mix, work_sweep = mix_sweep(io_date=io_date,
                                                                              work_mix=work_mix,
                                                                              work_sweep=work_sweep,
                                                                              ws=ws,
                                                                              mix_sweep_count=mix_sweep_count,
                                                                              vin=vin,
                                                                              collec_time=new_time_3
                                                                              )
                            min_save = requests.post(url=perf_mixer_saveMixer, json=work_mix, headers=headers)
                            print(min_save.text)
                            sweep_save = requests.post(url=perf_sweep_saveSweep, json=work_sweep, headers=headers)
                            print(sweep_save.text)
                        elif io_date['chargingState'] == 'OUTAGE' and ws == 2:
                            mix_sweep_count, work_mix = mix_sweep(io_date=io_date,
                                                                              work_mix=work_mix,
                                                                              work_sweep=work_sweep,
                                                                              ws=ws,
                                                                              mix_sweep_count=mix_sweep_count,
                                                                              vin=vin,
                                                                              collec_time=new_time_3
                                                                              )
                            min_save = requests.post(url=perf_mixer_saveMixer, json=work_mix, headers=headers)
                            print(min_save.text)
                        elif io_date['chargingState'] == 'OUTAGE' and ws == 3:
                            mix_sweep_count, work_sweep = mix_sweep(io_date=io_date,
                                                                  work_mix=work_mix,
                                                                  work_sweep=work_sweep,
                                                                  ws=ws,
                                                                  mix_sweep_count=mix_sweep_count,
                                                                  vin=vin,
                                                                  collec_time=new_time_3
                                                                  )
                            sweep_save = requests.post(url=perf_sweep_saveSweep, json=work_sweep, headers=headers)
                            print(sweep_save.text)
                        else:
                            pass
                    except Exception as error:
                        print(error)
                    else:
                        with open(out_flie, 'a+', encoding='utf-8') as newFile:
                            newFile.write(json.dumps(io_date) + '\n')

                    time.sleep(10)




def main(num, ws=4):
    if num == 1:
        vin_list = ['L58ZC5VC9ND003096', 'LEWUMC180PF101060', 'LEWUMC187MF146721']
        # vin_list = ['LEWUMC187MF146721']
        for vin in vin_list:
            full_gb = Thread(target=full_save, args=(vin, ws))
            full_gb.start()
            full_qb = Thread(target=full_saveQB, args=(vin,))
            full_qb.start()
        full_gb.join()
        full_qb.join()

    elif num == 2:
        FOLDER_PATH = r'D:\data\fulldata\fulldata'
        IN_FILE_NAME = os.listdir(FOLDER_PATH)
        for vin in IN_FILE_NAME:
                lstr = vin.find('_')
                rstr = vin.rfind('.')
                vin = vin[lstr + 1: rstr]
                full_save(vin)
                # full_saveQB(vin)



if __name__ == '__main__':
    car_info = argparse.ArgumentParser()
    car_info.add_argument('-sc', type=int, default=-1, help='车电量')
    car_info.add_argument('-mli', type=int, default=-1, help='车里程')
    car_info.add_argument('-ws', type=int, default=4,
                          help='输入1: 加入搅拌和扫刷状态，输入2: 加入搅拌状态，输入3：加入扫刷状态, 输入4：不加任何状态')
    car_args = car_info.parse_args()
    if car_args.sc != -1 and car_args.mli != -1:
        while True:
            main(num=1, ws=car_args.ws)
    else:
        print('输入的参数不正确，请输入 -h 命令查看参数')

