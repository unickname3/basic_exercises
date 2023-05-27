"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
from pprint import pprint

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append(
            {
                "id": uuid.uuid4(),
                "sent_at": sent_at,
                "sent_by": random.choice(users_ids),
                "reply_for": random.choice(
                    [
                        None,
                        (
                            random.choice([m["id"] for m in messages])
                            if messages
                            else None
                        ),
                    ],
                ),
                "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
                "text": lorem.sentence(),
            }
        )
    return messages


def user_with_maximum_messages(messages):
    """Выводит айди пользователя, который написал больше всех сообщений."""
    stat = Counter([message["sent_by"] for message in messages])
    return stat.most_common(1)[0][0]


def user_with_maximum_answers(messages):
    """Выводит айди пользователя, на сообщения которого больше всего отвечали."""
    number_answers_for_message = dict()
    messages_by_user = dict()
    for message in messages:
        reply_for = message["reply_for"]
        number_answers_for_message.setdefault(reply_for, 0)
        number_answers_for_message[reply_for] += 1

        user = message["sent_by"]
        messages_by_user.setdefault(user, [])
        messages_by_user[user].append(message["id"])

    replys_for_user = dict()
    for user, messages_list in messages_by_user.items():
        replys_for_user.setdefault(user, 0)
        for message_id in messages_list:
            replys_for_user[user] += number_answers_for_message.get(message_id, 0)
    return max(replys_for_user, key=replys_for_user.get)


def user_with_maximum_seen(messages):
    """Выводит айди пользователей, сообщения которых видело больше всего уникальных пользователей."""
    users_message_seen = dict()
    for message in messages:
        user = message["sent_by"]
        users_message_seen.setdefault(user, set())
        users_message_seen[user] = users_message_seen[user].union(
            set(message["seen_by"])
        )

    users_message_seen_stat = {
        user: len(users_message_seen[user]) for user in users_message_seen.keys()
    }

    maximum_views = max(users_message_seen_stat.values())

    return ", ".join(
        [
            str(user)
            for user in users_message_seen_stat.keys()
            if users_message_seen_stat[user] == maximum_views
        ]
    )


def popular_time_to_send(messages):
    """Определяет, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов)."""
    pass


def longest_conversation(messages):
    """Выводит идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов)."""
    pass


if __name__ == "__main__":
    history = generate_chat_history()
    pprint(history)
    print(
        f"Больше всех сообщений написал пользователь с id: {user_with_maximum_messages(history)}"
    )
    print(
        f"Больше всего отвечали на сообщения пользователя с id: {user_with_maximum_answers(history)}"
    )
    print(
        f"Больше всего видели сообщения пользователя с id: {user_with_maximum_seen(history)}"
    )
