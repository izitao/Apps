import pandas
from datetime import datetime


#vstupni data
filepath_clicks_raw = "raw_data/clicks.csv"
filepath_impressions_raw = "raw_data/impressions.csv"

#vystupni data
filepath_clicks_edited = "data/clicks_filter.csv"
filepath_impressions_edited = "data/impressions_filter.csv"

#inicializace vstupnich dat
impressions_data_raw = pandas.read_csv(filepath_impressions_raw)
clicks_data_raw = pandas.read_csv(filepath_clicks_raw)

#pracovni databaze
impressions_data_edit = pandas.read_csv(filepath_impressions_raw)
clicks_data_edit = pandas.read_csv(filepath_clicks_raw)

#kriterium pozadovaneho casu
min_delta = 10*60

#id duplicitnich impresi
impressions_ids_to_delete = []


def separate_tables(impressions_data_raw):
    """ Rozdeli vstupni data do jednotlivych tabulek podle id reklamy(adId) """
    # promenna obsahujici vypis vsech id reklam (adID)
    adIds = []

    # vyber vstupnich dat podle klice adId (bez opakovani)
    for adId in impressions_data_raw["adId"]:
        if adId not in adIds:
            adIds.append(adId)

    # vzestupne setrideni promenne
    adIds.sort()

    # vytvoreni samostatnych tabulek se spolecnym adID
    impressions_data = []
    for adId in adIds:
        impressions_data.append(impressions_data_raw.loc[lambda df: df['adId'] == adId, :])

    return impressions_data


def order_by_visitor_hash(impressions_data):
    """ Serazeni kazde tabulky podle visitorHash """

    for table in impressions_data:
        visitor_hashes = []

        # ziskani seznamu jednotlivych visitorhashu v dane tabulce (bez opakovani)
        for vh in table["visitorHash"]:
            if vh not in visitor_hashes:
                visitor_hashes.append(vh)
        get_visitor_timestamps(visitor_hashes, table)


def get_visitor_timestamps(visitor_hashes, table):
    """ Vytvori slovnik s timestampy daneho visitora k prislusne tabulce reklamy (adId) """

    # vytvoreni slovniku ke kazdemu visitorovi | tabulka s konkretnim visitorhashem v dane tabulce
    for vh in visitor_hashes:
        timestamp_dict = {}
        k = 0

        # vlozeni vsech navstev daneho visitora konkretniho adId do slovniku timestamp_dict = {poradi prvku ve slovniku: (impressionId, time_stamp)}
        for index, row in table[table.visitorHash == vh].iterrows():
            impression_id = row["impressionId"]
            impression_time = datetime.fromisoformat(row["impressionTime"])
            timestamp_dict[k] = (impression_id, impression_time)
            k += 1

        # vytvoreni seznamu s klici slovniku timestamp → slouzici pro dalsi praci
        values_list = timestamp_dict.keys()
        get_duplicate_impression_id(values_list, timestamp_dict)


def get_duplicate_impression_id(values_list, timestamp_dict):
    """ Na zaklade casoveho kriteria vyhodnoti duplicitni navstevy daneho visitora """

    for value in range(len(values_list)-1):
        if len(values_list) <= 1:
            break
        else:
            # vypocet rozdilu casu dvou po sobe jdoucich navstev
            delta = abs((timestamp_dict[value+1][1] - timestamp_dict[value][1]))
            delta = delta.total_seconds()
            # hlavni podminky casoveho kriteria
            if delta <= min_delta:
                print(timestamp_dict[value][0])
                impression_id_delete = timestamp_dict[value][0]
                impressions_ids_to_delete.append(impression_id_delete)


def delete_duplicate_visits(impression_ids):
    """ Vymaze z dataframu duplicitni imprese """

    impression_ids.sort(reverse=True)

    for impression_id in impression_ids:
        impressions_data_edit.drop(index=impression_id-1, axis=0, inplace=True)
        # ziskani indexu radku pro tabulku clicks ktery se vyhodnotli jako duplicitni v tabulce impressions
        click_index_delete = (clicks_data_edit[clicks_data_edit.impressionId == impression_id].index.values)
        clicks_data_edit.drop(click_index_delete, axis=0, inplace=True) #vymazani duplicitniho radku v pracovni tabulce clicks"""


order_by_visitor_hash(separate_tables(impressions_data_raw))
delete_duplicate_visits(impressions_ids_to_delete)

#EXPORRT DO SOUBORU BEZ INDEXOVANI RADKU

impressions_data_edit.to_csv(filepath_impressions_edited, index=False)
clicks_data_edit.to_csv(filepath_clicks_edited, index=False)

