import unittest
from datetime import datetime

from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestNubbinBattery(unittest.TestCase):
    def test_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(last_service_date, today)
        self.assertTrue(car.needs_service())
    
    def test_battery_not_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = NubbinBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = SpindlerBattery(last_service_date, today)
        self.assertTrue(car.needs_service())
    
    def test_battery_not_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SpindlerBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

class TestCapsuletEngine(unittest.TestCase):
    def test_CapsuletEngine(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_CapsuletEngine_not_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_SternmanEngine(self):
        warn_on = True

        car = SternmanEngine(warn_on)
        self.assertTrue(car.needs_service())
    
    def test_SternmanEngine_not_serviced(self):
        warn_on = False

        car = SternmanEngine(warn_on)
        self.assertFalse(car.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_CapsuletEngine(self):
        
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_CapsuletEngine_not_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine( current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
