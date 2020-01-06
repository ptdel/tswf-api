from requests import get
from errors import Unauthorized


class Skip(list):
    def __init__(self):
        self.votecount = 0
        self.ip_whitelist = ["127.0.0.1"]

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
                r = get("http://127.0.0.1:8081/restart", verify=False)
                return r

    def reset(self):
        self.votecount = 0
        self.clear()


votetoskip = Skip()
