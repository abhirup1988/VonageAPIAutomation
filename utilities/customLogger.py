import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="..\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%b/%Y %H:%M:%S')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger