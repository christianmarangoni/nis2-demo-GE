# Agente Root (Supervisore NIS2)

## Ruolo e Ambito Funzionale
Orchestratore principale. Analizza l'intento dell'utente e reindirizza la conversazione all'agente specialista competente.

---

## File Contenuti nella Cartella
*   **`agent_config.md`**: Contiene la configurazione dell'agente per l'interfaccia di Vertex AI (Descrizione, Modello suggerito e Istruzioni di Sistema).
*   **`normativa_estratto.md`**: L'estratto normativo del D.Lgs. 138/2024 (NIS2 Italia) pertinente a questo specifico dominio, utilizzato per caricare la base di conoscenza della legge.

---

## Documentazione da Inserire nel Data Store (Grounding RAG)
Per eseguire i test di conformità per questa area, è necessario caricare nel relativo Data Store di Vertex AI i seguenti documenti aziendali (presenti nella root del repository):

Nessun documento richiesto. Questo agente non utilizza un Data Store per rispondere direttamente, ma contiene esclusivamente le regole e gli intenti di routing.
