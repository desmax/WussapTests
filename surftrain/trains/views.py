from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404
from trains.models import Status, Train
from django.conf import settings
from django.template.context import RequestContext
from datetime import datetime, timedelta

def index(request):
    error_messages = None
    if request.method == 'POST':
        try:
            train = Train(description = request.POST['description'],
                username = request.POST['username'],
                departure = request.POST['departure'],
                status = Status.objects.get(name = 'scheduled'))
            train.full_clean()
            if train.departure < datetime.now():
                exception = ValidationError('Departure should be in future')
                raise exception
            train.save()
            return redirect(reverse('trains.views.view', kwargs = {
                'train_id': train.pk
            }))
        except ValidationError, error:
            error_messages = error.messages

    tomorrow = datetime.now() + timedelta(days = 1)
    tomorrow = tomorrow.date()

    ongoing = Train.objects.filter(status = Status.objects.get(name = 'ongoing'),
        departure__lt = tomorrow,
        departure__gt = datetime.now()
    )[:3]
    scheduled = Train.objects.filter(status = Status.objects.get(name = 'scheduled'),
        departure__gte = datetime.now())[:3]

    arrived = Train.objects.filter(status = Status.objects.get(name = 'arrived'),
        departure__gt = datetime.now(),
        arrival__lte = datetime.now()
    )[:3]

    template = loader.get_template('trains/views/index.html')

    context_dictionary = {
        'arrived': arrived,
        'ongoing': ongoing,
        'scheduled': scheduled,
    }
    if error_messages:
        context_dictionary = dict(context_dictionary.items() + {'error_messages': error_messages}.items())

    context = RequestContext(request, context_dictionary)
    return render_layout(template.render(context))

def status(request, status_name):
    try:
        status = Status.objects.get(name = status_name)
        trains = Train.objects.filter(status = status.pk)
    except Status.DoesNotExist:
        raise Http404
    except Train.DoesNotExist:
        raise Http404

    template = loader.get_template('trains/views/status.html')
    context = Context({
        'trains': trains,
        'status_name': status_name
    })

    return render_layout(template.render(context))

def view(request, train_id):
    train = get_object_or_404(Train, pk = train_id)

    template = loader.get_template('trains/views/view.html')
    context = Context({
        'train': train,
    })

    return render_layout(template.render(context))

def render_layout(content):
    return render_to_response(settings.LAYOUT, {
        'content': content,
        'static_url': settings.STATIC_URL
    })