# 创建插件管理并添加规范
import pluggy
from btest.Day12.interface import MySpec
from btest.Day12.plugins_1 import Plugin_1
from btest.Day12.plugins_2 import Plugin_2
import btest.Day12.hook_wrapper as h_wrapper
from btest.Day12.interface import HookSpec

# 创建插件管理并添加规范
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)
pm.add_hookspecs(HookSpec)

# 注册插件
pm.register(Plugin_1(), name="p1")
pm.register(Plugin_2(), name="p2")  # LIFO

# 注册包装器
pm.register(h_wrapper)


# 1、让我们在一个模块中演示核心功能，并展示如何开始尝试插件功能。
def example_1():
    # 调用我们的“myhook”钩子
    results = pm.hook.myhook(arg1=1, arg2=2)
    print(results)  # 输出:[-1, 3] ,把每次实现的钩子结果存储在列表里，。

    """ 输出结果如下：
   正在执行 Plugin_2.myhook()...
   正在执行 Plugin_1.myhook()...
    [-1, 3]   # results 的输出结果
    """


# 2、自定义钩子的顺序
def example_2():
    # 调用我们的“myhook_2”钩子
    results = pm.hook.myhook_2(arg1=1, arg2=2)
    print(results)  # 输出:[3, -1] ,把每次实现的钩子结果

    """ 输出结果如下：
    inside Plugin_1.myhook_2()
    inside Plugin_2.myhook_2()
    [3, -1]
    """


# 3、实现对名字为my_hook钩子的装饰器，对钩子扩展
def example_3():
    # 调用我们的“myhook”钩子
    pm.hook.myhook(arg1=1, arg2=2)
    """
    程序开始执行，输入的参数为 1 2
    正在执行 Plugin_2.myhook()...
    正在执行 Plugin_1.myhook()... 
    程序执行完毕，结果为 [-1, 3]
    """


# 可以控制调用同名hookimpl函数的深度。
def example_4():
    # 调用我们的“he_myhook”钩子
    print('--------我是he_myhook1---------')
    pm.hook.he_myhook1(arg1=1)  # 当某个hookimpl 遇到了return就会停止

    print('\n--------我是he_myhook2---------')
    pm.hook.he_myhook2(arg1=1)


#  5、插件阻塞与检查是否注册
def example_5():
    pm.set_blocked('p1')  # 阻止p1插件注册
    print(pm.is_blocked('p1'))  # 如果给定的插件名称被阻止，则返回``True``
    pm.unregister('p1')  # 注销p1插件
    # 如果插件已注册，则返回``True`` ，未注册（注销了）返回False
    print(pm.is_registered('p1'))


#  插件信息
def example_6():
    print(pm.list_name_plugin())  # 返回名称-插件对列表
    print(pm.get_plugins())  # 检索所有插件
    print(pm.get_plugin('p1').info)  # 可以访问创建内部资源


# 后注册的插件先执行, LIFO 算法，后进先出。

if __name__ == '__main__':
    # example_1()
    # example_2()
    # example_3()
    # example_4()
    # example_5()
    example_6()
