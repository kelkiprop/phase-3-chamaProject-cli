from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    # Relationships
    contributions = relationship("Contribution", back_populates="member", cascade="all, delete")
    loans = relationship("Loan", back_populates="member", cascade="all, delete")

class Contribution(Base):
    __tablename__ = 'contributions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    member_id = Column(Integer, ForeignKey('members.id', ondelete="CASCADE"))

    # Relationship.schema tablename

    member = relationship("Member", back_populates="contributions")

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, default="pending")  # Ensure Loan has a status column
    member_id = Column(Integer, ForeignKey('members.id', ondelete="CASCADE"))

    # Relationship
    member = relationship("Member", back_populates="loans")
