from .models import User
from .models import Feedback
from .models import Tip

class UserService(object):
    @classmethod
    def get_by_username(cls, username):
        return User.get(username=username)

    @classmethod
    def get_by_email(cls, email):
        return User.get(email=email)

    @classmethod
    def create(cls, username, firstname, lastname, email, password):
        return User(
            username=username, firstname=firstname, lastname=lastname, password=password, email=email
        )

class FeedbackService(object):
    @classmethod
    def get_by_username(cls, username):
        return Feedback.get(username=username)

    @classmethod
    def get_by_mark(cls, mark):
        return Feedback.get(mark=mark)

    @classmethod
    def create(cls, Feedback, username, mark):
        return Feedback(
            username=username, Feedback=Feedback,
            mark=mark
        )

class TipService(object):
    @classmethod
    def get_by_feedback_id(cls, feedback_id):
        return Tip.get(feedback_id=feedback_id)

    @classmethod
    def get_by_status(cls, status):
        return Tip.get(status=status)

    @classmethod
    def create(cls, feedback_id, amount, status):
        return Tip(
            feedback_id=feedback_id, amount=amount,
            status=status
        )
