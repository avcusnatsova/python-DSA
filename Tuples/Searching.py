t = (
    "John Doe",       # Name
    21,               # Age
    "Computer Science",  # Major
    "Senior",         # Year
    3.8,              # GPA
    "Basketball",     # Hobby
    "USA"             # Country
)
#using in operator
print(21 in t)

#index 

print(t.index(3.8))

#using linear search

def search(stuple, element):
    for i in range(0, len(stuple)):
        if stuple[i] == element:
            return 'the {element} is found at {i}'
    return 'the element is not found'
print(search(t, 5))