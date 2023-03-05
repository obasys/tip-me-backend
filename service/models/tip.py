from datetime import datetime
from .base import db
from pony import orm

class Tip(db.Entity):
    _table_ = "tips"

    created = orm.Optional(datetime, default=datetime.utcnow)
    feedback_id = orm.Required(int)
    amount = orm.Required(str)
    status = orm.Required(bool, default=False)
