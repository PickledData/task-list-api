from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    goals: Mapped[list["Goal"]] = relationship(back_populates="task")

    def to_dict(self):
        goal_as_dict = {
            "id":self.id,
            "title":self.title
        }
        return goal_as_dict
    
    @classmethod
    def from_dict(cls, goal_data):
        new_goal = cls(title=goal_data["title"])

        return new_goal
