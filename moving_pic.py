from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import re, time, os, random
import urllib
import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

app = Flask(__name__)

# 轮廓检测
def get_pos_1(imageSrc):
    # 读取图像文件并返回一个image数组表示的图像对象
    image = cv2.imread(imageSrc)
    # GaussianBlur方法进行图像模糊化/降噪操作。
    # 它基于高斯函数（也称为正态分布）创建一个卷积核（或称为滤波器），该卷积核应用于图像上的每个像素点。
    blurred = cv2.GaussianBlur(image, (5, 5), 2, 2)
    # print(image)
    # Canny方法进行图像边缘检测
    # blurred: 输入的单通道灰度图像。
    # threshold1: 第一个阈值，用于边缘链接。一般设置为较小的值。
    # threshold2: 第二个阈值，用于边缘链接和强边缘的筛选。一般设置为较大的值
    canny = cv2.Canny(blurred, 50, 300)  # 轮廓
    # findContours方法用于检测图像中的轮廓, 并返回一个包含所有检测到轮廓的列表。
    # contours(可选): 输出的轮廓列表。每个轮廓都表示为一个点集。
    # hierarchy(可选): 输出的轮廓层次结构信息。它描述了轮廓之间的关系，例如父子关系等。
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历检测到的所有轮廓的列表
    # print(contours)
    n = 1
    for contour in contours:
        # contourArea方法用于计算轮廓的面积
        area = cv2.contourArea(contour)
        # print("area   ", end="")
        # print(area, end='')
        # arcLength方法用于计算轮廓的周长或弧长
        length = cv2.arcLength(contour, True)
        # print("    length   ", end="")
        # print(length)
        # 如果检测区域面积在5025-7225之间，周长在300-380之间，则是目标区域
        if 4000 < area < 6000:
            print(f"就是我 第{n}次      ", end="")
            print(area, length)
            # 计算轮廓的边界矩形，得到坐标和宽高
            # x, y: 边界矩形左上角点的坐标。
            # w, h: 边界矩形的宽度和高度。
            x, y, w, h = cv2.boundingRect(contour)
            print("计算出目标区域的坐标及宽高：", x, y, w, h)
            # 在目标区域上画一个红框看看效果
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imwrite(f"{n:04}.png", image)
            n += 1
            return x
    return 0


# 模版匹配
def get_pos_2(bg_image, sli_image):
    print('进来了')
    # 加载主图像和模板图像
    image = cv2.imread(bg_image)
    template = cv2.imread(sli_image)

    # 将图像转换为灰度图像
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 获取模板图像的宽度和高度
    print(template.shape)
    template_h, template_w = template.shape[:2]
    print(template_h, template_w)

    # 使用归一化交叉相关方法执行模板匹配
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # 找到结果矩阵中最佳匹配的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(f'min_val     {min_val}')
    print(f'max_val     {max_val}')
    print(f'min_loc     {min_loc}')
    print(f'max_loc     {max_loc}')

    # 在最佳匹配周围绘制矩形
    top_left = min_loc
    bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imwrite(f"0001.png", image)

    return min_loc[0]


# 数据中台
url = 'https://daas-perf.seazonmotor.com/'
url1 = 'https://accounts.douban.com/passport/login'
url2 = 'https://www.zhihu.com/'


# 创建Chrome WebDriver对象
@app.route('/get_pic/<any(1, 2):get_type>')
def get_pic(get_type=2):
    driver = webdriver.Chrome()
    try:
        driver.get(url=url)
        # print(dir(driver))
        # 选择账号登陆
        if get_type == 1:
            # 账号密码登陆
            loginType = driver.find_element(By.CSS_SELECTOR, 'label[class="el-radio-button is-active"]')
            loginType.click()
            # 记住登陆状态
            remblogin = driver.find_element(By.CLASS_NAME, 'el-checkbox__label')
            remblogin.click()

            driver.implicitly_wait(3)  # 使用浏览器隐式等待3秒

            # print(loginType.text)
            # time.sleep(5)

            # 设置账号和密码
            userInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号/邮箱/手机号"]')
            userInput.send_keys("zld87")
            # userInput.clear()
            pwdInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号密码"]')
            pwdInput.send_keys("123qweASD")
            # time.sleep(3)

            # 获取登录按钮并点击登录
            loginButton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[5]/div/button')
            loginButton.click()
            # print(f'loginButton:     {loginButton.location}')

        elif get_type == 2:
            # 手机验证码登陆
            loginType = driver.find_element(By.CSS_SELECTOR, 'label[class="el-radio-button"]')
            loginType.click()
            # 记住登陆状态
            remblogin = driver.find_element(By.CLASS_NAME, 'el-checkbox__label')
            remblogin.click()

            # 设置手机号码
            userInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入手机号"]')
            userInput.send_keys("13916843740")
            # 点击验证码并弹出图片验证
            pwdInput = driver.find_element(By.CSS_SELECTOR, 'button[class="el-button getCodeBtn"]')
            pwdInput.click()


        # 开始验证滑块图片一系列操作

        driver.implicitly_wait(5)  # 使用浏览器隐式等待3秒

        # 等待滑块验证图片加载后，再做后面的操作
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'bg-img')))

        # 等待模版图片加载后，再做后面的操作
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'slider-img')))

        # 获取滑块验证背景图片下载路径
        bg_image = driver.find_element(By.ID, 'bg-img')
        bg_src = bg_image.get_attribute('src')

        # 获取模版图像下载路径
        slider_img = driver.find_element(By.ID, 'slider-img')
        sli_src = slider_img.get_attribute('src')
        # print(src)

        # 下载图片至本地
        urllib.request.urlretrieve(bg_src, 'bgImage.png')
        urllib.request.urlretrieve(sli_src, 'sliImage.png')

        # 计算缺口图像的x轴位置
        # dis = get_pos_1(imageSrc='bgImage.png')

        print('准备进入')
        dis = get_pos_2(bg_image='bgImage.png', sli_image='sliImage.png')

        # 根据滑块图标中
        if dis != 0:
            # 获取小滑块元素，并移动它到上面的位置
            print('进来了, 小图片坐标', end='')
            # smallImage = driver.find_element(By.ID, 'slider-move-btn')
            smallImage = driver.find_element(By.XPATH, '//*[@id="slider-move-btn"]')
            # 移动图标起始 x轴坐标
            print(smallImage.location['x'])
            # 小滑块到目标区域的移动距离（缺口坐标的水平位置 距离 小滑块的水平坐标相减的差）
            # 新缺口坐标=原缺口坐标*新画布宽度/原画布宽度
            new_dis = int(smallImage.location['x'] + dis * 260 / 590)
            # 使用浏览器隐式等待5秒
            driver.implicitly_wait(5)

            # 按下小滑块按钮不动
            ActionChains(driver).click_and_hold(smallImage).perform()

            # 移动小滑块，模拟人的操作，一次次移动一点点
            i = 1
            ac_move = smallImage.location['x']
            print(f'newDis:  {new_dis}')
            while ac_move < new_dis:
                x = random.randint(3, 10)  # 每次移动3到10像素
                ac_move += x
                print("准备移动")
                ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
                print("第{}次移动后，位置为{}".format(i, smallImage.location['x']))
                i += 1

            # 移动完之后，松开鼠标
            ActionChains(driver).release()
            # 整体等待5秒看结果
            time.sleep(3)

            # os.remove('bgImage.png')

    finally:
        # 关闭浏览器
        driver.quit()
    # return 'ok'


# get_pic(2)
if __name__ == '__main__':
    app.run(port=1234, debug=True)
