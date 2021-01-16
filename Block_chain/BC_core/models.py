from django.db import models
from django.utils import timezone

class Block(models.Model):
    """
    Модель Блока
    """
    # height = models.PositiveIntegerField('Height of block', null=True)    
    hash_block = models.CharField('Hash of block', max_length=200, blank=True)
    time = models.DateTimeField('Time of block', default=timezone.now)
    miner_address = models.CharField('Miner addres', max_length=200, blank=True)
    num_of_transaction = models.PositiveIntegerField('Num of transaction', null=True)

    def __str__(self):
        return 'Hash block: {}\nTime: {}'.format(self.hash_block, self.time)

    # @property
    # def hash_block(self):
    #     return self.hash_block.count()
        