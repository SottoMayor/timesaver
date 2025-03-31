from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import db

class TimestampModel(db.Model):
    __abstract__ = True
    created: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
