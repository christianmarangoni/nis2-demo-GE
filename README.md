# Blueprint Configurazione Prototipo NIS2 (Vertex AI)

In base alle conferme e all'analisi del **D.Lgs. 138/2024** (NIS2 Italia), questo documento funge da *blueprint* per implementare il prototipo in modalità no-code su Google Cloud (Gemini Enterprise App / Vertex AI Agent Builder).

## Architettura del Prototipo

> **Sulla frammentazione del datastore:** 
La frammentazione dei documenti in base all'area è la **best practice** per applicazioni RAG avanzate. Il D.Lgs. 138/2024 (e le successive determinazioni ACN) impone misure raggruppabili in 5 categorie chiave. Creare un Datastore specifico per ogni area riduce drasticamente le "allucinazioni" dell'LLM, aumentando la precisione perché ogni Agente Specialista cercherà solo nel perimetro di sua competenza.

## 1. Definizione delle Aree Funzionali (Gli Agenti Specialisti)

Dall'analisi della NIS2 e dei requisiti di gestione del rischio, struttureremo 5 Agenti Specialisti:

1.  **Agente Governance e Sicurezza** (Policy, formazione, responsabilità dei vertici).
2.  **Agente Gestione Incidenti** (Incident response, notifica e monitoraggio).
3.  **Agente Continuità Operativa** (Business continuity, backup e crisis management).
4.  **Agente Supply Chain** (Sicurezza degli approvvigionamenti e fornitori).
5.  **Agente Sicurezza Logica e Igiene TIC** (Controllo accessi, crittografia, vulnerabilità).

La configurazione delle istruzioni di sistema per ciascun agente e l'estratto della normativa da caricare sono disponibili nelle rispettive sottocartelle di questa repository.

## 2. Architettura dei Datastore (Vertex AI Search)

### Google Cloud Storage (GCS) - "La Regola"
Per i documenti complessi (il D.Lgs. 138/2024, gli allegati tecnici, le linee guida ACN e NIST), dividiamo i documenti in 5 bucket o 5 folder separati su GCS, uno per ogni area funzionale. 
*   **Esempio:** `gs://lepida-nis2-normative/gestione_incidenti/` (conterrà solo la manualistica normativa relativa agli incidenti).
*   Da questi 5 percorsi creeremo **5 Data Store separati** in Vertex AI.

### Google Drive - "La Pratica"
Per la flessibilità richiesta, utilizzeremo **Shared Drives**. Configureremo un Data Store in Vertex AI collegato a un Drive condiviso chiamato `NIS2_Valutazione_Lepida`.
All'interno, creeremo 5 cartelle (una per area). Gli operatori caricheranno qui i loro documenti semplici (policy attuali, moduli, organigrammi). I permessi potranno essere mantenuti ampi a livello di Shared Drive.

## 3. Configurazione No-Code su Vertex AI Agent Builder

La costruzione fisica del prototipo segue questi passaggi sull'interfaccia standard di Vertex AI Agent Builder (Dialogflow CX Agent Designer):

> [!TIP]
> Tutto questo setup avviene senza scrivere codice, sfruttando i "Tools" e il routing nativo di Gemini Enterprise.

1.  **Creazione dell'Agente Root (Supervisore):**
    *   **Istruzione:** "Sei l'assistente principale per la conformità NIS2 di Lepida. Il tuo scopo è capire quale area della sicurezza l'utente vuole valutare e inoltrare la richiesta allo specialista competente. Non rispondere direttamente nel merito."
2.  **Creazione dei Tools (Data Store):**
    *   Nella sezione *Tools*, aggiungeremo il connettore a GCS (5 datastore normativi) e il connettore a Google Drive.
3.  **Creazione dei 5 Sub-Agents (Specialisti):**
    *   Prendiamo ad esempio l'**Agente Gestione Incidenti**.
    *   **Istruzione:** "Sei l'esperto NIS2 per la gestione incidenti. Usa il tool `GCS_Incidenti_Normativa` per capire i requisiti legali. Usa il tool `Drive_Lepida_Incidenti` per leggere le procedure attuali di Lepida. Confrontali e scrivi un report su cosa manca."
    *   **Assegnazione Tools:** A questo sub-agente assegneremo solo i due datastore specifici della sua area.
4.  **Impostazione del Routing:**
    *   Nell'agente Root, configureremo transizioni basate sugli intenti (es. se l'utente nomina "backup", passa all'Agente Continuità Operativa).

## Conclusione

Con questo setup, potrai presentare a Lepida un prototipo funzionante direttamente nell'interfaccia di test di Agent Builder. 
L'operatore caricherà un documento in Drive, aprirà la chat di test sulla destra dello schermo e scriverà: *"Valuta la nostra nuova policy di Incident Response"*. 
L'agente Root capirà l'intento, passerà il comando al Sub-Agent Gestione Incidenti, che leggerà GCS, leggerà Drive, e fornirà l'analisi dei gap. 

Tutto gestito con servizi Enterprise nativi e zero codice backend.
