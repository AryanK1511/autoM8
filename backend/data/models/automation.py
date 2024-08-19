from sqlalchemy import Column, Integer, String
from ..database import Base

# ===== AUTOMATION MODEL =====
class Automation(Base):
    __tablename__ = 'automations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, automation_id):
        print()
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
