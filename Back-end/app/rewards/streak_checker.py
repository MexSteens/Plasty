from app.database.model import Complaint
from datetime import date, timedelta


def StreakChecker(user):
    streaks_gained = 0

    if user.streaks == 0:
        today = date.today()

        if len(Complaint.read_date(user_id=user.id, date=today)) >= 1:
            user.streaks += 1
            streaks_gained = 1
    elif user.streaks == 1:
        today = date.today()

        complaint_today = Complaint.read_date(user_id=user.id, date=today)

        if len(complaint_today) == 1:
            user.streaks += 1
            streaks_gained = 1
    else:
        today = date.today()
        yesterday = today - timedelta(days=1)

        complaint_today = Complaint.read_date(user_id=user.id, date=today)
        complaint_yesterday = Complaint.read_date(user_id=user.id, date=yesterday)

        if not complaint_yesterday:
            user.streaks = 0
        elif len(complaint_today) == 1:
            user.streaks += 1
            streaks_gained = 1

    return streaks_gained
