import sys 
# The sys library will automatically have the info of any exception that is being generated in the current runtime environment.
from logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    # where did the exception occured? : file_name.py
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occured in python script[{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # string like below will be created.
    # Error occured in python script[main.py] line number [45] error message [division by zero]

    return error_message

# This will be called when we write something like: raise CustomeException(e, sys)
class CustomException(Exception): # so Exception will be a superclass of our CustomException
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
