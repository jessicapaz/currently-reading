class GoodreadsException(Exception):
    """Exception raised when an error occurred handling request to Goodreads."""
    def __init__(self):
        super().__init__("Couldn't get books from Goodreads API")
