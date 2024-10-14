from datetime import datetime, timedelta, time

import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from habits.models import Habits
from users.models import User

URL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/"
GET_UPDATES = "getUpdates"
SEND_MESSAGE = "sendMessage"


@shared_task
def send_habit_reminder():
    now = datetime.utcnow()
    time_ = time(now.time().hour, now.time().minute, 0)

    habits = Habits.objects.filter(day=now.date()).filter(time=time_)

    for habit in habits:
        user = User.objects.get(pk=habit.user.pk)

        if user.telegram:
            get_updates_payload = {
                'chat_id': user.telegram
            }
            headers = {
                'accept': 'application/json',
                'content-type': 'application/json'
            }

            chat = requests.post(URL + GET_UPDATES, json=get_updates_payload, headers=headers).json()

            if chat.get('ok') is True:
                chat_id = chat['result'][0]['message']['chat']['id']

                payload = {
                    'chat_id': chat_id,
                    'text': f'Напоминаню вам о привычке! {habit}'
                }

                requests.post(URL + SEND_MESSAGE, json=payload, headers=headers)

        else:
            send_mail(
                subject='Напоминание!',
                message=habit,
                recipient_list=[user.email],
                from_email=settings.EMAIL_HOST_USER,
                fail_silently=False
            )

        habit.day += timedelta(days=habit.periodicity)
        habit.save()
