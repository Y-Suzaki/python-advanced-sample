from datetime import datetime, timezone, timedelta

#
# ロカールのタイムゾーンで取得、今回はJSTになる
#
datetime_default_obj = datetime.now()
print(datetime_default_obj)

# '%Y/%m/%d %H:%M:%S.%f'形式で出力
print(datetime_default_obj.strftime('[Native] %Y/%m/%d %H:%M:%S.%f'))

#
# UTCのタイムゾーンで取得
#
datetime_utc_obj = datetime.now(timezone.utc)
print(datetime_utc_obj)
print(datetime_utc_obj.strftime('[UTC] %Y/%m/%d %H:%M:%S.%f'))

# 標準ライブラリのみで、JSTのタイムゾーンに変更
# 2番目の引数'JST-TIMEZONE'は文字列表現に使われるようで、任意の文字列でよさそう
timezone_jst = timezone(timedelta(hours=+9), 'JST-TIMEZONE')
datetime_jst_obj = datetime_utc_obj.astimezone(timezone_jst)
print(datetime_jst_obj.strftime('[JST] %Y/%m/%d %H:%M:%S.%f'))
