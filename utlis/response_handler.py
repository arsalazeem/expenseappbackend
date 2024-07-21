from localisation import LocalizedResponseHandler


def response_handler(**kwargs):
    data = kwargs.get("data")
    if data is None:
        data = []
    msg = kwargs.get("msg_type")
    status_code = kwargs.get("status_code")
    # get string key from localisation handler
    localisation = LocalizedResponseHandler()
    description_code = str(kwargs.get("description_code"))
    description = localisation.getString(description_code)
    return {"msg": msg, "data": data, "description": description}, status_code
