country_capitals = {
    "USA" : "Washington, D.C.",
    "France" : "Paris",
    "Germany" : "Berlin",
    "Japan" : "Tokyo",
    "UK" : "London"

}
country=input("Enter a country name (USA, France, Germany, Japan, UK): ")

if country in country_capitals:
    print("The capital of", country, "is", country_capitals[country])
else:
    print("Capital not found for the entered country.")