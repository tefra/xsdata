def arguments(data: dict):
    def quote(value):
        return (
            '"{}"'.format(value.replace('"', "'"))
            if isinstance(value, str)
            else value
        )

    return ",\n".join([f"{key}={quote(value)}" for key, value in data.items()])
