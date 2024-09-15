from tortoise import fields, models


class Referral(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='referrals_made')
    referred_user = fields.ForeignKeyField('models.User', related_name='referred_by')
    date_referred = fields.DatetimeField(auto_now_add=True)
    commission_earned = fields.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        table = "referrals"

    def __str__(self):
        return f"Referral(user_id={self.user.user_id}, referred_user_id={self.referred_user.user_id})"
