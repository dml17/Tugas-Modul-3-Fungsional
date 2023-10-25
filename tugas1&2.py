def convert_to_minutes(weeks, days, hours, minutes):
    return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes

def curried_converter(weeks):
    def curry_days(days):
        def curry_hours(hours):
            def curry_minutes(minutes):
                return convert_to_minutes(weeks, days, hours, minutes)
            return curry_minutes
        return curry_hours
    return curry_days

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output = []

for entry in data:
    parts = entry.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    
    result = curried_converter(weeks)(days)(hours)(minutes)
    output.append(result)

print(output)
print()
for entry in data:
    parts = entry.split()
    integer_values = list(filter(str.isdigit, parts))
    output.append(integer_values)

for item in output:
    print(item)
    
    