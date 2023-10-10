from json import load

path="C:\\Users\\abhij\\Desktop\\python_work\\looping\\read_fromjson\\rest.contries\\contreis.json"

with open(path,encoding="utf-8")as f:
    countries=load(f)

# starts_withc=[c.get("name") for c in countries if c.get("name").startswith("c")]

# print(starts_withc)

# name_capital=[[c.get("name"),c.get("capital")] for c in countries]
# print(name_capital)

max_border_country=max(countries,key=lambda c:len(c.get("borders")))

print(max_border_country.get("name"))

c_with_borders=[c for c in countries if "borders" in c]
max_borders_country=max(c_with_borders,key=lambda c:len(c.get("borders")))
print(max_borders_country.get("name"))


# india_borders=[c.get("borders") for c in countries if c.get ("names")=="India"]

# print(india_borders)

india_borders=[c.get("borders") for c in countries if c.get ("names")=="afghanistan"]

india_border_names=[c.get("names") for c in countries if c. get("alpha3code") in india_borders]

print(india_border_names)

all_regions={c.get("region") for c in countries}
print(all_regions)

depended_countries=[c.get("names") for c in countries if c.get("independent")==False]

print(depended_countries)

for c in countries 
                