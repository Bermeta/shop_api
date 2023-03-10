from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    full_link_server = f'http://34.125.235.247/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте свой аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по  ссылке: \n{full_link}\n{full_link_server}',
        'bermetzarlyk@gmail.com',
        [user],
        fail_silently=False
    )

def send_reset_email(user):
    code = user.activation_code
    email = user.email
    send_mail('Letter with password reset code!', f"Your reset code {code}", 'bermetzarlyk@gmail.com', [email, ],
              fail_silently=False)


def send_notification(user_email, order_id, price):
    send_mail(
        'Уведомление о создании заказа!',
        f'''Вы создали заказ {order_id},ожидайте звонка!
        Полная стоимость  вашего заказа: {price}. Спасибо что выбрали нас!''',
        'from@example.com',
        [user_email],
        fail_silently=False
    )

