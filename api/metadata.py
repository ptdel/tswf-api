import pafy


class Metadata:
    def __init__(self, url):
        self.metadata = pafy.new(url)
        self.url = url

    def to_dict(self):
        return dict(
            title=self.metadata.title, duration=self.metadata.duration, url=self.url,
        )
