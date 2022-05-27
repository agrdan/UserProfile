from datetime import date
import datetime
from datetime import datetime as dt


class Utils:

    @staticmethod
    def parseStringDtToDate(string_date):
        try:
            date_formate = datetime.datetime.strptime(string_date, '%Y-%m-%d')
            parsedDate = date_formate.strftime("%Y-%m-%d")
            return parsedDate
        except Exception as e:
            print(e)

    @staticmethod
    def parseTimestamp(timestamp):
        date = dt.fromtimestamp(int(timestamp))
        parsedDate = date.strftime("%m/%d/%Y, %H:%M:%S")
        return parsedDate


    @staticmethod
    def getCurrentTimestamp():
        return str(int(dt.now().timestamp()))

    @staticmethod
    def timestapsDiff(timestampOld):
        oldtime = dt.fromtimestamp(int(timestampOld))
        currentTime = dt.fromtimestamp(int(dt.now().timestamp()))
        diff = currentTime - oldtime
        return diff