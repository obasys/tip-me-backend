from webargs import fields, validate

join_args = {
    "username": fields.Str(required=True, validate=validate.Length(min=4, max=32)),
    "password": fields.Str(required=True, validate=validate.Length(min=8)),
    "firstname": fields.Str(required=True),
    "lastname": fields.Str(required=True),
    "email": fields.Email(required=True)
}

login_args = {
    "password": fields.Str(required=True, validate=validate.Length(min=8)),
    "email": fields.Email(required=True)
}
