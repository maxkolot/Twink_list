from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Advertisement(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='advertisements')
    ad_type = fields.CharField(max_length=20)  # 'ads_in_bot', 'ads_in_list', 'ads_in_channels'
    media_id = fields.CharField(max_length=255, null=True)  # File ID в Telegram
    description = fields.TextField()
    buttons = fields.JSONField(null=True)
    status = fields.CharField(max_length=20, default='pending')  # 'pending', 'approved', etc.
    price = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    scheduled_datetime = fields.DatetimeField(null=True)
    date_created = fields.DatetimeField(auto_now_add=True)
    date_updated = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, ad_type={self.ad_type}, status={self.status})"
