import datetime
import time
from fabric.api import local
standard_time = datetime.datetime(2022, 3, 11, 19, 26, 55, 524128)
standard_block_height = 11760339 - 10000
while True:

    diff = (datetime.datetime.now()-standard_time).seconds
    current_height = standard_block_height + diff // 6
    print(current_height)

    # call node with argument approximate_current_block_height
    local(
        fr"node C:\Users\Owner\Downloads\doc.mjs {current_height} | xargs python C:\Users\Owner\Downloads\doc.py")

    time.sleep(6)  # can be any
