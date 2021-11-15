import warnings


def ignore_warning(action='ignore'):
    """ignore warning message

    Parameter
    ---------
    action : str
        default ignore
    """
    warnings.filterwarnings(action=action)

