import logging
logger = logging.getLogger(__name__)
fn = logging.FileHandler('test.log')
logger.addHandler(fn)
logging.basicConfig(filename='test.log',level=logging.INFO,format='%(name)s:%(levelname)s:%(asctime)s:%(message)s')
def prime(n):
    return all(n%i for i in range(2, int(n*0.5)+1)) and n>1
logging.info(prime(7))
logger.info(prime(7))