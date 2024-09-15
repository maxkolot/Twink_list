from tortoise import fields, models


class ScheduledTask(models.Model):
    id = fields.IntField(pk=True)
    task_type = fields.CharField(max_length=50)  # 'send_list', 'send_ad', 'notify_user', etc.
    scheduled_datetime = fields.DatetimeField()
    parameters = fields.JSONField()
    status = fields.CharField(max_length=20, default='pending')  # 'pending', 'completed', 'failed'
    date_created = fields.DatetimeField(auto_now_add=True)
    date_updated = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "scheduled_tasks"

    def __str__(self):
        return f"ScheduledTask(id={self.id}, task_type={self.task_type}, status={self.status})"
