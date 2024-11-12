from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .goal import Goal


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str] 
    completed_at: Mapped[str] = mapped_column(nullable=True)
    goal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("goal.id"))
    goal: Mapped[Optional["Goal"]] = relationship(back_populates="tasks")

def to_dict(self):
    task_as_dict = {
        "id": self.id,
        "title": self.name,
        "description":self.description,
        "completed_at":self.completed_at
    }

    return task_as_dict

@classmethod
def from_dict(cls, task_data):
    new_task = cls(title=task_data["title"])
    return new_task