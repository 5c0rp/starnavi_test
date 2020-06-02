import random
import requests
import yaml

CONF_FILE = input('Config file path (./config.yaml by default): ') \
            or './config.yaml'
BASE_URL = input('Base url (http://127.0.0.1:8000/ by default)') \
           or 'http://127.0.0.1:8000/'


def load_config():
    with open(CONF_FILE, 'r') as file:
        return yaml.full_load(file)


class Bot:

    def __init__(self, base_url, **kwargs):
        self.number_of_users = kwargs.get('number_of_users', 0)
        self.max_posts_per_user = kwargs.get('max_posts_per_user', 0)
        self.max_likes_per_user = kwargs.get('max_likes_per_user', 0)
        self.base_url = base_url
        self.users_storage = []
        self.posts_storage = []

    def get_signup_url(self) -> str:
        return f'{self.base_url}api/v1/signup'

    def get_login_url(self) -> str:
        return f'{self.base_url}api/v1/login'

    def get_post_create_url(self) -> str:
        return f'{self.base_url}api/v1/posts/'

    def get_like_url(self, post_id: str) -> str:
        return f'{self.base_url}api/v1/posts/{post_id}/like/'

    def get_random_posts(self) -> list:
        return random.sample(self.posts_storage, self.likes_count())

    def get_auth_headers(self, token: str) -> dict:
        return {'Authorization': f'JWT {token}'}

    def signup_users(self) -> None:
        url = self.get_signup_url()
        for i in range(self.number_of_users):
            username = f'user_{i}'
            data = {
                'username': username,
                'password': 'strong_password'
            }
            req = requests.post(url, json=data)
            if req.status_code == 201:
                self.users_storage.append(data)

    def login_users(self) -> None:
        url = self.get_login_url()
        for user_cred in self.users_storage:
            req = requests.post(url, json=user_cred)
            if req.status_code == 200:
                user_cred.update(req.json())

    def create_posts(self) -> None:
        url = self.get_post_create_url()
        counter = 0
        for user_cred in self.users_storage:
            post_count = random.randint(0, self.max_posts_per_user)
            for _ in range(post_count):
                data = {
                    'subject': f'Subject_{counter}',
                    'body': 'Some text here'
                }
                req = requests.post(
                    url,
                    json=data,
                    headers={**self.get_auth_headers(user_cred.get('token'))}
                )
                if req.status_code == 201:
                    self.posts_storage.append(req.json())

    def likes_count(self) -> int:
        likes_count = random.randint(0, self.max_likes_per_user)
        if likes_count <= len(self.posts_storage):
            return likes_count
        return len(self.posts_storage)

    def add_likes(self) -> None:
        for user_cred in self.users_storage:
            for post in self.get_random_posts():
                url = self.get_like_url(post.get('id'))
                requests.post(
                    url,
                    headers={**self.get_auth_headers(user_cred.get('token'))}
                )

    def run(self):
        self.signup_users()
        self.login_users()
        self.create_posts()
        self.add_likes()


if __name__ == '__main__':
    print('Bot started!')
    config = load_config()
    bot = Bot(BASE_URL, **config)
    bot.run()
