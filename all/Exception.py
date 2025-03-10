'''This throws Different Errors'''

class NetworkError(Exception):
    '''Throw Network connection error'''

class NetworkTimeOutError(Exception):
    '''Throw Network TimeOut Error, if the time exceeds the limits'''

class NetworkConnectionError(Exception):
    '''Throw an error if program is not connected with internet'''