"""
Application entry point
"""
import logging

import cyclops.app

root_logger = logging.getLogger()
root_logger.setLevel(level=logging.INFO)

try:
    app = cyclops.app.create_app()
except:
    root_logger.exception('Error starting application')
    raise
