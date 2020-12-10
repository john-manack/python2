# NESTED DICTIONARIES
# Within the digitalcrafts dictionary, there is a
# US dictionary. Within the US dictionary, there are two
# additional dictionaries.
digitalcrafts = {
    "US" : {
        "Georgia": {
            "Atlanta": "3442 Piedmont Rd NE 420"
        },
        "Texas": {
            "Houston": "1334 Brittmore Rd 1327"
        }
    }
}

print(digitalcrafts['US'])
print(digitalcrafts['US']['Georgia'])
print(digitalcrafts['US']['Georgia']['Atlanta'])

# Add a new city and address dictionary to the 
# US dictionary
digitalcrafts['US']['South Carolina'] = {
    "Greenville": "123 Sesame Street"
}

print(digitalcrafts)