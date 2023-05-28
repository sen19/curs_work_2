import logging

api_logger = logging.getLogger('api_log')
api_logger.level = logging.INFO
file_handler = logging.FileHandler('api/logs/api.log', 'a', 'utf-8')
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_api)
api_logger.addHandler(file_handler)