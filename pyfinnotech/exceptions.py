class FinnotechException(Exception):
    def __init__(self, message, logger):
        """
        :param message: error message
        """
        self.message = message
        logger.error(f"Stexchange RPC Error: {message}")
