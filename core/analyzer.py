def analyze_error(log: str):
    if "ModuleNotFoundError" in log:
        return "missing_dependency"

    if "SyntaxError" in log:
        return "syntax_error"

    if "KeyError" in log:
        return "data_error"

    if "TypeError" in log:
        return "type_error"

    if "FileNotFoundError" in log:
        return "file_error"

    if "NameError" in log:
        return "name_error"

    return "unknown"
