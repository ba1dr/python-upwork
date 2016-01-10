# Python bindings to Upwork API
# python-upwork version 0.5
# (C) 2010-2015 Upwork

import logging
import urllib3
try:
    # Python2
    unicode('test')
except NameError:
    # Python3
    unicode = str


class BaseUpworkException(Exception):
    """Base exception class.

    Performs logging.

    """
    def __init__(self, *args, **kwargs):
        self._info = "{0} ; {1}".format(', '.join(args), ', '.join("%s: %s" % e for e in kwargs.items()))
        self.upwork_debug(*args, **kwargs)

    def __str__(self):
        return self._info

    def __unicode__(self):
        return self._info

    def __repr__(self):
        return "%s: %s" % (self.__class__.__name__, self._info)

    def upwork_debug(self, *args, **kwargs):
        logger = logging.getLogger('python-upwork')
        logger.debug('{0}: {1}'.format(
            self.__class__.__name__,
            ', '.join(map(unicode, args))))


class BaseHttpException(urllib3.exceptions.HTTPError, BaseUpworkException):

    def __init__(self, *args, **kwargs):
        # self.upwork_debug(*args, **kwargs)
        super(BaseHttpException, self).__init__(*args, **kwargs)


class HTTP400BadRequestError(BaseHttpException):
    pass


class HTTP401UnauthorizedError(BaseHttpException):
    pass


class HTTP403ForbiddenError(BaseHttpException):
    pass


class HTTP404NotFoundError(BaseHttpException):
    pass


class InvalidConfiguredException(BaseException):
    pass


class APINotImplementedException(BaseException):
    pass


class AuthenticationError(BaseException):
    pass


class NotAuthenticatedError(BaseException):
    pass


class ApiValueError(BaseException):
    pass


class IncorrectJsonResponseError(BaseException):
    pass
