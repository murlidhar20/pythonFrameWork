import logging
from utilities.readProperties import ReadConfig


class GenerateLogs:
    @staticmethod
    def log_gen(__name__):
        logger = logging.getLogger(__name__)
        #file_handler = logging.FileHandler(filename=ReadConfig.get_test_data('LOG_FILE'), mode='a')




        file_handler = logging.FileHandler("C:\\Users\\HP\\PycharmProjects\\pythonFrameWork\\Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)-12s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt="%d-%m-%Y %H:%M:%S")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger



    @staticmethod
    def loggen():
        logging.basicConfig(filename="..\Logs\automation12345.log", format='%(asctime)s:%(levelname)s:(messsage)s',
                            datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.info)
        return logger

