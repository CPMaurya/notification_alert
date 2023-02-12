from django.shortcuts import render
from django.views import View
from main.forms import SubmitForm
from main.models import MainModel
from main.twilio import schedule_message_whatapp
from datetime import datetime, timedelta
from django.db import transaction


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitForm()
        context = {
            "form": the_form,
        }
        return render(request, "home.html", context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        form = SubmitForm(request.POST)
        context = {
            "form": form
        }
        template = "home.html"
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get('last_name')
            mobile_no = form.cleaned_data.get('mobile_no')
            notification_time = form.cleaned_data.get('notification_time')

            created = MainModel.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                mobile=mobile_no, 
                notification_time=notification_time
            )
            
            context = {
                "created": created,
            }
            schedule_time = (notification_time - timedelta(minutes=15))
            payload = f'''Dear {first_name},
                    You have reaceive a missed call at - {schedule_time}
                    Thank You'''
            if created:
                schedule_message_whatapp(to_number=mobile_no,
                                         payload=payload, 
                                         send_at=schedule_time.strftime("%Y-%m-%d %H:%M:%S"))
                template = "success.html"

        return render(request, template, context)


class AllNotifications(View):
    """ Show all Notification List """

    def get(self, request, *args, **kwargs):
        queryset = MainModel.objects.all()

        context = {
            "queryset": queryset,
        }
        return render(request, "all_notification.html", context)