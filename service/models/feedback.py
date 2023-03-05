from datetime import datetime
from .base import db
from pony import orm

class Feedback(db.Entity):
    _table_ = "feedbacks"

    created = orm.Optional(datetime, default=datetime.utcnow)
    username = orm.Required(str)
    feedback = orm.Required(str)
    mark = orm.Required(int)