"""contents of api.py"""
from os import getenv
from typing import Any

from stackapi import StackAPI


class StackOverflow(StackAPI):
    """A subclass of `StackAPI` that limits API calls to StackOverflow."""

    def __init__(self, key: str | None = None, **kwargs):
        if key is None:
            key = getenv("stackapi_key")
        super().__init__(name="stackoverflow", key=key, **kwargs)
        self._quota_remaining: int | None = None

    def fetch(
            self, endpoint=None, page=1, key=None, filter='default', **kwargs
    ) -> dict[str, Any]:
        response = super().fetch(
            endpoint=endpoint, page=page, key=key, filter=filter, **kwargs
        )
        self._quota_remaining = response.get("quota_remaining")
        return response

    @property
    def quota_remaining(self) -> int | None:
        return self._quota_remaining

    def fetch_questions(
            self, question_ids: list[int] | None = None, **kwargs
    ) -> dict[str, Any]:
        """Fetch questions from Stack Overflow."""
        endpoint = "questions"
        if question_ids is None:
            response = self.fetch(endpoint=endpoint, **kwargs)
        else:
            endpoint += "/{ids}"
            response = self.fetch(endpoint=endpoint, ids=question_ids, **kwargs)
        return response
