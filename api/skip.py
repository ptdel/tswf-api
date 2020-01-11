from requests import get
from errors import Unauthorized
from config import settings


class Skip(list):
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
        self.votecount = 0
        self.clear()


votetoskip = Skip()
