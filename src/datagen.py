from faker import Faker

fake = Faker()

def generate_data():
    data = {}
    data["name"] = fake.name()
    data["description"] = fake.text()
    return data

print(generate_data())