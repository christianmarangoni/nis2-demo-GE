# Documenti Interni Simulati di Lepida (Base di Conoscenza)

Questa cartella contiene i documenti aziendali interni e riservati simulati (scritti in formato Markdown) che servono per completare la base di conoscenza della demo. Essi coprono le aree critiche e non pubbliche della sicurezza aziendale richieste dalla conformità NIS2.

---

## Elenco dei File e Mappatura degli Agenti

### 1. `Piano_Incident_Response_Lepida_SIMULATO.md`
*   **Descrizione:** Definisce le procedure interne di monitoraggio (SOC), il workflow di triage/escalation (P1/P2/P3/P4) e le tempistiche obbligatorie per le notifiche al CSIRT Italia (pre-notifica entro 24h, notifica completa entro 72h e relazione finale entro 30 giorni) e la gestione dei Data Breach (ex Art. 33 GDPR).
*   **Agente RAG Associato:** 
    *   `specialist_incident` (Gestione Incidenti).

### 2. `Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.md`
*   **Descrizione:** Descrive la strategia di backup geografico "3-2-1-1" di Lepida, l'uso di backup immutabili (tecnologia WORM per 30 giorni) per prevenire l'azione di ransomware, le soglie RTO/RPO per i servizi essenziali, e i piani di Disaster Recovery con switch-over sui Data Center secondari (Bologna -> Parma).
*   **Agente RAG Associato:** 
    *   `specialist_continuity` (Continuità Operativa).

### 3. `Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.md`
*   **Descrizione:** Specifica la procedura per valutare i rischi legati alla catena di fornitura (Supply Chain). Include i requisiti di certificazione (ISO 27001, ISO 27017, ISO 27018), il questionario di autovalutazione del fornitore (Vendor Security Assessment) e le clausole contrattuali standard (Diritto di Audit, penali per incidenti).
*   **Agente RAG Associato:** 
    *   `specialist_supply_chain` (Supply Chain).

### 4. `Policy_Gestione_Vulnerabilita_e_SDLC_Lepida_SIMULATO.md`
*   **Descrizione:** Delinea le regole per la gestione delle vulnerabilità dell'infrastruttura (scansioni periodiche e tempistiche di patching in base al punteggio CVSS) e il ciclo di sviluppo sicuro del software (Secure SDLC basato su OWASP Top 10 e strumenti SAST/DAST). Include anche il programma di divulgazione coordinata delle vulnerabilità (VDP/CVD) tramite il canale `security.txt`.
*   **Agente RAG Associato:** 
    *   `specialist_system_vuln` (Sicurezza Sistemi e Vulnerabilità).

### 5. `Metodologia_Analisi_Rischi_e_Audit_Lepida_SIMULATO.md`
*   **Descrizione:** Documenta il framework metodologico per l'identificazione e la valutazione dei rischi di sicurezza (basato su ISO 27005 e formula $R = P \times I$) e la classificazione per gravità. Inoltre, stabilisce la struttura degli audit (self-assessment trimestrali, audit interni annuali e penetration test condotti da terze parti indipendenti).
*   **Agente RAG Associato:** 
    *   `specialist_risk_audit` (Analisi Rischi e Audit).
