from dataclasses import dataclass, field
from typing import List
from dataclasses_avroschema import AvroModel
from src.avro.enums.task_rarity import TaskRarity
from src.avro.enums.task_topic import TaskTopic

@dataclass
class SaveTask(AvroModel):
    taskId: str
    version: int = 0
    title: str = ""
    description: str = ""
    experience: int = 0
    currencyReward: int = 0
    rarity: TaskRarity = field(default=TaskRarity.COMMON)
    topics: List[TaskTopic] = field(default_factory=list)
    agility: int = 0
    strength: int = 0
    intelligence: int = 0

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"


@dataclass
class SaveTasksEvent(AvroModel):
    transactionId: str
    playerId: int
    tasks: List[SaveTask]

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"

