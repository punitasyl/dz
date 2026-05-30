
'''
Проблема: Изначально класс Notifier нарушает принцип, поскольку для добавления нового уведомления требуется изменение кода (например, добавление elif для нового канала).

Решение:

Создать абстрактный класс Notifier с абстрактным методом отправки сообщений.
Реализовать конкретные нотификаторы (например, EmailNotifier и PushNotifier), наследуя их от Notifier и реализуя метод отправки.
Создать класс NotificationService, принимающий Notifier и вызывающий его метод отправки.
Процесс:

Импортируем ABC для создания абстрактного класса.
Определяем Notifier с абстрактным методом.
Разрабатываем классы для каждого способа уведомлений (Email, Push), используя полиморфизм.
Для расширения функционала создаем новый класс, например, TelegramNotifier, без изменения существующего кода.
Результат: Теперь NotificationService может легко использовать новые нотификаторы, соответствуя принципу открытости/закрытости: добавление нового функционала без изменения существующего кода.
'''


from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        raise NotImplementedError("Subclasses must implement this method")

@dataclass
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending email with message: {message}")

@dataclass
class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending push notification with message: {message}")

@dataclass
class TelegramNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Telegram message: {message}")

@dataclass
class NotificationService:
    notifier: Notifier

    def send(self, message: str):
        self.notifier.send(message)

# Пример использования
email_notifier = EmailNotifier()
push_notifier = PushNotifier()
telegram_notifier = TelegramNotifier()
service = NotificationService(push_notifier)
service.send("Hello via Email!")
service.notifier = push_notifier
service.send("Hello via Push!")