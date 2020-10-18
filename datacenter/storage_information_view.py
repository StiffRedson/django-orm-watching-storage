from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        who_entered = visit.passcard
        indoors = visit.entered_at
        outsid = visit.leaved_at
        time_in_storage = visit.format_duration()
        time_long = visit.is_visit_long()

        non_closed_visit = {
                                "who_entered": who_entered,
                                "entered_at": indoors,
                                "duration": time_in_storage,
                                "is_strange": time_long
                            }

        non_closed_visits.append(non_closed_visit)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
