from django.db import models
from django.utils import timezone
import datetime
import pytz
import time


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

    def get_duration(self):
        if self.leaved_at is None:
            self.leaved_at = timezone.now()
        delta = self.leaved_at - self.entered_at
        return delta.seconds

    def format_duration(self):
        duration = Visit.get_duration(self)
        return datetime.timedelta(seconds=duration)

    def is_visit_long(self, minutes=60):
        is_strange = Visit.get_duration(self)
        time_presence = int(is_strange) / 60
        return time_presence > minutes
