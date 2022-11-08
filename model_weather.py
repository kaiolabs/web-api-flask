class Weather:
    # construtor da classe
    def __init__(self, temperature, humidity, dewpoint, pressure, speed, direction, datetime): 
        self.temperature = temperature
        self.humidity = humidity
        self.dewpoint = dewpoint
        self.pressure = pressure
        self.speed = speed
        self.direction = direction
        self.datetime = datetime
        
    # método que retorna o objeto em formato string
    def __str__(self):
        return "Temperatura: {}ºC, Humidade: {}%, Ponto de Orvalho: {}ºC, Pressão: {}hPa, Velocidade do Vento: {}km/h, Direção do Vento: {}º, Data: {}".format(self.temperature, self.humidity, self.dewpoint, self.pressure, self.speed, self.direction, self.datetime)
