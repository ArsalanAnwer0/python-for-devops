# Data structures

# list
environments = ["dev","prd","stg","test"]

print(len(environments))
environments.append("basiton")

# dictionary
device_info = {
    "name" : "Apple MacBook",
    "RAM" : "16 GB",
    "CPU" : 8
}

device_info.update({"Environment":environments})
print(device_info)


device_dict = {"keyword":"value"}
print(type(device_dict))

# tuples
days_of_week = ("Sunday","Monday")

# array