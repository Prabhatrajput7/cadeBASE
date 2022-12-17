import logging


def test_loggingDemo():
    #__name__ will get the tc name
    logger = logging.getLogger(__name__)

    #now you need to provide a file name
    filehandler = logging.FileHandler('logfiles.log')
    #s in below is act like a string so that concatination can be happen
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    #in which format i neeed to print addhandler || file handler object
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("its a print statement and print to file")
    logger.info("information statement")
    logger.warning("aaye stop it bitch")
    logger.error("ERROR")
    logger.critical("haha gone bitch")
