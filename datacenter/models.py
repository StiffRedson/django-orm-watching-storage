from django.db import models
from django.utils import timezone
import datetime
import pytz


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved",
        )

    @property
    def get_duration(self):
        if self.leaved_at is None:
            self.leaved_at = timezone.now()
        # moscow_tz = pytz.timezone("Europe/Moscow")
        # moscow_tz.localize(self.leaved_at)
        delta = self.leaved_at - self.entered_at
        return delta.seconds

    @staticmethod
    def format_duration(duration):
        return datetime.timedelta(seconds=duration)

    @staticmethod
    def is_visit_long(visit, minutes=60):
        if int(visit) / 60 > minutes:
            return True
        else:
            return False
