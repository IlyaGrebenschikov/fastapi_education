import logging

from src.core.settings import load_logger_settings, LoggerSettings


class Logger:
    def __init__(self, settings: LoggerSettings) -> None:
        self._settings = settings
        
    def _setup_file_handler(self) -> logging.FileHandler:
        handler = logging.FileHandler(self._settings.dir_path / 'base.log')
        
        handler.setFormatter(self._settings.formater)
        handler.setLevel(self._settings.level)
        
        return handler
    
    def _setup_stream_handler(self) -> logging.StreamHandler:
        handler = logging.StreamHandler()
        
        handler.setFormatter(self._settings.formater)
        handler.setLevel(self._settings.level)
        
        return handler
    
    def load_logger(self) -> logging.Logger:
        logger = logging.getLogger(self._settings.name)
        file_handler = self._setup_file_handler()
        stream_handler = self._setup_stream_handler()
        
        logger.setLevel(self._settings.level)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        
        return logger


log_settings = load_logger_settings()
log = Logger(log_settings).load_logger()
