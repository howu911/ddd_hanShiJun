import re

from modules.user_register.domain.entities import User
from modules.user_register.domain.repositories import UserRepository, SalesRepRepository


class RegistrationService:
    def __init__(self, user_repo: UserRepository, sales_rep_repo: SalesRepRepository):
        self.user_repo = user_repo
        self.sales_rep_repo = sales_rep_repo

    def register_user(self, user_name: str, phone: str) -> User:
        if user_name is None or len(user_name) == 0:
            raise ValueError("User name is required")

        if phone is None or len(phone) == 0 or not self.is_valid_phone(phone):
            raise ValueError("Phone is required")

        area_code = self.get_area_code(phone)
        operator_code = self.get_operator_code(phone)
        sales_rep = self.sales_rep_repo.find(area_code, operator_code)

        if sales_rep is None:
            raise ValueError("No sales rep found for the phone number")

        user = User(user_name, phone, sales_rep.rep_id)

        return self.user_repo.save(user)

    def is_valid_phone(self, phone: str) -> bool:
        phone_pattern = r'^0\d{2,3}-?\d{7,8}$'
        if re.match(phone_pattern, phone):
            return True

        return False

    def get_area_code(self, phone: str) -> str:
        pass

    def get_operator_code(self, phone: str) -> str:
        pass

