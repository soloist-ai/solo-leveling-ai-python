from dataclasses import dataclass, field
from typing import List
from dataclasses_avroschema import AvroModel
from src.avro.enums.task_rarity import TaskRarity
from src.avro.enums.task_topic import TaskTopic



@dataclass
class GenerateTask(AvroModel):
    taskId: str
    version: int = 0
    rarity: TaskRarity = field(default=TaskRarity.COMMON)
    topics: List[TaskTopic] = field(default_factory=list)

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"


@dataclass
class GenerateTasksEvent(AvroModel):
    transactionId: str
    playerId: int
    inputs: List[GenerateTask]

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"