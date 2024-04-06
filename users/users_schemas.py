from marshmallow import Schema, fields


class UserSignUpSchema(Schema):
    first_name = fields.Str(required=True, error_messages={"required": "First name is required"})
    last_name = fields.Str(required=True, error_messages={"required": "Last name is required"})
    email = fields.Str(required=True, error_messages={"required": "email is required"})
    password = fields.Str(required=True, error_messages={"required": "password is required"})


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    is_email_verified = fields.Boolean()
    is_phone_verified = fields.Boolean()


