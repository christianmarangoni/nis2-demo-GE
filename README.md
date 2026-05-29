# Prototipo Agentic RAG per Conformità NIS2

## Obiettivo

Sistema multi-agente basato su Vertex AI Agent Builder per l'assessment della conformità alla direttiva NIS2 (D.Lgs 138/2024) per Lepida.

## Architettura Implementata

**1 Root Supervisor + 8 Agenti Specialisti** con copertura al 100% dell'Art. 24 comma 2 (10 misure obbligatorie a-l) e obblighi ancillari.

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

## Struttura Repository

```
nis2-agentic-rag-prototype/
├── README.md
├── generate_agents.py
├── root_supervisor/
├── specialist_governance/
├── specialist_incident/
├── specialist_continuity/
├── specialist_supply_chain/
├── specialist_ict_security/
├── specialist_risk_audit/
├── specialist_system_vuln/
├── specialist_personnel_asset/
├── documenti_reali/                # Documenti pubblici reali scaricati
│   ├── manuale_operativo.pdf       # Manuale Operativo LepidaID (SPID)
│   ├── carta_dei_servizi.pdf       # Carta dei Servizi LepidaID
│   ├── manuale_utente.pdf          # Guida utente LepidaID
│   ├── soluzioni_tecnologiche.pdf  # Allegati tecnici e soluzioni
│   └── trattamento_dati.pdf        # Informativa e flussi privacy (GDPR)
└── documenti_simulati/             # Documenti interni simulati (riservati)
    ├── Piano_Incident_Response_Lepida_SIMULATO.md
    ├── Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.md
    ├── Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.md
    ├── Policy_Gestione_Vulnerabilita_e_SDLC_Lepida_SIMULATO.md
    └── Metodologia_Analisi_Rischi_e_Audit_Lepida_SIMULATO.md
```

Ogni cartella contiene:
- **`agent_config.md`** — System prompt, modello e descrizione dell'agente
- **`normativa_estratto.md`** — Estratto del D.Lgs. 138/2024 pertinente all'agente

## Lavoro Completato

| Fase | Stato |
|---|:---:|
| Gap Analysis dell'atto completo (7871 righe) | ✅ |
| Migrazione da 5 a 8 agenti | ✅ |
| Creazione agent_config.md per tutti i 9 agenti | ✅ |
| Estrazione normativa_estratto.md per tutti gli 8 specialisti | ✅ |
| Rimozione cartelle legacy (business_continuity, incident_management) | ✅ |
| Download dei 5 documenti reali da `id.lepida.it` | ✅ |
| Generazione dei 5 documenti interni simulati in Markdown | ✅ |
| Aggiornamento README.md con tabella agenti | ✅ |
| Push su GitHub (incluso `documenti_reali` e `documenti_simulati`) | ✅ |

## Setup su Vertex AI Agent Builder

1. Creare l'**Agente Root** con `gemini-2.5-flash` per routing a bassa latenza
2. Creare gli **8 Specialisti** con `gemini-3-pro` per ragionamento complesso
3. Configurare i **Data Store GCS** con i rispettivi `normativa_estratto.md`
4. Integrare documenti aziendali Lepida via **Google Drive** nei Data Store (usando i file in `documenti_reali` e `documenti_simulati` per i test)
5. Configurare le regole di **routing** nel Root Agent
