from fuzzywuzzy import fuzz
from fuzzywuzzy import process
s1= "I love fuzzysforfuzzys"
s2= "I am loving fuzzysforfuzzys"
print("Fuzzy ratio: ", fuzz.ratio(s1,s2))
print("Fuzzy partial ratio: ",fuzz.partial_ratio(s1,s2))
print("Fuzzy token sort ratio: ",fuzz.token_sort_ratio(s1,s2))
print("Fuzzy token set ratio: ", fuzz.token_set_ratio(s1,s2))
print("Fuzzy Wratio: ",fuzz.WRatio(s1,s2),'\n\n')
query= 'fuzzys for fuzzys'
choices= ['fuzzy for fuzzy', 'fuzzy fuzzy', 'g.for fuzzys']
print("List of ratios: ")
print(process.extract(query,choices))
print("Best among the above list: ",process.extractOne(query,choices))