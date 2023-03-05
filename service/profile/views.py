from ..decorators import auth_required
from flask import Blueprint, request
from pony import orm

blueprint = Blueprint("profile", __name__, url_prefix="/profile")

@blueprint.route("/info", methods=["GET"])
@orm.db_session
@auth_required
def info():
    return {
        "error": None, "data": {
            "username": request.account.username,
            "firstname": request.account.firstname,
            "lastname": request.account.lastname,
            "email": request.account.email
        }
    }

@blueprint.route("/feedback", methods=["GET"])
@orm.db_session
@auth_required
def feeback():
    return {
        "error": None, "data": {
            "username": request.account.username,
            "feedback": request.account.feeback,
            "mark": request.account.mark
        }
    }

@blueprint.route("/tip", methods=["GET"])
@orm.db_session
@auth_required
def tip():
    return {
        "error": None, "data": {
            "feedback_id": request.account.feedback_id,
            "amount": request.account.amount,
            "status": request.account.status
        }
    }
