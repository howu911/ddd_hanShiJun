from modules.user_register.domain.services import RegistrationService
from modules.user_register.infrastructure.sales_repository import MysqlSalesRepRepository
from modules.user_register.infrastructure.user_repository import MysqlUserRepostory

if __name__ == '__main__':
    user_repo = MysqlUserRepostory()
    sales_rep_repo = MysqlSalesRepRepository()

    registration_service = RegistrationService(user_repo, sales_rep_repo)
    registration_service.register_user("ljt", "029-12345678")
