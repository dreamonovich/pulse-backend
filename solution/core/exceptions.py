from rest_framework import status


class ReasonException(Exception):
    def __init__(self, reason='Not found', status_code=status.HTTP_404_NOT_FOUND):
        self.reason = reason
        self.status_code = status_code
