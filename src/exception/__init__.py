import sys
import traceback

class NetworkException(Exception):
    """
    Base class for all network-related exceptions.
    """
    def __init__(self, error_message, error_details: sys):
        # Extract traceback information
        _, _, exc_tb = error_details.exc_info()
        if exc_tb is not None:
            # Extract the file name and line number from the traceback
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            # Format the error message to include the file name and line number
            error_message = f"Error occurred in script: {file_name} at line: {line_number} - {error_message}"
        else:
            # Fallback if no traceback is available
            error_message = f"Error: {error_message}"
        
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        raise NetworkException("This is a custom error message", sys)
    except NetworkException as e:
        raise e
