from seedwork.domain.entities import Entity


class User(Entity):
    def __init__(self, name: str, phone: str, rep_id: str):
        self.name = name
        self.phone = phone
        self.rep_id = rep_id


class SalesRep(Entity):
    def __init__(self, rep_id: str, name: str, phone: str, area_code: str, operator_code: str):
        self.rep_id = rep_id
        self.name = name
        self.phone = phone
        self.area_code = area_code
        self.operator_code = operator_code
