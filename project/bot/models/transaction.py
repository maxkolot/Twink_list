from tortoise import fields, models


class Transaction(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='transactions')
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    payment_method = fields.CharField(max_length=20)  # 'semi-automatic', 'telegram_stars'
    status = fields.CharField(max_length=20, default='pending')  # 'pending', 'confirmed', 'failed'
    date_created = fields.DatetimeField(auto_now_add=True)
    date_confirmed = fields.DatetimeField(null=True)
    transaction_type = fields.CharField(max_length=50)  # 'vip_subscription', 'promo_fire', etc.
    details = fields.TextField(null=True)

    class Meta:
        table = "transactions"

    def __str__(self):
        return f"Transaction(id={self.id}, user_id={self.user.user_id}, amount={self.amount})"
