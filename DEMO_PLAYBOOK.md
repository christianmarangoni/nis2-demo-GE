# Playbook della Demo Step-by-Step — Agentic RAG NIS2 (Lepida)

Questo manuale descrive passo dopo passo come configurare ed eseguire la demo dell'**Agentic RAG** per la conformità NIS2 di Lepida SpA utilizzando Google Cloud Vertex AI Agent Builder.

A differenza di una semplice demo di domanda/risposta (Q&A), questo flusso illustra scenari interattivi in cui **l'utente fornisce all'agente un documento aziendale obsoleto (non conforme)** e **l'agente, conoscendo le regole della NIS2, scrive e genera un nuovo documento corretto (patch/sostitutivo) che risolve tutte le lacune individuate.**

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

## FASE 2: Esecuzione degli Scenari Interattivi di Demo

### SCENARIO 1: Rilevamento e Fix Automatico del Piano Incident Response Obsoleto

#### 1. Obiettivo dello Scenario
Dimostrare come l'agente rilevi che il vecchio piano incident response non rispetta le regole NIS2 e scriva autonomamente la versione corretta conforme alla legge.

#### 2. Prompt da digitare nella chat (all'agente Root o allo Specialista Incidenti):
> *"Ho caricato sul nostro data store il documento `Piano_Incident_Response_OBSOLETO.txt`. Puoi analizzarlo a fondo rispetto ai requisiti del D.Lgs. 138/2024 e scrivere un nuovo documento sostitutivo in formato Markdown che corregga tutte le mancanze e ci renda conformi alla NIS2?"*

#### 3. Comportamento dell'Agente:
*   L'agente Root indirizza la richiesta allo **Specialista Gestione Incidenti**.
*   Lo specialista confronta la sezione `normativa_estratto.txt` (Art. 25, 26) con `Piano_Incident_Response_OBSOLETO.txt`.
*   Rileva che il documento obsoleto parla di denunce alla Polizia entro 48 ore lavorative, non cita il CSIRT Italia, né i tempi di pre-notifica obbligatori (24h e 72h).
*   Genera un nuovo piano completo e strutturato in Markdown.

#### 4. Risposta attesa (Output dell'Agente):
L'agente risponderà con un'analisi critica delle lacune e genererà il documento corretto:

```markdown
### Analisi delle Non-Conformità (Gap Analysis)
Il documento `Piano_Incident_Response_OBSOLETO.txt` presenta gravi lacune rispetto all'Art. 25 del D.Lgs. 138/2024:
1. **Mancanza dei canali istituzionali:** Il piano prevede solo la denuncia alla Polizia Postale, senza menzionare il CSIRT Italia.
2. **Tempistiche violate:** Prevede notifiche entro 48 ore lavorative dalla risoluzione, mentre la NIS2 impone una pre-notifica entro 24 ore dalla conoscenza dell'incidente significativo.
3. **Mancanza della relazione finale:** Non è previsto l'invio della relazione finale entro 1 mese.

---

### NUOVO DOCUMENTO PROPOSTO: Piano di Gestione Incidenti Conformità NIS2 (Lepida SpA)

**Codice Documento:** LPD-SEC-IRP-2026-NIS2  
**Stato:** Approvato (Grounding NIS2)

#### 1. Processo di Escalation e Triage
Ogni anomalia rilevata deve essere classificata entro 15 minuti dal Security Operations Center (SOC).

#### 2. Obblighi di Notifica al CSIRT Italia (Art. 25 D.Lgs. 138/2024)
In caso di incidenti con impatto significativo, Lepida SpA effettuerà le seguenti comunicazioni tramite PEC o Portale ACN:
*   **Pre-notifica (Early Warning):** Entro 24 ore dalla conoscenza dell'evento.
*   **Notifica dell'incidente:** Entro 72 ore dalla conoscenza dell'evento.
*   **Relazione Finale:** Entro 1 mese dalla risoluzione, contenente la Root Cause Analysis.
...
```

---

### SCENARIO 2: Rilevamento e Fix della Procedura di Qualifica Fornitori (Supply Chain)

#### 1. Obiettivo dello Scenario
Dimostrare come l'agente esamini le linee guida degli acquisti e generi un "Cybersecurity Annex" integrativo per imporre requisiti NIS2 obbligatori ai fornitori cloud terzi.

#### 2. Prompt da digitare nella chat (all'agente Root o allo Specialista Supply Chain):
> *"Verifica il documento `Procedura_Qualifica_Fornitori_OBSOLETA.txt` rispetto all'Art. 24 comma 2 lettera d) della NIS2. Poiché mancano i requisiti per la sicurezza della supply chain cloud, scrivi un 'Cybersecurity Annex' (Allegato di Sicurezza) in Markdown pronto da aggiungere ai nuovi contratti per sanare le lacune."*

#### 3. Comportamento dell'Agente:
*   L'agente rileva che la vecchia procedura richiede solo la certificazione generica ISO 9001 (Qualità) e non cita cloud, vulnerabilità o incidenti del fornitore.
*   Genera un documento integrativo da allegare ai contratti futuri che impone ISO 27017/27018, penali e diritti di audit.

#### 4. Risposta attesa (Output dell'Agente):
```markdown
### Lacune Rilevate nel documento obsoleto:
* Nessun requisito di certificazione di sicurezza specifico per i cloud provider (ISO 27017/27018).
* Assenza del diritto di audit di sicurezza sui sistemi del fornitore.
* Mancanza dell'obbligo di notifica a Lepida di incidenti informatici occorsi al fornitore.

---

### ALLEGATO TECNICO CONTRATTUALE: Cybersecurity Annex (Lepida SpA)

#### Art. 1 - Certificazioni Obbligatorie
Il Fornitore di servizi Cloud dichiara e garantisce di essere in possesso delle certificazioni ISO/IEC 27001, ISO/IEC 27017 e ISO/IEC 27018 in corso di validità.

#### Art. 2 - Diritti di Audit (Right to Audit)
Lepida SpA si riserva il diritto di effettuare verifiche e audit di sicurezza (anche tramite penetraton test coordinati) sui sistemi del Fornitore utilizzati per l'erogazione del servizio, con preavviso di 5 giorni lavorativi.

#### Art. 3 - Gestione Incidenti del Fornitore
Il Fornitore ha l'obbligo di notificare a Lepida SpA qualsiasi incidente informatico che interessi le infrastrutture di erogazione del servizio entro **24 ore** dal rilevamento.
```

---

## FASE 3: Presentazione dell'Assessment Finale (Tabella Gap / Conformità)

Per concludere la demo, puoi chiedere al Root Agent:
> *"Genera un report finale in formato tabellare che riassuma quali documenti obsoleti abbiamo analizzato, quali lacune abbiamo corretto e quali nuovi documenti conformi sono stati generati."*

L'agente produrrà una tabella riepilogativa chiara dell'attività di assessment e fix completata.
