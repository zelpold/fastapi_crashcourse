from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)
@router.post("")
async def add_tasks(
        task:Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)

    return STaskId(**{"ok":True, "task_id":task_id})


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
