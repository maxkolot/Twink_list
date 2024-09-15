from tortoise import fields, models


class UserStatistic(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='statistics')
    date = fields.DateField()
    messages_sent = fields.IntField(default=0)
    ads_requested = fields.IntField(default=0)

    class Meta:
        table = "user_statistics"

    def __str__(self):
        return f"UserStatistic(user_id={self.user.user_id}, date={self.date})"
