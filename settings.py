import logging

class Null:
    pass


EXCLUDED_KEYS = set(Null.__dict__.keys())


class ShellSettings:
    LOGO = """
         _.._..,_,_
        (          )
         ]~,"-.-~~[
       .=])' (;  ([     Beer2Beer is a 4b Inf project
       | ]:: '    [     ITET Leonardo da Vinci, Milazzo (ME)
       '=]): .)  ([     A working demo of a p2p system!!!
         |:: '    |
          ~~----~~
    
    CONTRIBUTOR(s):
    * Antonio Caristia (antonio.caristia at davincimilazzo.edu.it)
    * Antonio Trifirò (antonio.trifiro at davincimilazzo.edu.it)
    * Francesco Salerno ( francesco.salerno at davincimilazzo.edu.it)
    """
    USERNAME = None
    PASSWORD = None
    DIRECTORY = None
    DIRECTORY_SETTINGS = ".beer2beer"
    SERVER_HOST = "localhost"
    SERVER_PORT = 8888

    @classmethod
    def load(cls, records):
        for key,value in records.items():
            setattr(cls, key, value)


    @classmethod
    def dict_from_class(cls):
        records = {}
        for key, value in cls.__dict__.items():
            if key not in EXCLUDED_KEYS and not hasattr(value, '__func__'):
                records[key] = value
        return records


class LoggerSettings:
    LOGGER_LEVEL = logging.DEBUG
    LOGGER_HANDLER = logging.StreamHandler()
    LOGGER_STRING = "[%(asctime)s] - %(name)-6s - %(levelname)-6s - %(message)s"

    @classmethod
    def get_logger(cls, logger_name=__name__):
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(cls.LOGGER_LEVEL)

        # create console handler and set level to debug
        ch = cls.LOGGER_HANDLER
        ch.setLevel(cls.LOGGER_LEVEL)

        # create formatter
        formatter = logging.Formatter(cls.LOGGER_STRING)

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)
        return logger
