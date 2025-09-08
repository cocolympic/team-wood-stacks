import datetime

# 2025年7月1日の日時オブジェクトを作成
dt_summer = datetime.datetime(2025, 7, 1, 12, 0, 0)

# 夏時間（DST）のオフセットを確認
print(f"夏時間のオフセット: {dt_summer.dst()}")
