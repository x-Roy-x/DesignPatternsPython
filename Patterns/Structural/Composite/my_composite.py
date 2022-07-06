import abc
from enum import Enum


class PostStatus(Enum):

    PACKAGE = 0
    GLASS = 1
    GENERAL = 2
    FAST = 3


class PostPackage:

    def __init__(self, name, address, status=PostStatus.PACKAGE):
        self.name = name
        self.address = address
        self.status = status
        self._parent = None

    @property
    def post_composite(self):
        return self._parent

    @post_composite.setter
    def post_composite(self, post_composite):
        self._parent = post_composite

    def load(self):
        pass

    def unload(self):
        pass

    @abc.abstractmethod
    def deliver(self):
        pass


class PostComposite(PostPackage):

    def __init__(self, name, address):
        self._posts = []
        super().__init__(name, address)

    def load(self, post):
        post.post_composite = self
        self._posts.append(post)

    def unload(self, post):
        self._posts.remove(post)

    def deliver(self):
        print(f"Deliver {self.status} to post station {self.name} by {self.address}")

        for post in self._posts:
            post.deliver()


class PostGlass(PostPackage):

    def __init__(self, name, address):
        super().__init__(name, address, PostStatus.GLASS)

    def deliver(self):
        print(f"{self.name} can take your post in {self.post_composite.name} by {self.post_composite.address}")


class PostFast(PostPackage):

    def __init__(self, name, address):
        super().__init__(name, address, PostStatus.FAST)

    def deliver(self):
        print(f"Post man delivers post to {self.address}")


if __name__ == '__main__':
    post_station_1 = PostComposite("Post station 1", "London 123")
    post_station_1.load(PostFast("John", "Small town 3"))
    post_station_1.load(PostGlass("Jo", "Green street 10"))

    post_station_2 = PostComposite("Post station 2", "Main Ukraine")
    post_station_2.load(PostFast("Oleh", "Lviv 2"))

    post_station_1.load(post_station_2)

    post_station_1.deliver()







