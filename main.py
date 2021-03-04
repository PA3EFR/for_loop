from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'

""" Your code here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()
# print(len(countries))     ; ontdek aantal landen (249)

print("opdracht 1")
current_length = 250
for country in countries:
    check_length = len(country)
    if check_length <= current_length:
        current_length = check_length
print(f"smallest country names consist of {current_length} characters")
list = ("The list ")
for country in countries:
    if len(country) == current_length:
        list = str(list) + ", " + str(country)
print(list)
print()

print("opdracht 2")
print("countries with most amount of vowels")
country_list = ["", 0]
vowelcount = 0
vowel1, vowel2, vowel3 = (0, 0, 0)
vowelcount_old = 0
country1, country2, country3 = ("", "", "")
for country in countries:
    character_length = len(country)
    vowelcount = 0
    for character_length in country:
        character = character_length.lower()
        if character == "a":
            vowelcount += 1
        elif character == "i":
            vowelcount += 1
        elif character == "e":
            vowelcount += 1
        elif character == "o":
            vowelcount += 1
        elif character == "u":
            vowelcount += 1
    #    print (country, vowelcount)
    if vowelcount >= vowelcount_old:
        country3 = country2
        vowel3 = vowel2
        country2 = country1
        vowel2 = vowel1
        country1 = country
        vowel1 = vowelcount
        vowelcount_old = vowelcount
print(country1, "\t", vowel1)
print(country2, "\t", vowel2)
print(country3, "\t", vowel3)

print()
print("opdracht 3")


def opsplitsing(countries):
    composed_alfabet = ""
    country_contributes = ""
    alfabeth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for country in countries:
        flag_country_contributes = False
        character_length = len(country)
        for character_length in country:
            character = character_length.lower()
            #            print(character)
            x = 0
            for x in range(26):
                if character in alfabeth:                                   # om leestekens te vermijden
                    if character not in composed_alfabet:
                        composed_alfabet = composed_alfabet + character
                        flag_country_contributes = True
        if flag_country_contributes == True:
            country_contributes = country_contributes + ", " + country
    print(f"countries contributing: {country_contributes}")
    print(f"composed alfabet: {sorted(composed_alfabet)}")


number_of_countries = len(countries)
print("number of countries:", number_of_countries)
opsplitsing(countries)
