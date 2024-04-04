from modules.user_register.domain.entities import User
from modules.user_register.domain.repositories import UserRepository


class MysqlUserRepostory(UserRepository):
    def __init__(self):
        pass

    def save(self, user: User):
        print(f'Saving user {user.name} to MySQL database, user info: {user.__dict__}')
