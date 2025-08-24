import sys
import traceback
from typing import Optional, cast

class DocumentPortalException(Exception):
    """Custom exception for Document Portal"""
    def __init__(self, error_message: str, error_details: Optional[object] = None):
        # normalize message
        if isinstance(error_message, BaseException):
            norm_msg = str(error_message)
        else:
            norm_msg = str(error_message)
        
        # resolve exc_info (supports: sys module, Exception object or current context)
        exc_type = exc_value = exc_tb = None
        if error_details is None:
            exc_type, exc_value, exc_tb = sys.exc_info()
        else:
            if hasattr(error_details, "exc_info"):
                exc_info_obj = cast(sys, error_details)
                exc_type, exc_value, exc_tb = exc_info_obj.exc_info()
            elif isinstance(error_details, BaseException):
                exc_type, exc_value, exc_tb = type(error_details), error_details, error_details.__traceback__
            else:
                exc_type, exc_value, exc_tb = sys.exc_info()

        # walk to the last frame to report the most relevant location
        last_tb = exc_tb
        while last_tb and last_tb.tb_next:
            last_tb = last_tb.tb_next

        self.file_name = last_tb.tb_frame.f_code.co_filename if last_tb else "<unknown>"
        self.line_no = last_tb.tb_lineno if last_tb else -1
        self.error_message = norm_msg
        
        self.error_message = norm_msg

        # full pretty traceback (if available)
        if exc_type and exc_tb:
            self.traceback_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            self.traceback_str = ""

        super().__init__(self.__str__())

    def __str__(self):
        # compact, logger-friendly message (no leading spaces)
        base = f"Error in [{self.file_name}] at line [{self.line_no}] | Message: {self.error_message}"
        if self.traceback_str:
            return f"{base}\nTraceback:\n{self.traceback_str}"
        return base
    
    def __repr__(self):
        return f"DocumentPortalException(file={self.file_name!r}, line={self.line_no}, message={self.error_message!r})"

if __name__ == "__main__":
    try:
        a = 1 / 0
        print(a)
    except Exception as e:
        app_exc = DocumentPortalException(e, sys)
        # logger.error(app_exc)
        raise app_exc