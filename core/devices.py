class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.connected_to = None

    def can_ping(self, target):
        """Проверка возможности ping"""
        return (self.connected_to and 
                target.connected_to and 
                self.ip.split('.')[:3] == target.ip.split('.')[:3])  # Проверяем подсеть

class Router(Device):
    def __init__(self, ip):
        super().__init__("ROUTER", ip)
        self.dns = "8.8.8.8"

class Computer(Device):
    def __init__(self, name, ip):
        super().__init__(name, ip)
        self.has_internet = False
