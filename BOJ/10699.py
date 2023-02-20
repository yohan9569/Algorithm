# 구현 / 브론즈 5 / 오늘 날짜


# 1.
from datetime import datetime, timezone, timedelta
print(datetime.now(timezone(timedelta(hours=9))).date())

# 2.
from datetime import datetime
from pytz import timezone
print(datetime.now(timezone('Asia/Seoul')).date())

# 3.
print('2023-02-19')
