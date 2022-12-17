import inspect
import  logging
class Baseclass:
    def test_getlogger(self):
        loggername = inspect.stack()[0][3]#to get the fx name
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('l2.log')
        if logger.hasHandlers():
            logger.handlers.clear()
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger


"""
Folks, you may see that there are duplicate log statements in your log file for a "single" run, if you execute your test case, especially with parameterized test data(i.e, params=([("Data1"), ("Data2")])

Example: (Data2 prints additionally):

    2020-01-27 13:10:41,862: INFO: test_VerifyHomePageForm: Entering name input Data2
    2020-01-27 13:10:41,863: INFO: test_VerifyHomePageForm: Entering name input Data2

This is due to every time you call the logging function, it's adding another handler to the instance, which causes duplicate logs. 
Please refer this for more detail: https://stackoverflow.com/questions/7173033/duplicate-log-output-when-using-python-logging-module
To avoid this, Just added the following logic before this line: logger.addHandler(handler)
if (logger.hasHandlers()):     
     logger.handlers.clear()
"""
