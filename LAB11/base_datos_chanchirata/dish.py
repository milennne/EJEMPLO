class Dish:
    def __init__(self, code, name, price, region):
        self.code = code
        self.name = name
        self.price = price
        self.region = region

    def __str__(self):
        return f"{self.code} - {self.name} ({self.region}) - S/ {self.price}"
    
        