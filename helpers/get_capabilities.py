from config.android_capabilities import android_capabilities
from config.ios_capabilities import ios_capabilities


def get_capabilities(env):
    if env == 'android':
        return android_capabilities()
    elif env == 'ios':
        return ios_capabilities()
    else:
        raise ValueError(f"Environment '{env}' is not supported.")