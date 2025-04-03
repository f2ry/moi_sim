class GameState:
    def __init__(self):
        self.is_network_ready = False
        self.is_internet_ready = False
        self.current_devices = None  # Для хранения созданных устройств

game_state = GameState()