class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):                 # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):          # setter with validation
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):              # computed, read-only
        return self._celsius * 9 / 5 + 32

t = Temperature(20)
t.celsius = 25         # runs the setter
print(t.fahrenheit)    # 77.0
