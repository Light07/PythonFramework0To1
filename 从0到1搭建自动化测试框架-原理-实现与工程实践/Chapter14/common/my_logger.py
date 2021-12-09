import logging
import sys

from concurrent_log_handler import ConcurrentRotatingFileHandler

# 设置日志的名称
LOGGER_NAME = 'main'
# 指定日志的等级必须在LOG_LEVEL变量里
LOG_LEVEL = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']


class MyLogger:
    # 创建一个日志对象
    def __init__(self, logger_name=LOGGER_NAME,
                 log_level: LOG_LEVEL = None,
                 file_name=None,
                 file_size=512 * 1024,
                 log_format="%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(processName)s -%(thread)d -%("
                            "threadName)s - %(message)s"):

        self.log_level = log_level
        # 创建一个格式器
        self.formatter = logging.Formatter(log_format)
        # 指定log文件
        self.file_name = file_name
        # 指定log文件大小
        self.file_size = file_size
        # 指定logger名称
        self.logger_name = LOGGER_NAME

        self.logger = logging.getLogger(logger_name)

        # 设置日志等级
        try:
            self.logger.setLevel(logging.DEBUG if not self.log_level else self.log_level)
        except Exception:
            self.logger.error('Log等级必须属于LOG_LEVEL变量')
            raise ValueError('Log等级必须属于LOG_LEVEL变量')

        # 为日志对象添加流的处理器handler
        self.logger.addHandler(self.get_console_handler())

        # 为日志对象添加文件处理器handler
        if file_name:
            self.logger.addHandler(self.get_file_handler())

        self.propagate = False

    def get_logger(self, module_name):
        return logging.getLogger(self.logger_name).getChild(module_name)

    def get_console_handler(self):
        # 创建一个流处理器handler
        ch = logging.StreamHandler(sys.stdout)
        # 创建一个日志格式器formatter并将其添加到处理器handler
        ch.setFormatter(self.formatter)
        self.logger.handlers.clear()
        return ch

    def get_file_handler(self):
        # 使用进程安全的方式创建
        # 指定文件写入方式为append，文件大小为512k
        fh = ConcurrentRotatingFileHandler(self.file_name, "a", self.file_size, encoding="utf-8")
        fh.setFormatter(self.formatter)
        return fh

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warning(self, msg, extra=None):
        self.logger.warning(msg, extra=extra)
