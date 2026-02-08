# du_03.02.26_dict_country_packing_unpacking
# There is a dictionary that stores country names and their capitals.
# A country name is used as a key, a capital as a value.
# Implement the following:
# adding data,
# deleting data,
# finding data,
# editing data,
# saving a
# loading data
# (using packing and unpacking).

import pickle

class Country:

    def __init__(self):
        self.data = {
            "Slovakia": "Bratislava",
            "Austria": "Vienna",
            "Hungary": "Budapest"
        }

    def add_country(self, country, capital):
        if country in self.data:
            return "Country already exists."
        self.data[country] = capital
        return f"{country} added."

    def delete_country(self, country):
        if country in self.data:
            del self.data[country]
            return f"{country} deleted."
        return "Country not found."

    def find_country(self, country):
        if country in self.data:
            return self.data[country]
        return "Country not found."

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            return f"{country} updated."
        return "Country not found."

    def save_data(self, file):
        with open(file, "wb") as f:
            pickle.dump(self.data, f)
        return "Data saved."

    def load_data(self, file):
        with open(file, "rb") as f:
            self.data = pickle.load(f)
        return "Data loaded."

countries = Country()

print(countries.add_country("Czech Republic", "Prague"))
print(countries.delete_country("Hungary"))
print(countries.find_country("Austria"))
print(countries.save_data("countries.pkl"))
print(countries.load_data("countries.pkl"))
print(countries.data)