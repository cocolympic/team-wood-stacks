from datetime import tzinfo, timedelta, datetime

class JST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=9)

    def dst(self, dt):
        return timedelta(0)  # 日本は夏時間なし

    def tzname(self, dt):
        return "Asia/Tokyo"

# タイムゾーン付きの日時を作成
japan_time = datetime(2025, 9, 8, 23, 57, tzinfo=JST())

print(japan_time)           # 2025-09-08 23:57:00+09:00
print(japan_time.tzinfo)    # Asia/Tokyo
