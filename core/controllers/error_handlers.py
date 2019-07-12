from flask_restful import abort


def handle_schema_error(func):
    def error_handler(*args, **kwargs):
        if args[0]._errors:
            abort(404, errors=args[0]._errors)

        return func(*args, **kwargs)
    return error_handler
