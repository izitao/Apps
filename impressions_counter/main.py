import pandas
from datetime import datetime

import pandas as pd
from dateutil import parser

filepath_clicks_raw = "raw_data/clicks.csv"
filepath_impressions_raw = "raw_data/impressions.csv"

filepath_clicks_edited = "raw_data/clicks_filter.csv"
filepath_impressions_edited = "data/impressions_filter.csv"

impressions_data_raw = pandas.read_csv(filepath_impressions_raw)
clicks_data_raw = pandas.read_csv(filepath_clicks_raw)

#print(impressions_data)
#impressions_dict = impressions_data_raw.to_dict()
#print(impressions_data["adId"])
'''for row in impressions_dict:
    print(row)'''
#print(impressions_dict)

#pracovni databaze
impressions_data_edit = pandas.read_csv(filepath_impressions_raw)
clicks_data_edit = pandas.read_csv(filepath_clicks_raw)


###impressions_data_raw = (impressions_data_raw.sort_values(by=["adId", "visitorHash"]))
#print(impressions_data_raw)


#for row in impressions_data_raw["impressionTime"]:
    #print(row)

'''for rows in impressions_data_raw:
    #if impressions_data_raw["adId"] == 1:
    print(impressions_data_raw["adId"])
    #print(rows)
'''

#Make a list of adIds → vytvoreni samostatnych tabulek ze zdroje impressions (rozdeleno podle adID)
adIds = []
for adId in impressions_data_raw["adId"]: #vyber dat poole klice adId
    if adId not in adIds:               #pridani neopakujicich se adId
        adIds.append(adId)
    #Sort increasingly by number
for adId in range(len(adIds) - 1): #algoritmus pro vzestupne vytrideni
    if adIds[adId - 1] < adIds[adId]:
        temp = adIds[adId + 1]
        adIds[adId + 1] = adIds[adId]
        adIds[adId] = temp

#Deleting duplicate rows based on condition < 10 MINs
    #vytvoreni samostatnych tabulek dle adID
impressions_data = []
for adId in adIds:
    #print(impressions_data_raw.loc[lambda df: df['adId'] == adId, :])
    impressions_data.append(impressions_data_raw.loc[lambda df: df['adId'] == adId, :]) #pridani podtabulky ktere maji spolecne adId
    #impressions_data_raw.loc[lambda df: df['adId'] == adId, :].drop_duplicates(subset=["visitorHash","impressionTime"], keep="first")

    #serazeni kazde tabulky dle visitorHASH
for table in impressions_data:
    visitorHashes = []
    for vh in table["visitorHash"]: #ziskani seznamu jednotlivych visitorashu v dane tabulce
        #print(table[table.visitorHash == vh])
        if vh not in visitorHashes:
            visitorHashes.append(vh)
    for vh in visitorHashes: #tabulka s konkretnim visitorhashem v dane tabulce
        timestamp_dict = {}
        k = 0
        # naskladani hodnot do slovniku
        for index, row in table[table.visitorHash == vh].iterrows(): #vsechny navstevy daneho uzivatele #timestamp_dict = {poradi prvku ve slovniku: (index_v_tabulce, time_stamp)}
            #print(type(datetime.fromisoformat(row["impressionTime"])))
            #timestamp_dict[index] = datetime.fromisoformat(row["impressionTime"]) #prevedni ze stringu na datetime
            timestamp_dict[k] = (index, datetime.fromisoformat(row["impressionTime"]))  #prevedni ze stringu na datetime
            k += 1

        #print(timpestamp_dict)
        values_list = timestamp_dict.keys() #vytvoreni seznamu s klicema slovniku timestamp → slouzici pro dalsi praci
        #print(timestamp_dict[0][1])
        min_delta = 10*60

        for value in range(len(values_list)-1):
            #print(timestamp_dict[value+1][1] - timestamp_dict[value][1])
            delta = (timestamp_dict[value+1][1] - timestamp_dict[value][1]) #volba casoveho udaje daneho radku v tabulce a vypocet rozdilu casu navstevy
            delta = delta.total_seconds() #prevod na sekundy
            if delta <= min_delta: #hlavni podminky
                print(index)
                impressionId_delete = (impressions_data_raw[impressions_data_raw.impressionId == index]["impressionId"].values[0]) #vyheldani impressionID z vychozich dat prevedeni na int → vstup pro identifikaci pro vymazani z tabulky clicks
                impressions_data_edit.drop(index, axis=0, inplace=True) #vymazani duplicitniho radku v pracovni tabulce impressions
                #clicks_data_edit.drop(columns=impressionId_delete)
                click_index_delete = (clicks_data_edit[clicks_data_edit.impressionId == impressionId_delete].index.values) #ziskani indexu radku pro tabulku clicks ktery se vyhodnotli jako duplicitni v tabulce impressions
                print(click_index_delete)
                clicks_data_edit.drop(click_index_delete, axis=0, inplace=True) #vymazani duplicitniho radku v pracovni tabulce clicks
                #print(table)




print(clicks_data_raw)
    #print(visitorHashes)
print(impressions_data_edit)
print(clicks_data_raw)
print(clicks_data_edit)

#EXPORRT DO SOUBORU BEZ INDEXOVANI RADKU
impressions_data_edit.to_csv(filepath_impressions_edited, index=False)
clicks_data_edit.to_csv(filepath_clicks_edited, index=False)




