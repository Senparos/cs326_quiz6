#author: Jay Sanders
#class: CS 325
#due: 2024-03-01


class Catalog_System:
    def __init__(self, catalog):
        self.catalog = catalog
    def load_catalog(self, catalog):
        self.catalog = catalog
class Catalog_Update(Catalog_System):
    def update_catalog(self, book, add):
        if add == True:
            self.catalog.append(book)
        else:
            self.catalog.remove(book)
class Catalog_Search(Catalog_System):
    def search(self, book):
        return book in self.catalog
class Checkout_System(Catalog_System):
    def checkout(self, book, status):
        if status == "return":
            self.catalog.append(book)
        if status == "checkout":
            self.catalog.remove(book)
class Librarian(Catalog_Update, Catalog_Search, Checkout_System):
    def __init__(self, name, catalog):
        self.name = name
        self.catalog = catalog
class Guest(Catalog_Search, Checkout_System):
    def __init__(self, name, catalog):
        self.name = name
        self.catalog = catalog
        
def main():
    default_catalog = ["the catcher in the rye", "1984", "The Fellowship of the Ring"]
    guest1 = Guest("Mary", default_catalog)
    lib1 = Librarian("Jane", default_catalog)
    guest1.checkout("The Fellowship of the Ring", "checkout")
    lib1.update_catalog("The Two Towers", True)

if __name__ == "__main__":
    main()