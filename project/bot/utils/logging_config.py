import logging

def setup_logging(log_file: str = './project/logs/logging.txt'):
    """Настройка логирования"""
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
