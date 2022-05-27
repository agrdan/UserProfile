

import uuid

stringToken = str(uuid.uuid4())
print(stringToken)
print(len(stringToken))

from datetime import datetime as dt
from time import sleep as delay

now = dt.now().timestamp()
nowInt = int(now)
nowStr = str(nowInt)
print(nowStr)
print(len(nowStr))

delay(5)

from utils.Utils import Utils

diff = Utils.timestapsDiff(nowStr)
print(f"Diff is {diff.seconds}")