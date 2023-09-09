from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    A CustomUser class is added so we can add functionality later. It's more convenient then not to add CustomUser at beginning of project before database migrations are started.
    """
    registration_accepted = models.BooleanField(
        "Registration accepted",
        default=False,
        help_text="Designates whether this user is accepted for registration.",
    )

    def __str__(self):
        """
        String representation of `CustomUser` is `username`.
        """
        return self.username