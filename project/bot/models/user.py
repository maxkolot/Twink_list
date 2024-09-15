from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)  # Telegram ID пользователя
    language = fields.CharField(max_length=2, default='ru')  # 'ru' или 'en'
    status = fields.CharField(max_length=20, default='active')  # 'active', 'inactive', 'blocked'
    date_joined = fields.DatetimeField(auto_now_add=True)
    referral = fields.ForeignKeyField('models.User', related_name='referrals', null=True)
    balance = fields.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_referrals = fields.IntField(default=0)
    is_admin = fields.BooleanField(default=False)

    class Meta:
        table = "users"

    def __str__(self):
        return f"User(id={self.user_id}, status={self.status})"
