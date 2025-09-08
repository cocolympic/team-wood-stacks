from datetime import datetime, timezone, timedelta

dt = datetime(2025, 9, 7, 14, 30, tzinfo=timezone(timedelta(hours=2)))

# Get the time with timezone
time_with_tz = dt.timetz()

print("Original datetime:", dt)
print("Time with tzinfo:", time_with_tz)
print("Timezone info:", time_with_tz.tzinfo)
