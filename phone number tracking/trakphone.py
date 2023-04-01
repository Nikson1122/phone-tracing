import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter Your NO. (e.g. +9779812345678):")
phone = phonenumbers.parse(number, None)  # None specifies that no default region is provided
if not phonenumbers.is_valid_number(phone):
    print("Invalid phone number!")
else:
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")
    print(phone)
    print(time)
    print(car)
    print(reg)
