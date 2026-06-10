# Specialista Gestione Incidenti

## Ruolo e Ambito Funzionale
Analizza le procedure di rilevamento, contenimento ed escalation degli incidenti informatici e verifica la conformità rispetto ai tempi di notifica imperativi al CSIRT Italia (24h/72h/1 mese).

---

## File Contenuti nella Cartella
*   **`agent_config.md`**: Contiene la configurazione dell'agente per l'interfaccia di Vertex AI (Descrizione, Modello suggerito e Istruzioni di Sistema).
*   **`normativa_estratto.md`**: L'estratto normativo del D.Lgs. 138/2024 (NIS2 Italia) pertinente a questo specifico dominio, utilizzato per caricare la base di conoscenza della legge.

---

## Documentazione da Inserire nel Data Store (Grounding RAG)
Per eseguire i test di conformità per questa area, è necessario caricare nel relativo Data Store di Vertex AI i seguenti documenti aziendali (presenti nella root del repository):

- `documenti_reali/carta_dei_servizi.pdf` (SLA e canali di assistenza utenti)
- `documenti_simulati/Piano_Incident_Response_Lepida_SIMULATO.md` (Piano operativo interno e workflow di notifica CSIRT)
