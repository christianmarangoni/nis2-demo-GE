# Prototipo Agentic RAG per Conformità NIS2

## Obiettivo

Sistema multi-agente basato su Vertex AI Agent Builder per l'assessment della conformità alla direttiva NIS2 (D.Lgs 138/2024) per Lepida.

## Architettura Implementata

**Architettura Multi-Agente (Agent-to-Agent)**:
**1 Root Supervisor (Default Agent)** che riceve le richieste e instrada l'utente verso **8 Sub-Agenti Specialisti** con copertura al 100% dell'Art. 24 comma 2 (10 misure obbligatorie a-l) e obblighi ancillari. L'interazione utente è centralizzata sul Root Agent.

### Mappatura Completa Art. 24 c.2 → Agenti

| Lett. | Misura Obbligatoria | Agente Assegnato |
|:---:|---|---|
| **a** | Politiche di analisi dei rischi | Analisi Rischi e Audit |
| **b** | Gestione degli incidenti + notifica | Gestione Incidenti |
| **c** | Continuità operativa, backup, DR | Continuità Operativa |
| **d** | Sicurezza catena di approvvigionamento | Supply Chain |
| **e** | Sicurezza sviluppo/manutenzione sistemi + vulnerabilità | Sicurezza Sistemi e Vulnerabilità |
| **f** | Valutazione efficacia delle misure | Analisi Rischi e Audit |
| **g** | Igiene informatica e formazione | Igiene TIC, Crittografia e MFA |
| **h** | Crittografia e cifratura | Igiene TIC, Crittografia e MFA |
| **i** | Personale, accessi e asset | Personale, Accessi e Asset |
| **l** | MFA, comunicazioni protette | Igiene TIC, Crittografia e MFA |

### Copertura Obblighi Ancillari

| Articolo | Obbligo | Agente |
|---|---|---|
| Art. 7 | Registrazione ACN | Governance |
| Art. 23 | Responsabilità vertici | Governance |
| Art. 16 | Divulgazione vulnerabilità | Sicurezza Sistemi |
| Art. 27 | Certificazioni TIC | Governance |
| Art. 28 | Specifiche tecniche | Igiene TIC |
| Art. 30 | Categorizzazione attività | Governance |
| Art. 34-37 | Vigilanza e audit | Analisi Rischi e Audit |
| Art. 38 | Sanzioni | Governance |

## Struttura del Repository

*   [DEMO_PLAYBOOK.md](DEMO_PLAYBOOK.md): Guida passo-passo per configurare e presentare la demo con scenari di verifica e gap-fix.
*   [root_supervisor/](root_supervisor/agent_config.md): Agente principale di smistamento (Routing verso i Sub-Agenti).
*   [specialist_governance/](specialist_governance/agent_config.md): Governance, Compliance e Sanzioni (Art. 23, 7, 27, 30, 38).
*   [specialist_incident/](specialist_incident/README.md): Gestione Incidenti e Notifiche (Art. 24 c.2 lett. b, Art. 25, 26).
*   [specialist_continuity/](specialist_continuity/README.md): Continuità Operativa e DR (Art. 24 c.2 lett. c).
*   [specialist_supply_chain/](specialist_supply_chain/README.md): Sicurezza Supply Chain (Art. 24 c.2 lett. d).
*   [specialist_ict_security/](specialist_ict_security/README.md): Igiene TIC, Crittografia e MFA (Art. 24 c.2 lett. g, h, l, Art. 28).
*   [specialist_risk_audit/](specialist_risk_audit/README.md): Analisi Rischi e Audit di Efficacia (Art. 24 c.2 lett. a, f, Art. 34, 35).
*   [specialist_system_vuln/](specialist_system_vuln/README.md): Sicurezza Sistemi e Vulnerabilità (Art. 24 c.2 lett. e, Art. 16).
*   [specialist_personnel_asset/](specialist_personnel_asset/README.md): Personale, Accessi, Asset e Sicurezza Fisica (Art. 24 c.2 lett. i).
*   [documenti_reali/](documenti_reali/README.md): Cartella contenente i documenti pubblici reali scaricati (da inserire in Google Drive).
*   [documenti_simulati/](documenti_simulati/README.md): Cartella contenente i piani e le policy aziendali simulate (in formato Markdown).
*   [gcs_upload/](gcs_upload/README.md): Copie di tutti i file di configurazione, normative e simulazioni rinominati in `.txt` pronti per GCS.


Ogni cartella degli agenti contiene:
- **`agent_config.md`** — System prompt, modello e descrizione dell'agente
- **`normativa_estratto.md`** — Estratto del D.Lgs. 138/2024 pertinente all'agente

## Lavoro Completato

| Fase | Stato |
|---|:---:|
| Gap Analysis dell'atto completo (7871 righe) | ✅ |
| Migrazione da 5 a 8 agenti | ✅ |
| Creazione agent_config.md per tutti gli 8 agenti | ✅ |
| Estrazione normativa_estratto.md per tutti gli 8 specialisti | ✅ |
| Rimozione cartelle legacy (business_continuity, incident_management) | ✅ |
| Download dei 5 documenti reali da `id.lepida.it` | ✅ |
| Generazione dei 5 documenti interni simulati in Markdown | ✅ |
| Aggiornamento README.md con tabella agenti | ✅ |
| Push su GitHub (incluso `documenti_reali` e `documenti_simulati`) | ✅ |

## Setup su Vertex AI Agent Builder

1. **Creazione App e Root Agent**: Creare una singola Agent App in Vertex AI Agent Builder. Il Default Agent agirà da `root_supervisor`. Incollare le sue istruzioni (da `root_supervisor/agent_config.md`).
2. **Creazione 8 Sub-Agenti Specialisti**: All'interno della stessa app, creare gli 8 agenti specialisti come sub-agenti, copiando le rispettive System Instructions dai file `specialist_*/agent_config.md`.
3. **Data Store Google Drive (PDF < 80 pagine)**: Caricare tutti i file PDF contenuti nella cartella `documenti_reali/` su Google Drive ed associarli ai relativi Data Store.
4. **Data Store GCS (file .txt)**: Caricare i file `.txt` della cartella `gcs_upload/` (normative e documenti simulati) all'interno di bucket GCS ed associarli ai rispettivi Data Store.
5. **Associazione Data Store**: Associare i Data Store esclusivamente ai rispettivi sub-agenti specialisti (il Root Agent non ha bisogno di Data Store).
6. **Routing**: Configurare le regole di routing nel Root Agent affinché indirizzi le richieste ai sub-agenti in base all'argomento richiesto dall'utente.
