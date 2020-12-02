# a variable is used to store data
# every datum has a type
# give your variables appropriate labels or names, identifiers

# rules for naming identifiers
# A variable name must start with a letter or the underscore character.
# A variable name cannot start with a number.
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# syntax for defining a variable
# identifier = initial_value
# = - assignment operator, it assigns the value on the right hand side to the identifier on the lhs

# store information(name, president, continent, gdp, population, regions_or_states) about a country

name_of_country = "Ghana"
population_of_ghana = 30_000_000_000
average_temperature_of_ghana = 45.58

gh_info = {
    "name": "Republic of Ghana",
    "president": "Nana Addo Danquah Akuffo-Addo",
    "continent": "Africa",
    "gdp": 65.5,
    "population": population_of_ghana,
    "regions_or_states": ["Central", "Greater Accra", "Eastern", "Western", "Volta" "Northern", "Brong Ahafo",
                          "Upper East", "Upper West", "Ashanti"]
}

nigeria_info = {
    "country": "Nigeria",
    "president": "Muhammed Buhari",
    "continent": "Africa",
    "gdp": 397.3,
    "population": 195.9,
    "regions_or_states": ["Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River",
                          "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano",
                          "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun",
                          "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
}

african_countries_info = [gh_info, nigeria_info]

naomi_grades = {
    "french": "A",
    "python": "A"
}

bervelyn_grades = {
    "french": "A",
    "python": "A"
}

ugonna_grades = {
    "french": "C-",
    "python": "D+"
}

student_grades = [naomi_grades, bervelyn_grades, ugonna_grades]

naomi_laptop = {
    "brand": "HP",
    "model": "HP Envy 360",
    "ram": 16,
    "hdd": 1024,
    "screen size": 15.6,
}

feedback = ['i hate this course', 'what a piece of crap']
print(type(feedback))
# input output


print(values, sep='', end='')