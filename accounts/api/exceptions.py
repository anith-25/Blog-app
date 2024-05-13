from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _

class MailAlreadyInUseException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_code = _("email_exists")
    default_detail = _("The email is already in use.")


class PasswordsDoNotMatchException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_code = _("passwords_do_not_match")
    default_detail = _("The passwords do not match.")