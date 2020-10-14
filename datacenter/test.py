import datetime
from django.utils import timezone

listok = {'entered_at': f"{datetime.datetime(2019, 6, 22, 5, 18)}", 'duration': f"{datetime.timedelta(0, 1080)}", 'is_strange': False}

# for li in l:
#     print(li)
print(listok)
t = datetime.datetime.utcnow()
print(str(t))
