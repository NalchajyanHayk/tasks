from abc import ABC, abstractmethod
from datetime import datetime
from validations import Validations

# Abstract class for social media operations
class SocialMediaOperation(ABC):
    @abstractmethod
    def create_post(self, post):
        pass

    @abstractmethod
    def view_posts(self):
        pass

    @abstractmethod
    def create_comment(self, post, comment):
        pass

    @abstractmethod
    def manage_profile(self):
        pass

# Interface for different types of posts
class Post(ABC):
    def __init__(self, user, content):
        self._user = user
        self._content = content
        self._timestamp = datetime.now()


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if Validations.is_valid_name(user):
            self._user = user
        else:
            raise ValueError("Invalid user name")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self._content = content
        else:
            raise ValueError("Content must be a string")

    @property
    def timestamp(self):
        return self._timestamp

    @abstractmethod
    def post_type(self):
        pass
class TextPost(Post):
    def post_type(self):
        return "Text"

class ImagePost(Post):
    def post_type(self):
        return "Image"

class User:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._posts = []
        self._comments = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        if isinstance(contact_info, str) and contact_info:
            self._contact_info = contact_info
        else:
            raise ValueError("Contact information must be a non-empty string.")

    @property
    def posts(self):
        return self._posts

    @property
    def comments(self):
        return self._comments

    def create_post(self, post):
        self._posts.append(post)

    def view_posts(self):
        for post in self._posts:
            print(f"{post._user.name} ({post.post_type()} post, {post._timestamp}): {post._content}")

    def create_comment(self, post, comment):
        new_comment = Comment(self, post, comment)
        self._comments.append(new_comment)

    def manage_profile(self):
        print(f"User Profile - Name: {self.name}, Contact: {self.contact_info}")

class Comment:
    def __init__(self, user, post, content):
        self._user = user
        self._post = post
        self._content = content
        self._timestamp = datetime.now()

    @property
    def user(self):
        return self._user

    @property
    def post(self):
        return self._post

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

# Example usage
if __name__ == "__main__":
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    text_post = TextPost(user1, "Hello, world!")
    image_post = ImagePost(user2, "image.jpg")

    user1.create_post(text_post)
    user2.create_post(image_post)

    user1.view_posts()
    user2.view_posts()

    user1.create_comment(text_post, "Nice post!")
    user2.create_comment(image_post, "Beautiful image!")

    for comment in user1.comments:
        print(f"{comment.user.name} commented on {comment.post.user.name}'s {comment.post.post_type()} post: {comment.content}")

    user1.manage_profile()
    user2.manage_profile()
