random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]


data_float = list(filter(lambda x: isinstance(x, float), random_list))


def get_digits(n):
    ratusan = n // 100
    n %= 100
    puluhan = n // 10
    satuan = n % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_int = [get_digits(n) for n in data_int]

data_string = list(filter(lambda x: isinstance(x, str), random_list))
data_string = [s for s in data_string if s.isalpha()]

print(f"Data Float: {tuple(data_float)}")
print("Data Int:")
for d in data_int:
    print(f"\t{{'ratusan': {d['ratusan']}, 'puluhan': {d['puluhan']}, 'satuan': {d['satuan']}}}")
print(f"Data String: {data_string}")
