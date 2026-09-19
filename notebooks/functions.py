import pandas as pd

#pulizia dei dati di qualità dell'aria
def pulizia_dati(dati):
    
    dati = dati.rename(columns={'idSensore': 'idsensore'})
    dati["Data"] = pd.to_datetime(dati["Data"], format="mixed", dayfirst=True)
    dati = dati.dropna(subset=["Stato"])
    dati['Valore'] = (dati['Valore'].str.replace(',', '.', regex=False).astype(float))
    dati_columns = ["idsensore", "Data", "Valore"]
    dati = dati[dati_columns]

    return dati

#pulizia dei dati delle stazioni
def pulizia_stazioni(stazioni):
    stazioni["idsensore"] = stazioni["idsensore"].astype(int)
    stazioni["idstazione"] = stazioni["idstazione"].astype(int)
    stazioni = stazioni.rename(columns={'nometipose': 'inquinante'})
    stazioni = stazioni.to_crs("EPSG:7791")

    return stazioni