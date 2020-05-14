from merry import Merry
import requests
from requests import ConnectTimeout


merry = Merry()
merry.logger.disabled = True

catch = merry._try

class Baseclass(object):
    @staticmethod
    @merry._except(ZeroDivisionError)
    def process_zero_division_error(e):
        print('Zero division error', type(e))

    @staticmethod
    @merry._except(FileNotFoundError)
    def process_file_not_found(e):
        print('File not found', type(e))

    @staticmethod
    @merry._except(ConnectTimeout)
    def process_connect_timeout(e):
        print('connect timeout', type(e))
    
class Calculator(Baseclass):
    @catch
    def process(self, num1, num2, file):
        result = num1 / num2
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))

class Fetcher(Baseclass):

    @catch
    def process(self, url):
        response = requests.get(url=url)
        print("status code : ", response.status_code)
        if response.status_code == 200:
            print(response.text)

if __name__ == "__main__":
    c = Calculator()
    c.process(1,0,'result.txt')

    # f = Fetcher()
    # f.process('http://notfoundz.com')


    # 全球变量

    # @merry._try
    # def app_logic():
    #     db = open_database()
    #     merry.g.database = db
    
    # @merry._except(Exception):
    # def catch_all():
    #     db = getattr(merry.g, 'database') #获取merry全球变量
    #     if db is not None :
    #         close_database()
    #     sys.exit(1)