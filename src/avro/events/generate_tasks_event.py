from dataclasses import dataclass, field
from typing import List
from dataclasses_avroschema import AvroModel
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic


@dataclass
class GenerateTask(AvroModel):
    taskId: str
    version: int = 0
    rarity: Rarity = field(default=Rarity.COMMON)
    topics: List[TaskTopic] = field(default_factory=list)

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"


@dataclass
class GenerateTasksEvent(AvroModel):
    txId: str
    playerId: int
    inputs: List[GenerateTask]

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"
