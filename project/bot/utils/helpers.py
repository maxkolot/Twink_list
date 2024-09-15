import random
import string
from fpdf import FPDF
import hashlib
from datetime import datetime

def generate_password(length: int = 8) -> str:
    """Генерация случайного пароля"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))



def generate_promo_code() -> str:
    """Генерация уникального промо-кода"""
    current_time = datetime.now().isoformat()
    return hashlib.sha1(current_time.encode()).hexdigest()[:10]



def create_pdf_report(data: dict, filename: str = 'report.pdf') -> str:
    """Создание простого PDF отчета по каналам"""
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Отчет по каналам", ln=True, align="C")

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    filepath = f"./project/reports/{filename}"
    pdf.output(filepath)
    return filepath
