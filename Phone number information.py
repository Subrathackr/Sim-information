import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import time

print("======== mobile_number_iformation ========")
phonenumber = input("\n\tEnter Your Phone Number: ")
print("\n\tWait Searching Details..........")
time.sleep(3)

number = phonenumbers.parse(phonenumber)

print("\n\tCountry Name: ",geocoder.description_for_number(number,'en'))

print("\n\tSim Name: ",carrier.name_for_number(number,'en'))
print("\n\tThanks this tool used")