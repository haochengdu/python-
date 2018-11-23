### 1-获取主机ip
```
def get_ip():
    """获取主机ip"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        # print(s.getsockname())
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 对本机username的获取
>>> import socket
>>> socket.gethostname()
'LattePanda'
>>> host_name = socket.gethostname()
>>> host_name
'LattePanda'

# 对本机ip 的获取（不完全能获取ok）
>>> socket.gethostbyname(host_name)
'192.168.2.66'

# 对本机编码的获取
>>> import locale
>>> locale.getdefaultlocale()
('en_US', 'cp1252')

In [1]: import locale
In [2]: locale.getdefaultlocale()
Out[2]: ('zh_CN', 'cp936')
```
### 2-获取电脑的硬件信息 psutil模块
```
def get_cpu_info():
    """获取cup信息"""
    cpu_percent = str(psutil.cpu_percent(1)) + '%'
    return cpu_percent
    
def get_memory_info():
    """获取内存信息"""
    # 内存占用率
    memory_percent = str(psutil.virtual_memory().percent) + '%'
    return memory_percent
```
### 3-获取电脑操作系统信息 platform模块
```
def get_os_info():
    """获取os"""
    os_info = platform.platform()
    return os_info
```
### 4-获取电脑GPU信息 py3nvml模块
```
from py3nvml import nvidia_smi

class GPUHandler(object):
    """获取GPU信息，单例"""
    __instance = None
    __first_init = False

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if not GPUHandler.__first_init:
            self.my_nvidia_smi = nvidia_smi
            self.my_nvidia_smi.nvmlInit()  # 显卡初始化
            GPUHandler.__first_init = True

    def get_gpu_info(self):
        gpu_count = self.my_nvidia_smi.nvmlDeviceGetCount()  # 获取显卡总数
        # [{'gpu_num':0, 'gpu_name': 'xxx', 'mem_total':'4096MB', 'mem_used':'322MB','mem_percent': '20%'},{}....]
        gpu_info_list = []
        for i in range(gpu_count):
            handle = self.my_nvidia_smi.nvmlDeviceGetHandleByIndex(i)  # 创建操作某个GPU的对象
            memory_info = self.my_nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
            gpu_num = i
            gpu_name = self.my_nvidia_smi.nvmlDeviceGetName(handle)
            mem_total = int(memory_info.total / 1024 / 1024)
            mem_used = int(memory_info.used / 1024 / 1024)
            mem_percent = memory_info.used / memory_info.total * 100
            gpu_dict = dict(gpu_num=gpu_num, gpu_name=gpu_name, mem_total=str(mem_total) + 'MB',
                            mem_used=str(mem_used) + 'MB', mem_percent='%.2f' % mem_percent)
            gpu_info_list.append(gpu_dict)
        return gpu_info_list
```
### 5-对配置文件的处理 configparser模块
```
import configparser


class ConfigFileHandler(object):
    """对配置文件的操作-单例"""
    __instance = None
    __first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if not ConfigFileHandler.__first_init:
            # self.config_file_path = '../config/config.cfg'  # 测试
            self.config_file_path = './src/config/config.cfg'
            self.cfg = configparser.ConfigParser()
            self.cfg.read(self.config_file_path, encoding='utf-8')
            ConfigFileHandler.__first_init = True

    def get_config_value(self, section, option):
        """读取域下某个键的值"""
        return self.cfg.get(section=section, option=option)

    def set_config_value(self, section, option, val):
        """向配置文件中已有的section, option写入value"""
        self.cfg.set(section, option, val)
        with open(self.config_file_path, 'w') as fp:
            self.cfg.write(fp)  # 必须加入这一步才能写入配置文件

    def remove_config_option(self, section, option):
        self.cfg.remove_option(section, option)
        with open(self.config_file_path, 'w') as fp:
            self.cfg.write(fp)  # 必须加入这一步才能写入配置文件

    def has_option(self, section, option):
        return self.cfg.has_option(section, option)
```
### 6-对Redis的操作
```
import redis

from src.utils.config_handler import ConfigFileHandler


class RedisHelper(object):
    config_file_handler = ConfigFileHandler()

    def __init__(self):
        # 从配置文件中获取Redis的配置信息
        redis_host = RedisHelper.config_file_handler.get_config_value('REDIS', 'host')
        redis_port = int(RedisHelper.config_file_handler.get_config_value('REDIS', 'port'))
        redis_db = int(RedisHelper.config_file_handler.get_config_value('REDIS', 'db'))
        self.__redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    # 对字符串的操作
    # def is_exists(self, key_name):
    #     return self.__redis.exists(key_name)
    #
    # def get(self, key_name):
    #     if self.__redis.exists(key_name):
    #         return self.__redis.get(key_name)
    #     else:
    #         return False
    #
    # def set(self, key_name, value):
    #     self.__redis.set(key_name, value)
    #
    # def keys(self, prefix_flag):
    #     return self.__redis.keys(pattern=prefix_flag)
    #
    # def delete_key(self, key_name):
    #     self.__redis.delete(key_name)
    
    # 对hashset的操作
    def h_set(self, h_name, key_name, val):
        self.__redis.hset(h_name, key_name, val)

    def h_exists(self, h_name, key_name):
        return self.__redis.hexists(h_name, key_name)

    def h_get(self, h_name, key_name):
        return self.__redis.hget(h_name, key_name)

    def h_del(self, h_name, *keys):
        self.__redis.hdel(h_name, *keys)

    def h_keys(self, h_name):
        return self.__redis.hkeys(h_name)

    def h_len(self, h_name):
        return self.__redis.hlen(h_name)
```
### 7-日志模块
```
# 使用配置文件加载logging
logging.config.fileConfig('./src/config/logging.ini')
logger = logging.getLogger('root')


[loggers]
keys = root, src

[handlers]
keys = consoleHandler,fileHandler

[formatters]
keys = fmt

[logger_root]
level = DEBUG
handlers = consoleHandler, fileHandler

[logger_src]
level = INFO
qualname = src
propagate = 0
handlers = consoleHandler, fileHandler

[handler_consoleHandler]
class = StreamHandler
level = DEBUG
formatter = fmt
args = (sys.stdout,)

[handler_fileHandler]
class = logging.handlers.RotatingFileHandler
;class = handlers.ConcurrentRotatingFileHandler
level = DEBUG
formatter = fmt
;args = ("out.log", "a", 512*1024, 5)
args = ('./src/logs/agent.log','a',512*1024*1024,2,'utf-8')

[formatter_fmt]
;format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
format = %(asctime)s %(name)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s
datefmt=
```








