#!/usr/bin/python3

# single responsibility priciple

# items
class ItemSpec(object):
    name = ""
    type_item = ""
    color = ""

    def compare(self, ite_spec):
        return ite_spec.name == self.name & \
               ite_spec.type_item == self.type_item & \
               ite_spec.color == self.color

class Item(ItemSpec):
    id=""
    spec=""
    quantity=0
    price=1.1

# file manager
from pathlib import Path
from zipfile import ZipFile

class FileManager():
    def __init__(self, filename: str):
        self.path = Path(filename)

        def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, encoding="utf-8"):
        return self.path.write_text(encoding)

class ZipFileManager():
    def __init__(self, filename: str):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)


# orther and payment

from abc import ABC, abstractmethod

class Order():
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)



class PaymentProcess(ABC):
    def __init__(self, order: Order, security_code: str):
        pass
