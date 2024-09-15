from models.transaction import Transaction

async def process_payment(transaction_id: int) -> bool:
    """Обработка платежа по транзакции"""
    transaction = await Transaction.get_or_none(id=transaction_id)
    if transaction and transaction.status == 'pending':
        # Проверка платежа. Например, если администратор подтверждает платеж
        transaction.status = 'confirmed'
        await transaction.save()
        return True
    return False
