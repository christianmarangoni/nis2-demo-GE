# Documenti Obsoleti e Non Conformi (Scenari di Demo)

Questa cartella raccoglie i documenti aziendali simulati come vecchi o obsoleti (non conformi ai requisiti della direttiva NIS2). 

Vengono utilizzati nella demo per illustrare la capacità del sistema RAG di:
1.  **Analizzare documenti esistenti** alla ricerca di mancanze rispetto alla legge (Gap Analysis).
2.  **Scrivere e generare nuovi documenti correttivi** in formato Markdown che risolvano le non-conformità rilevate.

---

## Elenco dei Documenti

### 1. `Piano_Incident_Response_OBSOLETO.md`
*   **Perché non è conforme:**
    *   Prevede tempistiche di notifica inadeguate (48 ore lavorative dopo la risoluzione).
    *   Non menziona il CSIRT Italia o l'ACN (prevede solo la Polizia Postale).
    *   Manca della pre-notifica obbligatoria entro 24 ore e della relazione finale entro 1 mese.
*   **Agente Associato:** `specialist_incident` (Gestione Incidenti).

### 2. `Procedura_Qualifica_Fornitori_OBSOLETA.md`
*   **Perché non è conforme:**
    *   Non richiede certificazioni di sicurezza cloud specifiche (ISO 27017/27018) ma solo la generica ISO 9001 per la qualità.
    *   Manca di clausole contrattuali per il Diritto di Audit.
    *   Non impone al fornitore l'obbligo di notifica tempestiva degli incidenti a Lepida.
*   **Agente Associato:** `specialist_supply_chain` (Supply Chain).
