from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from ..database import Base


# ===== AUTOMATION MODEL =====
class Automation(Base):
    __tablename__ = "automations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    created_at = Column(
        DateTime, nullable=False, index=True, default=datetime.now(timezone.utc)
    )
    times_used = Column(Integer, nullable=False, default=0, index=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, automation_id):
        return session.query(cls).filter_by(id=automation_id).first()

    def update(self, session, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()
