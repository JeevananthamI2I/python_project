# exceptions/exception_handler.py

import logging
from exceptions.custom_exceptions import BankError

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def handle_exception(error):
    """Centralized exception handler for logging errors."""
    if isinstance(error, BankError):
        logger.error(f"BankError: {error}")
    else:
        logger.error(f"Unexpected Error: {error}")
    
    # Optionally raise the error again to be handled at a higher level
    raise error
