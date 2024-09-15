from tortoise import fields, models


class Channel(models.Model):
    id = fields.IntField(pk=True)
    channel_id = fields.BigIntField(unique=True)  # Telegram ID канала
    name = fields.CharField(max_length=255)
    link = fields.CharField(max_length=255)
    user = fields.ForeignKeyField('models.User', related_name='channels')
    date_added = fields.DatetimeField(auto_now_add=True)
    status = fields.CharField(max_length=20, default='free')  # 'free', 'vip', 'blocked'
    date_expiration = fields.DatetimeField(null=True)
    subscribers_count = fields.IntField(default=0)
    promo_fire = fields.BooleanField(default=False)
    promo_fire_expiration_date = fields.DatetimeField(null=True)

    class Meta:
        table = "channels"

    def __str__(self):
        return f"Channel(id={self.channel_id}, name={self.name})"
