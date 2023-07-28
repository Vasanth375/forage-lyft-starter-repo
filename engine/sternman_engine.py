from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        
        self.warning_light_is_on = warning_light_is_on
   
    def needs_service(self):
        pass


    # def engine_should_be_serviced(self):
    #     if self.warning_light_is_on:
    #         return True
    #     else:
    #         return False
