import sys
import logging
import os


class NetworkSecurityException(Exception):
    """
    Custom exception class for network security errors.
    This class captures the error message, line number, and file name
    where the exception occurred.
    Attributes:
        error_message (str): The error message.
        lineno (int): The line number where the exception occurred.
        file_name (str): The file name where the exception occurred.
    Methods:
        __str__(self): Returns a string representation of the exception.
    Usage:
        try:
            # Code that may raise an exception
            pass
        except Exception as e:
            raise NetworkSecurityException(str(e))
    Example:
        try:
            # Some code that raises an exception
            raise ValueError("An example error")
        except Exception as e:
            raise NetworkSecurityException(str(e))
    """
    def __init__(self, error_message):
        self.error_message = error_message
        exc_type, exc_value, exc_tb = sys.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self):
        return f"Error occurred in script: '{self.file_name}' at line: {self.lineno} with message: '{self.error_message}'"
