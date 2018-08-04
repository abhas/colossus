from django.utils.translation import gettext_lazy as _


class ImportTypes:
    BASIC = 1
    ADVANCED = 2

    LABELS = {
        BASIC: _('Basic'),
        ADVANCED: _('Advanced'),
    }

    CHOICES = tuple(LABELS.items())


class ImportStatus:
    PENDING = 1
    QUEUED = 2
    IMPORTING = 3
    COMPLETED = 4
    ERRORED = 5
    CANCELED = 6

    LABELS = {
        PENDING: _('Pending'),
        QUEUED: _('Queued'),
        IMPORTING: _('Importing'),
        COMPLETED: _('Completed'),
        ERRORED: _('Errored'),
        CANCELED: _('Canceled'),
    }

    CHOICES = tuple(LABELS.items())