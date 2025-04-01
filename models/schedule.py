from models.timestamp import TimestampModel
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

class ScheduleModel(TimestampModel):
    __tablename__ = 'schedules'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    schedule_date: Mapped[str] = mapped_column(Date, nullable=False)
    schedule_time: Mapped[str] = mapped_column(String(30), nullable=False)
    client: Mapped[str] = mapped_column(String(150), nullable=False)
    tuss_code: Mapped[str] = mapped_column(String(30), nullable=False)
    tuss_description: Mapped[str] = mapped_column(String(150), nullable=False)
    agreement: Mapped[str] = mapped_column(String(50), nullable=True)
    
    