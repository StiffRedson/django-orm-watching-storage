from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []
    for history in passcard:
        entered_at = history.entered_at
        visit = history.get_duration
        duration = Visit.format_duration(visit)
        is_strange = Visit.is_visit_long(visit)

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
