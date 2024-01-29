from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings


def create_post_template(
        post: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = 'ТОП 10-ПОСТОВ'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>РЕГИСТРАЦИЯ НА САЙТЕ</h1>
            Поздравляб  с успешной регистрацией на сайте
    """,
        subtype='html'
    )
    return email