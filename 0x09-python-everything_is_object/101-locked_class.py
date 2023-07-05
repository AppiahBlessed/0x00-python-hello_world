#!/usr/bin/python3
'''Have some control over instance sttribute creation
Dont create instance attribute if its not first_name
'''


class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'"
            )
