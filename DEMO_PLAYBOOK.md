# Playbook della Demo Step-by-Step — Agentic RAG NIS2 (Lepida)

Questo manuale descrive passo dopo passo come configurare ed eseguire la demo dell'**Agentic RAG** per la conformità NIS2 di Lepida SpA utilizzando Google Cloud Vertex AI Agent Builder.

La demo è strutturata per mostrare due tipi di flussi di lavoro:
1.  **Flussi di Sola Verifica (Compliance Check)**: L'utente interroga l'agente per verificare se i documenti e le misure attuali sono già conformi ai requisiti della NIS2. L'agente risponde confermando la conformità e mappando i controlli effettuati sugli articoli della legge.
2.  **Flussi di Rilevamento e Correzione (Gap & Fix)**: L'utente fornisce all'agente un documento aziendale obsoleto (non conforme). L'agente individua le mancanze e genera autonomamente un nuovo documento sostitutivo o integrativo conforme in formato Markdown.

---

## FASE 1: Preparazione dei Data Store su Vertex AI

Crea i **Data Store** separati su Vertex AI Agent Builder, caricando sia i documenti normativi che quelli aziendali (reali, simulati conformi e non conformi):

| Nome Data Store | Documento Normativo (da GCS - `.txt`) | Documenti Aziendali (da GCS / Drive) |
|---|---|---|
| **ds-governance** | `gcs_upload/specialist_governance/normativa_estratto.txt` | *Drive:* `documenti_reali/trattamento_dati.pdf` |
| **ds-incident** | `gcs_upload/specialist_incident/normativa_estratto.txt` | *Drive:* `documenti_reali/carta_dei_servizi.pdf`<br>*GCS:* `gcs_upload/documenti_simulati/Piano_Incident_Response_Lepida_SIMULATO.txt`<br>*GCS:* `gcs_upload/documenti_non_conformi/Piano_Incident_Response_OBSOLETO.txt` |
| **ds-continuity** | `gcs_upload/specialist_continuity/normativa_estratto.txt` | *GCS:* `gcs_upload/documenti_simulati/Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.txt` |
| **ds-supply-chain**| `gcs_upload/specialist_supply_chain/normativa_estratto.txt`| *GCS:* `gcs_upload/documenti_simulati/Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.txt`<br>*GCS:* `gcs_upload/documenti_non_conformi/Procedura_Qualifica_Fornitori_OBSOLETA.txt` |
| **ds-ict-security**| `gcs_upload/specialist_ict_security/normativa_estratto.txt`| *Drive:* `documenti_reali/soluzioni_tecnologiche.pdf`<br>*Drive:* `documenti_reali/manuale_operativo.pdf` |
| **ds-risk-audit** | `gcs_upload/specialist_risk_audit/normativa_estratto.txt` | *GCS:* `gcs_upload/documenti_simulati/Metodologia_Analisi_Rischi_e_Audit_Lepida_SIMULATO.txt` |
| **ds-system-vuln** | `gcs_upload/specialist_system_vuln/normativa_estratto.txt` | *GCS:* `gcs_upload/documenti_simulati/Policy_Gestione_Vulnerabilita_e_SDLC_Lepida_SIMULATO.txt` |
| **ds-personnel-asset**|`gcs_upload/specialist_personnel_asset/normativa_estratto.txt`| *Drive:* `documenti_reali/manuale_operativo.pdf` |

---

## FASE 2: Esecuzione degli Scenari di Sola Verifica (Compliance Check)

In questi scenari, l'agente esamina i documenti aziendali conformi e certifica che non vi sono violazioni o lacune.

### SCENARIO 1: Verifica Continuità Operativa e Backup Anti-Ransomware
*   **Obiettivo:** Verificare se il piano di DR e Backup simulato soddisfa i requisiti dell'Art. 24 comma 2 lettera c).
*   **Prompt da digitare in chat (all'agente Root o allo Specialista Continuità):**
    > *"Analizza il documento `Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.txt` e verifica se la nostra politica di backup e disaster recovery è conforme all'Art. 24 comma 2 lettera c) della NIS2. Ci sono lacune?"*
*   **Comportamento dell'Agente:**
    1. L'agente Root indirizza la richiesta allo **Specialista Continuità Operativa**.
    2. L'agente interroga `ds-continuity` e confronta le misure reali (strategia 3-2-1-1, backup WORM immutabili a 30 giorni, RTO/RPO per LepidaID) con la normativa.
*   **Risposta attesa (Sola Verifica):**
    > *"**Stato: VERIFICATO (CONFORME)**. Il documento `Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.txt` soddisfa pienamente i requisiti dell'Art. 24 c. 2 lett. c) del D.Lgs. 138/2024. Le misure di mitigazione ransomware (backup immutabile WORM) e gli obiettivi di ripristino per i servizi critici (RTO < 2 ore per LepidaID) sono adeguati allo stato dell'arte. Non sono state rilevate lacune o non-conformità."*

---

### SCENARIO 2: Verifica Sicurezza Fisica e Controllo Accessi degli Uffici
*   **Obiettivo:** Verificare se il manuale operativo reale di LepidaID risponde ai requisiti di sicurezza fisica e personale dell'Art. 24 comma 2 lettera i).
*   **Prompt da digitare in chat (all'agente Root o allo Specialista Personnel & Asset):**
    > *"Esegui una verifica di conformità sul manuale `manuale_operativo.pdf` rispetto all'Art. 24 comma 2 lettera i) della NIS2. I nostri uffici di registrazione e le procedure sul personale sono conformi?"*
*   **Comportamento dell'Agente:**
    1. L'agente Root indirizza la richiesta allo **Specialista Personale, Accessi e Asset**.
    2. L'agente interroga `ds-personnel-asset` e analizza le sezioni di sicurezza fisica del manuale operativo.
*   **Risposta attesa (Sola Verifica):**
    > *"**Stato: VERIFICATO (CONFORME)**. Il manuale operativo di LepidaID (`manuale_operativo.pdf`) è conforme all'Art. 24 comma 2 lett. i). Il documento dettaglia adeguatamente i requisiti di sicurezza fisica delle sedi di registrazione (RA) e il controllo degli accessi elettronici e fisici. Le procedure di identificazione e verifica del personale addetto sono allineate ai requisiti di sicurezza e affidabilità richiesti dalla NIS2."*

---

## FASE 3: Esecuzione degli Scenari di Rilevamento e Correzione (Gap & Fix)

In questi scenari, l'agente esamina i documenti obsoleti, rileva le violazioni e genera il documento correttivo.

### SCENARIO 3: Rilevamento e Fix del Piano Incident Response Obsoleto
*   **Obiettivo:** Rilevare che il vecchio piano non rispetta le tempistiche NIS2 e generare il nuovo piano conforme.
*   **Prompt da digitare in chat (all'agente Root o allo Specialista Incidenti):**
    > *"Ho caricato sul nostro data store il documento `Piano_Incident_Response_OBSOLETO.txt`. Analizzalo rispetto alla NIS2 e scrivi un nuovo documento sostitutivo in formato Markdown che corregga tutte le mancanze e ci renda conformi."*
*   **Risposta attesa (Gap & Fix):**
    L'agente evidenzierà le mancanze (es. assenza di notifica CSIRT entro 24h/72h e presenza di tempi obsoleti di 48 ore lavorative) e fornirà il testo del nuovo piano conforme:
    ```markdown
    ### Analisi delle Non-Conformità (Gap Analysis)
    * Violazione dell'obbligo di notifica al CSIRT Italia (è presente solo la Polizia Postale).
    * Tempistiche errate (48 ore dalla risoluzione invece del pre-allarme a 24 ore dalla conoscenza).

    ---
    ### NUOVO DOCUMENTO: Piano di Gestione Incidenti NIS2 (Lepida SpA)
    ...
    ```

---

### SCENARIO 4: Rilevamento e Fix della Procedura di Qualifica Fornitori (Supply Chain)
*   **Obiettivo:** Esaminare le vecchie linee guida acquisti e generare un "Cybersecurity Annex" integrativo per imporre requisiti NIS2 ai fornitori.
*   **Prompt da digitare in chat (all'agente Root o allo Specialista Supply Chain):**
    > *"Verifica il documento `Procedura_Qualifica_Fornitori_OBSOLETA.txt` rispetto alla NIS2. Scrivi un 'Cybersecurity Annex' (Allegato di Sicurezza) in Markdown pronto da aggiungere ai contratti dei fornitori per risolvere le mancanze."*
*   **Risposta attesa (Gap & Fix):**
    L'agente rileva la mancanza di requisiti cloud (ISO 27017/27018), l'assenza del diritto di audit e l'assenza di obblighi di notifica del fornitore a Lepida, e scrive l'allegato contrattuale correttivo.

---

## FASE 4: Presentazione dell'Assessment Finale (Tabella Gap / Conformità)

Per concludere la demo, puoi chiedere al Root Agent:
> *"Genera un report finale in formato tabellare che riassuma quali documenti (conformi e non conformi) abbiamo verificato in questa sessione di demo, quali esiti di conformità sono emersi e quali azioni correttive abbiamo implementato."*

L'agente produrrà una tabella riepilogativa chiara che funge da cruscotto finale per la presentazione.
