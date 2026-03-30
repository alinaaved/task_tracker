from sqlalchemy.orm import Session

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate) -> Task:
    task = Task(
        title=task_data.title,
        description=task_data.description
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session) -> list[Task]:
    return db.query(Task).order_by(Task.id).all()


def get_task(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task: Task, task_data: TaskUpdate) -> Task:
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.is_done is not None:
        task.is_done = task_data.is_done

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()