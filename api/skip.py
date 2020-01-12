from requests import get
from errors import Unauthorized
from config import settings


class Skip(list):
    """ Elects to skip the currently playing song.  Will call the player to
    restart when enough votes have been received from different users.

    .. todo:: move some functionality of this class to the /restart route.
    .. todo:: move ip_whitelist into it's own module
    .. todo:: this functionality will eventually be replaced by proper auth.
    """

    def __init__(self):
        self.votecount = 0
        self.ip_whitelist = settings.api.ip_whitelist

    def __call__(self, username, remote_ip):
        if remote_ip not in self.ip_whitelist:
            raise Unauthorized
        if username is not None:
            for x in self:
                if x == username:
                    raise Unauthorized
            self.append(username)
            self.votecount += 1

            if self.votecount >= 4:
                r = get(settings.api.restart_url, verify=settings.api.ssl_verify)
                return r

    def reset(self):
        """ resets vote count to zero. """
        self.votecount = 0
        self.clear()


votetoskip = Skip()
