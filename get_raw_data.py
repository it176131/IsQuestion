from pathlib import Path
from typing import Any

import pandas as pd

from is_question.api import StackOverflow


so = StackOverflow()
questions = so.fetch_questions(filter="withbody")
items: list[dict[str, Any]] = questions.get("items")
df = pd.DataFrame.from_records(items, index="question_id")
data_dir = Path("./data")
data_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(data_dir / "raw.csv")
