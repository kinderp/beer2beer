import logging


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