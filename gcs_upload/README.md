# Cartella Upload GCS (Google Cloud Storage)

Questa cartella raccoglie tutti i file originariamente in formato Markdown (`.md`) convertiti in formato testo semplice (`.txt`). 

In conformità con la strategia di archiviazione della demo:
1.  **I file in questa cartella (`.txt`)** devono essere caricati in bucket di **Google Cloud Storage (GCS)** per alimentare i Data Store corrispondenti su Vertex AI.
2.  **I PDF con più di 80 pagine** (se presenti in futuro) verranno inseriti su GCS, mentre tutti i PDF di dimensione inferiore a 80 pagine rimangono sul canale **Google Drive**.

---

## Struttura della Cartella

Ogni sottocartella contiene i rispettivi file `.txt` corrispondenti alle configurazioni degli agenti, estratti della legge ed ai documenti simulati:

```
gcs_upload/
├── root_supervisor/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_governance/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_incident/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_continuity/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_supply_chain/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_ict_security/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_risk_audit/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_system_vuln/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
├── specialist_personnel_asset/
│   ├── agent_config.txt
│   └── normativa_estratto.txt
└── documenti_simulati/
    ├── Metodologia_Analisi_Rischi_e_Audit_Lepida_SIMULATO.txt
    ├── Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.md.txt -> Piano_Disaster_Recovery_e_Backup_Lepida_SIMULATO.txt
    ├── Piano_Incident_Response_Lepida_SIMULATO.txt
    ├── Policy_Gestione_Vulnerabilita_e_SDLC_Lepida_SIMULATO.txt
    └── Procedura_Qualifica_Fornitori_ICT_Lepida_SIMULATO.txt
```
