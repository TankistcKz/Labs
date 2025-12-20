class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make} \nМодель: {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f'{super().get_info()} \nТип топлива: {self.fuel_type}'
    

tank1 = Vehicle('Daimler-Benz', 'Gepanzerte Selbstfahrlafette für Sturmgeschütz III mit 7,5-cm-Sturmkanone 37 oder 40')
tank2 = Car('Porsche', '8,8 cm StuK 43 Sfl L/71 Panzerjäger Tiger (P)', 'Бензин')
print(tank1.get_info())
print(tank2.get_info())