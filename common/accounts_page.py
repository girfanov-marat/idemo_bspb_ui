from datetime import datetime


CREATE_ACCOUNT_SUCCESS = "Открыт новый счёт для операций в RUB, номер счёта:"


def close_account_message(acc_name):
    return f"Счёт {acc_name} закрыт"


def statement_period(date_from, date_to):
    date_from = datetime.strptime(date_from, "%d%m%Y").strftime("%d.%m.%Y")
    date_to = datetime.strptime(date_to, "%d%m%Y").strftime("%d.%m.%Y")
    return f"Период: {date_from} - {date_to}"


EMAIL_SUCCESS_MESSAGE = "Информационное сообщение отправлено"
