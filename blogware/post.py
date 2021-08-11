"""
Contains the models to save and interpret posts,
including markdown formatting
"""

import pydantic
from datetime import datetime

class Post(pydantic.BaseModel):

    title: str
    date: datetime
    content: str