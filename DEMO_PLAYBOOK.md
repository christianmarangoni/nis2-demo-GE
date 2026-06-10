# Playbook della Demo Step-by-Step — Agentic RAG NIS2 (Lepida)

Questo manuale operativo descrive passo dopo passo come configurare, alimentare e presentare la demo dell'**Agentic RAG** per la conformità NIS2 di Lepida SpA utilizzando Google Cloud Vertex AI Agent Builder.

---

## Obiettivo della Demo
Mostrare come un'architettura multi-agente (*Hierarchical Routing*) possa analizzare i documenti aziendali reali e simulati di Lepida, confrontarli con i requisiti del D.Lgs. 138/2024 (NIS2 Italia) e identificare automaticamente conformità e lacune (Gap Analysis) senza allucinazioni, grazie al grounding dei Data Store dedicati.

---

## FASE 1: Preparazione dei Data Store su Vertex AI

Per ogni agente specialista, è necessario creare un **Data Store** separato in Vertex AI Agent Builder. Questo isolamento garantisce che ciascun agente risponda basandosi esclusivamente sulle fonti di sua competenza.

### Step-by-Step:
1.  Accedi alla console di **Vertex AI Agent Builder**.
2.  Vai su **Data Stores** e clicca su **Create Data Store**.
3.  Seleziona la sorgente (consigliato: **Cloud Storage** per caricare direttamente i file di questo repository, o **Google Drive**).
4.  Crea **8 Data Store distinti**, seguendo questo schema di caricamento dei documenti:

| Nome Data Store | Documento Normativo (da caricare) | Documenti Aziendali (da caricare) |
|---|---|---|
| **ds-governance** | `specialist_governance/normativa_estratto.md` | `documenti_reali/trattamento_dati.pdf` |
| **ds-incident** | `specialist_incident/normativa_estratto.md` | `documenti_reali/carta_dei_servizi.pdf`<br>`documenti_simulati/Piano_Incident_Response_Lepida_SIMULATO.md` |
| **ds-continuity** | `specialist_continuity/normativa_estratto.md` | `documenti_simulati/Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.md` |
| **ds-supply-chain** | `specialist_supply_chain/normativa_estratto.md` | `documenti_simulati/Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.md` |
| **ds-ict-security** | `specialist_ict_security/normativa_estratto.md` | `documenti_reali/soluzioni_tecnologiche.pdf`<br>`documenti_reali/manuale_operativo.pdf` |
| **ds-risk-audit** | `specialist_risk_audit/normativa_estratto.md` | `documenti_simulati/Metodologia_Analisi_Rischi_e_Audit_Lepida_SIMULATO.md` |
| **ds-system-vuln** | `specialist_system_vuln/normativa_estratto.md` | `documenti_simulati/Policy_Gestione_Vulnerabilita_e_SDLC_Lepida_SIMULATO.md` |
| **ds-personnel-asset**| `specialist_personnel_asset/normativa_estratto.md`| `documenti_reali/manuale_operativo.pdf` |

---

## FASE 2: Configurazione degli Agenti Specialisti

1.  Su Vertex AI Agent Builder, crea un nuovo **Agent** di tipo **Chat/Search** per ciascuno degli 8 specialisti.
2.  Assegna il modello **`gemini-1.5-pro`** (o superiore) per garantire capacità di ragionamento complesse e confronto critico.
3.  Copia e incolla il testo del rispettivo file `agent_config.md` (nella sezione *System Instructions*).
4.  Collega il relativo Data Store creato nella Fase 1 come **Tool** per l'agente.

---

## FASE 3: Configurazione dell'Agente Root (Supervisore)

L'Agente Root funge da orchestratore centrale ed è l'unico punto di contatto per l'utente finale.

1.  Crea un nuovo agente chiamato **Root Supervisor**.
2.  Associa il modello **`gemini-1.5-flash`** per garantire la massima velocità di risposta e instradamento.
3.  Incolla le istruzioni di sistema presenti in `root_supervisor/agent_config.md`.
4.  Crea le **regole di routing** (o collegamenti agli agenti specialisti tramite gli intenti) in modo che la richiesta dell'utente venga inoltrata al sub-agente corretto in base all'argomento rilevato.

---

## FASE 4: Esecuzione degli Scenari di Demo (Script di Presentazione)

Ecco tre scenari reali da mostrare durante la demo per evidenziare il valore del sistema Agentic RAG.

### Scenario 1: Verifica Conformità Gestione Incidenti
*   **Domanda dell'utente (al Root Agent):** 
    > *"Come gestiamo gli incidenti informatici in Lepida? Siamo allineati alle scadenze di notifica imposte dalla NIS2?"*
*   **Comportamento del Sistema:**
    1. L'agente Root rileva l'intento legato agli incidenti e indirizza la richiesta allo **Specialista Gestione Incidenti**.
    2. Lo specialista consulta il Data Store (`ds-incident`) che contiene l'estratto dell'Art. 25 NIS2 e il `Piano_Incident_Response_Lepida_SIMULATO.md`.
    3. Il modello confronta le regole NIS2 (pre-notifica 24h, notifica completa 72h) con il piano simulato.
*   **Risposta attesa del RAG:**
    > *"Sì, Lepida è conforme. Il piano di Incident Response simulato (Doc: PX-SEC-IRP-001 v3.1) prevede esplicitamente l'invio della pre-notifica (Early Warning) entro 24 ore e la notifica completa entro 72 ore al CSIRT Italia, in perfetto allineamento con l'Art. 25 del D.Lgs. 138/2024. Il piano prevede anche la relazione finale entro un mese."*

---

### Scenario 2: Valutazione Sicurezza dei Fornitori (Supply Chain)
*   **Domanda dell'utente (al Root Agent):**
    > *"Quali requisiti dobbiamo imporre ai nostri fornitori di servizi cloud per essere conformi alla NIS2?"*
*   **Comportamento del Sistema:**
    1. L'agente Root indirizza la richiesta allo **Specialista Supply Chain**.
    2. L'agente interroga `ds-supply-chain` che contiene la `Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.md`.
*   **Risposta attesa del RAG:**
    > *"In conformità all'Art. 24 c.2 lett. d) della NIS2, Lepida impone ai fornitori di servizi Cloud le certificazioni ISO/IEC 27017 e ISO/IEC 27018. Inoltre, il fornitore deve compilare un questionario di autovalutazione di 10 controlli di sicurezza e accettare clausole contrattuali vincolanti, tra cui il Diritto di Audit (Right to Audit) e l'obbligo di notificare a Lepida qualsiasi incidente di sicurezza entro 24 ore."*

---

### Scenario 3: Protezione dai Ransomware e Continuità Operativa
*   **Domanda dell'utente (al Root Agent):**
    > *"La nostra politica di backup ci protegge adeguatamente dagli attacchi ransomware secondo la NIS2?"*
*   **Comportamento del Sistema:**
    1. L'agente Root indirizza allo **Specialista Continuità Operativa**.
    2. L'agente interroga `ds-continuity` contenente il `Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.md`.
*   **Risposta attesa del RAG:**
    > *"Sì. La strategia di continuità operativa adotta la regola del backup '3-2-1-1' con replicazione offsite ed immutabilità dei dati (Immutable Backup) tramite tecnologia WORM per un periodo minimo di 30 giorni. Questa misura risponde ai requisiti dell'Art. 24 comma 2 lett. c) NIS2 e protegge efficacemente i backup da tentativi di cancellazione o cifratura da parte di ransomware."*
