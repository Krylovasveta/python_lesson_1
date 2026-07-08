from smartphone import Smartphone

catalog = [
    Smartphone("Apple","iPhone16","+78904562312"),
    Smartphone("Apple","iPhone15","+78904562333"),
    Smartphone("Apple","iPhone13","+78904562222"),
    Smartphone("Xiaomi","Redmi Note 13 Pro","+78904561111"),
    Smartphone("Samsung","Samsung Galsxy S21","+78904562555")
    ]

for b in catalog:
    print(f"{b.brand} - {b.model}. {b.number}")