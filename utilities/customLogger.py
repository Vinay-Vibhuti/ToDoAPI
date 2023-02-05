import logging

class CustomerLogger:
    @staticmethod
    def LogGen():
        logging.basicConfig(filename="C:\\Users\\arist\\PycharmProjects\\ToDoApi\\logs\\Automation.log", format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
