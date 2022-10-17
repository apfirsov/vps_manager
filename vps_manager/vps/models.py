import uuid

from django.db import models


class VirtualPrivateServer(models.Model):
    """VPS model."""

    STARTED = 'started'
    BLOCKED = 'blocked'
    STOPPED = 'stopped'

    STATUS_CHOICES = (
        (STARTED, 'Работает'),
        (BLOCKED, 'Заблокирован'),
        (STOPPED, 'Остановлен')
    )

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    cpu = models.PositiveSmallIntegerField('количество ядер')
    ram = models.PositiveSmallIntegerField('объем RAM')
    hdd = models.PositiveIntegerField('объем HDD')
    status = models.CharField(
        'Статус',
        max_length=7,
        choices=STATUS_CHOICES,
        default=STOPPED
    )

    class Meta:
        default_related_name = 'servers'
        verbose_name = 'VPS'

    def __str__(self):
        return f'VPS: {self.cpu} CPU / {self.ram} RAM / {self.hdd} HDD'
