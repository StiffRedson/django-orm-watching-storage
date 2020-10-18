from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []
    for history in passcard:
        entered_at = history.entered_at
        duration = history.format_duration()
        is_strange = history.is_visit_long()

        this_passcard_visit =   {
                                    "entered_at": entered_at,
                                    "duration": duration,
                                    "is_strange": is_strange
                                }

        this_passcard_visits.append(this_passcard_visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
