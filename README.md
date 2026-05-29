# Prototipo Agentic RAG per Conformità NIS2 (Lepida)

Questo repository contiene la struttura progettuale e le istruzioni (System Prompts) per la configurazione di un sistema **Agentic RAG** basato su Google Cloud Vertex AI Agent Builder, dedicato all'assessment della conformità alla direttiva NIS2 (D.Lgs 138/2024) per Lepida.

L'architettura è **no-code**, permettendo una configurazione diretta tramite l'interfaccia standard di Vertex AI.

## L'Architettura Multi-Agente (Hierarchical Routing)

A seguito di una *Gap Analysis* completa sull'intero testo legislativo, l'architettura è strutturata su **1 Root Agent (Supervisore)** e **8 Sub-Agenti Specialisti**, garantendo il 100% di copertura dell'Art. 24 comma 2 (Misure di gestione dei rischi) e degli obblighi di notifica, registrazione e sanzionatori.

### Panoramica degli Agenti

| Agente | Ruolo e Obiettivo | Copertura Normativa |
|---|---|---|
| **Root Supervisor** | Punto di contatto unico. Analizza l'intento dell'utente e instrada la richiesta allo specialista competente. | N/A (Routing) |
| **Governance, Compliance e Sanzioni** | Valuta responsabilità vertici, formazione, registrazione ACN e consapevolezza sanzioni. | Art. 23, 7, 27, 30, 38 |
| **Gestione Incidenti** | Valuta procedure di incident response e rispetto delle tempistiche di notifica al CSIRT Italia. | Art. 24(b), 25, 26 |
| **Continuità Operativa** | Valuta piani di backup, disaster recovery e crisis management. | Art. 24(c) |
| **Supply Chain** | Valuta la sicurezza della catena di fornitura e i requisiti verso i fornitori diretti. | Art. 24(d) |
| **Igiene TIC, Crittografia e MFA** | Valuta le pratiche operative di igiene, l'uso della crittografia e l'implementazione dell'MFA. | Art. 24(g,h,l) |
| **Analisi Rischi e Audit** | Valuta l'impianto metodologico di analisi dei rischi e le procedure di audit di efficacia delle misure. | Art. 24(a,f) |
| **Sicurezza Sistemi e Vulnerabilità** | Valuta il ciclo di vita sicuro del software (SDLC) e la gestione/divulgazione delle vulnerabilità. | Art. 24(e), 16 |
| **Personale, Accessi e Asset** | Valuta l'affidabilità HR, il controllo accessi (IAM), l'inventario asset e la sicurezza fisica. | Art. 24(i) |

## Gestione dei Dati (Data Stores)

Per evitare allucinazioni e garantire risposte precise, la base di conoscenza viene segmentata. Durante la configurazione in Vertex AI, è necessario:
1. Creare **Data Store (GCS)** distinti, contenenti gli estratti della normativa per ogni dominio.
2. Includere i documenti aziendali Lepida pertinenti a quella specifica area (tramite integrazione Google Drive o GCS).
3. Collegare ciascun Data Store al rispettivo Agente Specialista tramite i Tools di Data Store.

## Istruzioni di Setup su Vertex AI Agent Builder

1. Creare l'**Agente Root** usando il modello `gemini-2.5-flash` per garantire bassa latenza nel routing. Assegnare le istruzioni presenti nella cartella `root_supervisor`.
2. Creare progressivamente gli **8 Agenti Specialisti** usando il modello `gemini-3-pro` per il ragionamento complesso, copiando le istruzioni dalle rispettive cartelle.
3. Fornire agli Specialisti l'accesso ai rispettivi Data Store tramite i Tool standard dell'interfaccia.
4. Nell'Agente Root, aggiungere le regole di routing (tramite l'interfaccia Agent Builder) per delegare l'esecuzione agli Specialisti in base all'intento rilevato.
