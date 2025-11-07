from dataclasses import dataclass, field
from typing import List
from dataclasses_avroschema import AvroModel
from src.avro.enums.task_rarity import TaskRarity
from src.avro.enums.task_topic import TaskTopic
from src.avro.events.generate_tasks_event import GenerateTask
from src.models.generate_task_response import Task as PydanticTask


@dataclass
class SaveTask(AvroModel):
    taskId: str = ""
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

    @classmethod
    def from_generated(
        cls, task_data: GenerateTask, result_task: PydanticTask
    ) -> "SaveTask":
        return cls(
            taskId=task_data.taskId,
            version=task_data.version,
            rarity=task_data.rarity,
            topics=task_data.topics,
            title=result_task.title,
            description=result_task.description,
            experience=result_task.experience,
            currencyReward=result_task.currencyReward,
            agility=result_task.agility,
            strength=result_task.strength,
            intelligence=result_task.intelligence,
        )


@dataclass
class SaveTasksEvent(AvroModel):
    transactionId: str
    playerId: int
    tasks: List[SaveTask]

    class Meta:
        namespace = "com.sleepkqq.sololeveling.avro.task"
