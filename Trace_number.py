import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number =input("Enter the phone number with +_ _ : ")
while True:
    if len(number)> 10:
        break
    else:
        print("please Enter Valid Phone Number To Trace")
        number =input("Enter the phone number with +_ _ : ")


phone_number=phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone_number)
service_provider = carrier.name_for_number(phone_number, "en")
sim_region = geocoder.description_for_number(phone_number, "en")

print(phone_number)
print(f"Time zone : {time}")
print(f"Sim card provide : {service_provider}")
print(f"Sim region : {sim_region}")
