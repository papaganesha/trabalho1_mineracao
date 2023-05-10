import schedule 
import time

from etl_clients import etl_clients
from etl_stores import etl_stores
from etl_books import etl_books
from etl_sells import etl_sells

schedule.every(1).hours.do(etl_clients)
schedule.every(1).hours.do(etl_stores)
schedule.every(1).hours.do(etl_books)
schedule.every(10).seconds.do(etl_sells)


# Run scheduler
count = 0
while True:
    schedule.run_pending()
    time.sleep(1)
