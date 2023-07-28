from abc import ABC

from Battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        
        self.current_mileage = current_date

    def needs_service(self):
        pass

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 30000
