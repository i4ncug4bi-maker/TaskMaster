from sqlalchemy.orm import Session
from app import models, schemas


def list_tasks(db: Session, owner_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == owner_id)
        .order_by(models.Task.done.asc(), models.Task.id.desc())
        .all()
    )


def get_task(db: Session, task_id: int, owner_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id, models.Task.owner_id == owner_id)
        .first()
    )


def create_task(db: Session, task: schemas.TaskCreate, owner_id: int):
    db_task = models.Task(
        title=task.title.strip(),
        category=task.category.strip() if task.category else None,
        due_date=task.due_date,
        priority=task.priority,
        done=task.done,
        owner_id=owner_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: schemas.TaskUpdate, owner_id: int):
    db_task = get_task(db, task_id, owner_id)
    if not db_task:
        return None

    data = task.model_dump(exclude_unset=True)

    if "title" in data and data["title"] is not None:
        data["title"] = data["title"].strip()
    if "category" in data and data["category"] is not None:
        data["category"] = data["category"].strip() or None

    for key, value in data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, owner_id: int):
    db_task = get_task(db, task_id, owner_id)
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()
    return True
