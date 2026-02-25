from typing import List, Optional

from pydantic import BaseModel

from src.avro.events.task import Task
from src.avro.enums.save_tasks_operation import SaveTasksOperation


class SaveTasksEvent(BaseModel):
    txId: Optional[str] = None
    userId: Optional[int] = None
    tasks: Optional[List[Task]] = None
    operation: Optional[SaveTasksOperation] = None
