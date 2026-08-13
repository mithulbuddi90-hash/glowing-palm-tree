from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def connect(self):
        pass

class SmartLight(SmartDevice):
    def connect(self):
       return f"{self.name} is turned ON."
class SmartThermostat(SmartDevice):
    def connect(self):
       return f"{self.name} is set to 16°C."

devices = [SmartLight("Living Room Light"), SmartThermostat("Hallway")]
for device in devices:
    print(device.connect())