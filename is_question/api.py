from os import getenv
from typing import Any

from stackapi import StackAPI


class StackOverflow(StackAPI):
    def __init__(self, key: str | None = None, **kwargs):
        if key is None:
            key = self._get_key()
        super().__init__(
            name="stackoverflow", versions="2.2", key=key, **kwargs
        )
        self._quota_remaining: int | None = None

    @staticmethod
    def _get_key() -> str | None:
        return getenv(key="stackapi_key")

    @property
    def quota_remaining(self) -> int | None:
        return self._quota_remaining

    def fetch(
        self,
        endpoint: str | None = None,
        page: int = 1,
        key: str | None = None,
        filter: str = "default",
        **kwargs,
    ) -> dict[str, Any]:
        super().fetch.__doc__
        results = super().fetch(
            endpoint=endpoint,
            page=page,
            key=key,
            filter=filter,
            **kwargs,
        )
        self._quota_remaining = results.get("quota_remaining")
        return results

    def fetch_questions(
        self, question_ids: list[int] | None = None, **kwargs
    ) -> dict[str, Any]:
        endpoint = "questions"
        if question_ids is None:
            questions = self.fetch(endpoint=endpoint, **kwargs)
        else:
            endpoint += "/{ids}"
            questions = self.fetch(
                endpoint=endpoint, ids=question_ids, **kwargs
            )
        return questions
