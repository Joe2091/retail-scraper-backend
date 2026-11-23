from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from retail_scraper_backend.database.connection import Base


class Retailer(Base):
    __tablename__ = "retailers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    website: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )