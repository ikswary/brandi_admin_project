import json
import datetime


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode("utf-8")

        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(obj, datetime.timedelta):
            hours, remainder = divmod(obj.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            return '{:02}:{:02}'.format(int(hours), int(minutes))

        return json.JSONEncoder.default(self, obj)
