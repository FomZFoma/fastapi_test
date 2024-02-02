from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings


def create_post_template(
        post: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = 'УСПЕШНЫЙ ВЫХЛОП ПОСТА В СЕТЬ'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>СОЗДАНИЕ ПОСТА НА САЙТЕ Habr</h1>
            Поздравляб  с успешной загрузкой поста  на нашем сайте
            '{post['post_text']}', ТЫ РЕАЛЬНО КРУТ МУЖИК
    """,
        subtype='html'
    )
    return email