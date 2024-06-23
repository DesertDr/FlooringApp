def YNBool_Converter(message):
    yes_no_bool = {
        'n': False,
        'no': False,
        'y': True,
        'ye': True,
        'yes': True
    }
    return yes_no_bool.get(message.lower(), False)