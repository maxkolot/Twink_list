from tortoise import fields, models


class Promo(models.Model):
    id = fields.IntField(pk=True)
    media_id = fields.CharField(max_length=255, null=True)
    description = fields.TextField()
    buttons = fields.JSONField(null=True)
    code = fields.CharField(max_length=100, unique=True)
    date_created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "promos"

    def __str__(self):
        return f"Promo(id={self.id}, code={self.code})"
