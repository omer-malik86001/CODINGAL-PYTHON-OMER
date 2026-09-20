currencies={
    "QATAR":"QAR",
    "USA":"US DOLLARS",
    "FRANCE":"EURO",
}
print(currencies["QATAR"])
print(currencies.get("PAKISTAN","COUNTRY NOT FOUND"))
print(currencies.get("FRANCE","COUNTRY NOT FOUND"))

country=input("enter any country to find the currency of it ! - ")
print(currencies.get(country.upper(),"country not found"))
