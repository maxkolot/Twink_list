from tortoise import fields, models


class ChannelStatistic(models.Model):
    id = fields.IntField(pk=True)
    channel = fields.ForeignKeyField('models.Channel', related_name='statistics')
    date = fields.DateField()
    subscribers_count = fields.IntField()
    joins_from_bot = fields.IntField(default=0)
    joins_from_list = fields.IntField(default=0)

    class Meta:
        table = "channel_statistics"

    def __str__(self):
        return f"ChannelStatistic(channel_id={self.channel.channel_id}, date={self.date})"
