import phonenumbers 
from phonenumbers import carrier, timezone, geocoder 

# Parsing phone numbers Make sure all include country codes, otherwise my script will not work.
#thanks for a random facebook video for this script/idea
phone_number1 = phonenumbers.parse("+31615627165")  # Netherlands 🇳🇱


def print_phone_details(phone_number, label):
    print(f"\n{label} Details\n")
    print("Location:", geocoder.description_for_number(phone_number, "en"))
    print("Time Zone:", timezone.time_zones_for_number(phone_number))
    print("Carrier:", carrier.name_for_number(phone_number, "en"))
    print("Valid Number:", phonenumbers.is_valid_number(phone_number))
    print("Possible Number:", phonenumbers.is_possible_number(phone_number))

    print("\nFormatted Numbers:")
    print("E164 Format:", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164))
    print("International Format:", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
    print("National Format:", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))

# Print details for each phone number that you have added to it! only basic information.
print_phone_details(phone_number1, "Phone Number 1")
