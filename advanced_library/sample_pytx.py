import pytz
from datetime import datetime

# datetimeよりも便利な機能が多い

# JST（ローカルPCのデフォルト）
now = datetime.now()
print("{0:%Y-%m-%d %H:%M:%S}".format(now))

# 東京のタイムゾーンを指定
timezone = pytz.timezone('Asia/Tokyo')
# tokyo = timezone.localize(now)
tokyo = now.astimezone(timezone)
print(tokyo)

# UTCを指定
utc = now.astimezone(pytz.utc)
print(utc)
print("{0:%Y-%m-%dT%H:%M:%SZ}".format(utc))
