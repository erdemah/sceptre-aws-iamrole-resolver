# -*- coding: utf-8 -*-


class IAMRoleNotFoundError(Exception):
    """
    Error raised when the IAM Role does not exist
    """
    pass


class IAMRoleAmbiguousError(Exception):
    """
    Error raised when the partial IAM Role name matches more than one role
    """
    pass
