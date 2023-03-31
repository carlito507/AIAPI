import emails
from emails.template import JinjaTemplate
from app.core.config import SMTP_CONFIG, SECRET_KEY, BASE_URL
import logging
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)


def send_validation_email(email_to: str, validation_link: str):
    # Send email with validation link to new users
    message = emails.Message(
        subject="Please confirm your email",
        mail_from=("carltardifdesign.com", SMTP_CONFIG["sender_email"]),
        html=JinjaTemplate(
            f"""
            <p>Hi there,</p>
            <p>Please click the link below to confirm your email address:</p>
            <p><a href="{validation_link}">{validation_link}</a></p>
            <p>Thanks ans see you soon.</p>
            """
        ),
    )
    response = message.send(to=email_to, render=True, smtp=SMTP_CONFIG)
    logging.info(f"Email sent to {email_to}")
    return response


def generate_validation_link(username: str) -> str:
    # validation link implementation with token generated from username
    f = Fernet(FERNET_KEY)
    encrypted_username = f.encrypt(username.encode())
    logging.info(f"Validation link generated for {username}")
    return f"{BASE_URL}/validate?username={encrypted_username.decode()}"