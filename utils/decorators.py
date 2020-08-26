import logging
from functools import wraps


logger = logging.getLogger()


def start_finish_method_logger(method):
    """Логгирования начала и окончания выполнения теста"""
    @wraps(method)
    def message(*args, **kw):
        logger.info(f"Начало теста: {method.__name__}")
        result = method(*args, **kw)
        logger.info(f"Конец теста: {method.__name__}\n")
        return result
    return message


def decorate_class_methods(decorator):
    """Применяет декоратор ко всем методам в классе"""
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
