import sys
import logging
from exceptions import *
def error_message_detali(error,error_detalis:sys):
    _,_,exc_tb = error_detalis.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename 
    
    # #
    error_message ="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message


class CustomExceptions(Exception):
    def __init__(self, error_message,error_details:sys):

        super().__init__(error_message)

        self.error_message = error_message_detali(error_message,error_detalis=error_details)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a= 1/0
    except Exception as e:
        logging.info("cannot devide by zero")
        raise CustomExceptions(e,sys)
        


