import logging

logger: any


def setup_logger(logger_name, log_file=None):
    global logger
    # Configure the logging
    logging.basicConfig(
        level=logging.DEBUG,
        # json string with
        format='{"asctime":%(asctime)s, "name": %(name)s, "levelname":%(levelname)s, "message": %(message)s }',
        handlers=[
            logging.FileHandler(log_file) if log_file else logging.StreamHandler()
        ],
    )

    # Create and return a logger
    logger = logging.getLogger(logger_name)


def get_logger():
    global logger

    if logger is not None:
        return logger

    logger = setup_logger(logger)
    return logger
