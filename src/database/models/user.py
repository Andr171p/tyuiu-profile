from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String
from sqlalchemy.dialects.postgresql import ARRAY

from typing import List
from datetime import datetime

from src.database.models.abstract import Abstract


class User(Abstract):
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    gender: Mapped[str]
    bdate: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    sport: Mapped[str]
    foreign: Mapped[str]
    gpa: Mapped[float]
    exams_points: Mapped[int] = mapped_column(nullable=True)
    bonus_points: Mapped[int] = mapped_column(nullable=True)
    exams: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    education: Mapped[str] = mapped_column(nullable=True)
    study_form: Mapped[str] = mapped_column(nullable=True)

    @mapped_column
    def full_name(cls) -> str:
        return f"{cls.first_name} {cls.last_name} {cls.surname}"

    @mapped_column
    def total_points(cls) -> int:
        return cls.exams_points + cls.bonus_points

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.full_name()}, points={self.total_points()})>"
