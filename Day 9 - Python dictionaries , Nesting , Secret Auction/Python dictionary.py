programming_dictionary = {
    "code": "A piece of instruction for computer",
    "404": "A type of error"
}
print(programming_dictionary["code"])

programming_dictionary["loop"] = "Piece of code execute over and over under the condition"

programming_dictionary = {} #it clear the dictionary
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

tour = { "pakistan" :{ "visited_cities" : ["karachi", "lahore" , "kashmir"], "noOfVisits" : 12} }
print(tour)
#nesting dictionary in list
country_log = [
{
    "country" : "pakistan",
    "visited_cities" : ["karachi", "lahore" , "kashmir"],
    "noOfVisits" : 12
},
{
    "country" : "italy",
    "visited_cities" : ["a", "g" , "d"],
    "noOfVisits" : 4
}]
print(country_log)
