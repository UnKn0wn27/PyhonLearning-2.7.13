cities = {
    'Chisinau': 'CH',
    'Orhei': 'OR',
    'Soroca': 'SO'
}

raion = {
    'CH': 'Buiucani',
    'CH': 'Botanica',
    'CH': 'Riscani',
    'OR': 'Butuceni'
}

raion['SO'] = 'Bulboci'

print '=' * 27
print "Chisinau has:", raion[cities['Chisinau']]
print "Orhei has:", raion[cities['Orhei']]
print "Soroca has:", raion[cities['Soroca']]

print '=' * 27

for abbrev, rai in raion.items():
    print "%s are raionului %s" % (
        abbrev, rai)

print '=' * 27

for city, abbrev in cities.items():
    print "%s abreviarea %s are raionul %s" % (
        city, abbrev, raion[abbrev])

print '=' * 27

city = cities.get('Dubasare')

if not city:
    print "Gomenasai! No Dubasare!"

rai = raion.get("DU",'NU Exista!')
print "Raionul pentru orasul 'DU': %s" % rai

# del cities['Orhei'] // sterge orheiul
# cities.clear() // sterge toate datele din dictionar

print "str() produces a printable string representaion of a dictionary %s" % str(raion)
 
