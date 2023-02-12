from django.conf import settings
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from datetime import datetime


def schedule_message_whatapp(to_number, payload, send_at):
    account_sid = "AC9679dbfdbb48fdd3309dd3fde20dc279"  # please change it to your own
    auth_token = "a798a22ad93c6495522013410a878c33"  # please change it to your own
    client = Client(account_sid, auth_token)

    year = int(send_at.strftime("%Y"))
    month = int(send_at.strftime("%m"))
    day = int(send_at.strftime("%d"))
    hour = int(send_at.strftime("%H"))
    min = int(send_at.strftime("%M"))
    sec = int(send_at.strftime("%S"))
    try:
        message = client.messages.create(
            to=f'whatsapp:{to_number}',
            body=payload,
            schedule_type="fixed",
            send_at=datetime(year, month, day, hour, min, sec),
            messaging_service_sid=settings.MESSAGING_SERVCIE_SID
        )
        print(f"Message sent successfully: {message} {message.sid}")
    except TwilioRestException as e:
        print(e)
        pass


def schedule_call(to_number, first_name):
    account_sid = "AC9679dbfdbb48fdd3309dd3fde20dc279"  # please change it to your own
    auth_token = "a798a22ad93c6495522013410a878c33"  # please change it to your own
    client = Client(account_sid, auth_token)

    voice_note = "Hello {} this is reminder call, Thank You".format(first_name)

    try:
        call = client.calls.create(
                            twiml=f'<Response><Say>{voice_note}</Say></Response>',
                            to=f'{to_number}',
                            messaging_service_sid=settings.MESSAGING_SERVCIE_SID
                        )

        print(call.sid)
    except TwilioRestException as e:
        print(e)
        pass
