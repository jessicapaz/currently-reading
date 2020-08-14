import os


GOODREADS = {
    'api_key': os.getenv('API_KEY'),
    'base_url': os.getenv('GOODREADS_URL')
}


def validate_env():
    for key, value in GOODREADS.items():
        if value is None:
            raise Exception(
                f"missing GOODREADS {key} variable")
