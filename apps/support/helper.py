def constants(key, default=''):
    from apps.configs.constants import CONSTANTS
    return CONSTANTS[key] if key in CONSTANTS else default
