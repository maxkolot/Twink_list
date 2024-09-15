from tortoise import fields, models


class TemporaryChannel(models.Model):
    id = fields.IntField(pk=True)
    channel_id = fields.BigIntField()
    password = fields.CharField(max_length=255)
    user = fields.ForeignKeyField('models.User', related_name='temporary_channels')
    date_created = fields.DatetimeField(auto_now_add=True)
    expires_at = fields.DatetimeField()

    class Meta:
        table = "temporary_channels"

    def __str__(self):
        return f"TemporaryChannel(channel_id={self.channel_id}, user_id={self.user.user_id})"
