from marshmallow import Schema, fields, validate


class UserSignUpReq(Schema):
    first_name = fields.Str(required=True, error_messages={"required": "First name is required"})
    last_name = fields.Str(required=True, error_messages={"required": "Last name is required"})
    email = fields.Str(required=True, validate=validate.Email(error="Invalid email format"),
                       error_messages={"required": "Email is required"})
    password = fields.Str(required=True, error_messages={"required": "Password is required"})
