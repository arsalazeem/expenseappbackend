from marshmallow import Schema, fields


class UserSignUpRes(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    is_email_verified = fields.Boolean()
    is_phone_verified = fields.Boolean()
