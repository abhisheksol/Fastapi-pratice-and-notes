from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Blog(Base):
    __tablename__ = "fastapi"

    id = Column(Integer, primary_key=True,index=True)
    # email = Column(String, unique=True, index=True)
    title = Column(String)
    body = Column(String)
 