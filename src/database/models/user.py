from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base
from src.database.models.base.mixins import ModelWithIDMixin, ModelWithTimeMixin


class UserModel(ModelWithIDMixin, ModelWithTimeMixin, Base):
    __tablename__ = 'user'

    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(nullable=False, default=False)
