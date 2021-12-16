from faker import Faker

fake = Faker()

def generate_data():
    data = {}
    data["name"] = fake.name()
    data["description"] = fake.text()
    return data

# print(generate_data())

def generate_news_data(count = 1):
    all_data = []
    for _ in range(count):
        data = {}
        data["title"] = fake.sentence()
        data["description"] = fake.sentence()
        data["author"] = fake.name()
        data["date"] = fake.date()
        data["link"] = fake.url()
        all_data.append(data)
    return all_data

print(generate_news_data(5))
