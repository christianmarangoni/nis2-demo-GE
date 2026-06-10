# Documenti Reali di Lepida (Base di Conoscenza)

Questa cartella raccoglie i documenti pubblici e ufficiali di Lepida SpA scaricati direttamente dal portale del servizio LepidaID e usati per alimentare la base di conoscenza (Data Store) del prototipo RAG.

---

## Elenco dei File e Mappatura degli Agenti

### 1. `manuale_operativo.pdf`
*   **Descrizione:** Il Manuale Operativo ufficiale per l'erogazione del servizio SPID (LepidaID). Descrive l'architettura logica, i flussi di autenticazione, la gestione delle credenziali degli utenti e le regole di sicurezza fisica e organizzativa degli uffici di registrazione.
*   **Agenti RAG Associati:** 
    *   `specialist_personnel_asset` (per la parte di sicurezza fisica e organizzativa dei RA).
    *   `specialist_ict_security` (per la parte tecnica di gestione delle credenziali ed autenticazione).

### 2. `carta_dei_servizi.pdf`
*   **Descrizione:** La Carta dei Servizi del Gestore di Identità Digitale LepidaID. Formalizza gli standard di qualità, i tempi massimi di attivazione e ripristino dei servizi, e le procedure di contatto per assistenza e disservizi.
*   **Agenti RAG Associati:** 
    *   `specialist_incident` (per comprendere i canali di ricezione delle segnalazioni e le SLA promesse all'utenza).

### 3. `manuale_utente.pdf`
*   **Descrizione:** Guida utente ufficiale per l'attivazione e l'uso dell'identità digitale LepidaID nei vari livelli di sicurezza SPID.
*   **Agenti RAG Associati:** 
    *   `specialist_personnel_asset` / `specialist_ict_security` (documentazione di supporto all'addestramento e all'igiene informatica).

### 4. `soluzioni_tecnologiche.pdf`
*   **Descrizione:** Allegato tecnico che specifica l'architettura infrastrutturale ed i sistemi di protezione della connettività e dei data center utilizzati da Lepida.
*   **Agenti RAG Associati:** 
    *   `specialist_ict_security` (per la conformità sui requisiti tecnologici di crittografia, cifratura e MFA).

### 5. `trattamento_dati.pdf`
*   **Descrizione:** Informativa sul trattamento dei dati personali (ex Art. 13-14 del GDPR) adottata da Lepida per l'erogazione del servizio LepidaID.
*   **Agenti RAG Associati:** 
    *   `specialist_governance` (per il controllo della compliance legale sui flussi di dati e responsabilità dell'ente).
