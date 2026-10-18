"""
#Arbeidskrav 1 - PY1010
#Sammenlikning av aarlige kostnader for elbil og bensinbil
 
#Programmet beregner og skriver ut de aarlige totalkostnadene for elbil og bensinbil, samt den aarlige kostnadsdifferansen.
 
#Forutsetninger:
- Renter paa billaan og verditap er holdt utenfor (antas like for begge biltyper).
- Aarlig kjoerelengde er satt til 10 000 km.
- Et aar regnes som 365 dager.#"""


# Inndata felles for begge biltyper
 
km_per_aar = 10000  # [km/aar]
dager_per_aar = 365  # [dager/aar]
trafikkforsikringsavgift = 8.38  # [kr/dag]
 
# Inndata elbil
 
forsikring_elbil = 5000  # [kr/aar]
stromforbruk = 0.2  # [kWh/km]
strompris = 2.00  # [kr/kWh], kun hjemmelading
bomavgift_elbil = 0.1  # [kr/km]
 
# Inndata bensinbil
 
forsikring_bensinbil = 7500  # [kr/aar]
bensinkostnad = 1.0  # [kr/km]
bomavgift_bensinbil = 0.3  # [kr/km]
 
# Beregning av kostnader for elbil
 
trafikkavgift_aar = trafikkforsikringsavgift*dager_per_aar  # [kr/aar], lik for begge
strom_aar = stromforbruk*strompris*km_per_aar  # [kr/aar]
bom_elbil_aar = bomavgift_elbil*km_per_aar  # [kr/aar]
 
# Summerer alle aarlige kostnader for elbil:
total_elbil = forsikring_elbil + trafikkavgift_aar + strom_aar + bom_elbil_aar
 
#%% Beregning av kostnader for bensinbil
 
bensin_aar = bensinkostnad*km_per_aar  # [kr/aar]
bom_bensinbil_aar = bomavgift_bensinbil*km_per_aar  # [kr/aar]
 
# Summerer alle aarlige kostnader for bensinbil:
total_bensinbil = forsikring_bensinbil + trafikkavgift_aar + bensin_aar + bom_bensinbil_aar
 
#%% Beregning av kostnadsdifferanse
 
# Positiv differanse betyr at elbil er billigst:
differanse = total_bensinbil - total_elbil  # [kr/aar]
 
#%% Utskrift
 
print('Aarlige kostnader ved', km_per_aar, 'km/aar:')
print()
print('Elbil:')
print('  Forsikring =', forsikring_elbil, 'kr')
print('  Trafikkforsikringsavgift =', trafikkavgift_aar, 'kr')
print('  Strom =', strom_aar, 'kr')
print('  Bomavgift =', bom_elbil_aar, 'kr')
print('  Totalt =', total_elbil, 'kr')
print()
print('Bensinbil:')
print('  Forsikring =', forsikring_bensinbil, 'kr')
print('  Trafikkforsikringsavgift =', trafikkavgift_aar, 'kr')
print('  Bensin =', bensin_aar, 'kr')
print('  Bomavgift =', bom_bensinbil_aar, 'kr')
print('  Totalt =', total_bensinbil, 'kr')
print()
print('Aarlig kostnadsdifferanse (bensinbil - elbil) =', differanse, 'kr')
