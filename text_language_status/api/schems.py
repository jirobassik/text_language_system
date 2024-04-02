import uuid
from datetime import datetime
from typing import Optional

from ninja import Schema
from history.api.schems import HistoryOut

class StatusOut(Schema):
    id: uuid.UUID
    status: str
    time_add: datetime
    executed: bool
    history_id: Optional[HistoryOut] = None
