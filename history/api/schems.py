from datetime import datetime

from ninja import Schema


class HistoryOut(Schema):
    input_text: str
    result_text: str
    created_at: datetime
