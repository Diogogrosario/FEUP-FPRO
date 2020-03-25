def exception_str(f):
    try:
        f()
    except Exception as ex:
        return ex
    else:
        return "No exception was raised"
        