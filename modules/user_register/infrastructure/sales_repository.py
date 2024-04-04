from modules.user_register.domain.entities import SalesRep
from modules.user_register.domain.repositories import SalesRepRepository


class SalesRepModel:
    pass

class SalesRepDataMapper:
    def model_to_entity(self, model: SalesRepModel):
        return SalesRep(
            "0123",
            "John Doe",
            "12345678901",
            "029",
            "046-01"
        )

    def entity_to_model(self, entity: SalesRep):
        pass

class MysqlSalesRepRepository(SalesRepRepository):
    def __init__(self):
        self.data_mapper = SalesRepDataMapper()

    def find(self, area_code: str, operator_code: str):
        print(f'Finding sales rep for area code {area_code} and operator code {operator_code}')
        return self.data_mapper.model_to_entity(SalesRepModel())
