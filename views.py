from django.conf import settings
from django.core.mail import send_mail
subject = 'welcome to GFG world'
message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
email_from = settings.EMAIL_HOST_USER
recipient_list = [user.email, ]
send_mail( subject, message, email_from, recipient_list )
