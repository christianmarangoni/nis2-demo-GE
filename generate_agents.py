import os
import json

agents = [
    {
        "folder": "root_supervisor",
        "name": "Agente Root (Supervisore NIS2)",
        "description": "Punto di contatto unico per l'operatore Lepida. Gestisce l'intento dell'utente e instrada la conversazione all'agente specialista corretto.",
        "model": "gemini-1.5-flash",
        "system_instruction": "Sei l'assistente principale per la conformità NIS2 di Lepida. Il tuo scopo è analizzare la richiesta dell'utente (es. 'Valuta policy di backup') e instradare la conversazione al sub-agente specialista competente in base all'area funzionale. Non rispondere direttamente sui contenuti tecnici della NIS2, ma delega agli specialisti.",
        "normativa": "# Istruzioni Generali NIS2\n\nIl D.Lgs. 138/2024 definisce i requisiti di sicurezza per i soggetti essenziali e importanti. Il tuo compito non è valutare i documenti, ma comprendere le 5 macro-aree di intervento (Governance, Incidenti, Continuità, Supply Chain, Sicurezza Logica) per indirizzare le richieste."
    },
    {
        "folder": "specialist_governance",
        "name": "Specialista Governance e Sicurezza",
        "description": "Agente specializzato nella valutazione delle policy aziendali, dell'allocazione delle responsabilità ai vertici aziendali e della formazione in ambito cybersecurity.",
        "model": "gemini-1.5-pro",
        "system_instruction": "Sei l'esperto NIS2 per l'area Governance. Confronta i documenti di Lepida (dal tool Drive) con le normative NIS2 (dal tool GCS). Verifica in particolare se i vertici aziendali hanno approvato le misure di gestione dei rischi e se è prevista formazione obbligatoria per i dipendenti. Segnala le lacune.",
        "normativa": "# Estratto D.Lgs. 138/2024 - Governance\n\nGli organi di amministrazione e direttivi dei soggetti essenziali e importanti devono approvare le misure di gestione dei rischi di sicurezza informatica e sovrintenderne l'implementazione.\nDevono inoltre seguire una formazione specifica e incoraggiare l'offerta di formazione periodica ai dipendenti per identificare i rischi e valutare le pratiche di igiene informatica."
    },
    {
        "folder": "specialist_incident_management",
        "name": "Specialista Gestione Incidenti",
        "description": "Agente specializzato nel valutare le procedure di incident response, rilevamento, contenimento e notifica degli incidenti significativi al CSIRT Italia.",
        "model": "gemini-1.5-pro",
        "system_instruction": "Sei l'esperto NIS2 per la Gestione degli Incidenti. Valuta i piani di incident response di Lepida. Verifica la presenza di procedure chiare per il rilevamento precoce, il contenimento e i processi di notifica (Early Warning entro 24h, notifica completa entro 72h) verso l'ACN/CSIRT. Evidenzia cosa manca rispetto alla normativa.",
        "normativa": "# Estratto D.Lgs. 138/2024 - Gestione Incidenti\n\nI soggetti essenziali e importanti devono notificare senza ingiustificato ritardo al CSIRT Italia qualsiasi incidente significativo.\nLa notifica prevede:\n1. Pre-allarme (Early Warning) entro 24 ore dalla conoscenza dell'incidente.\n2. Notifica dell'incidente entro 72 ore con aggiornamento sulla situazione.\n3. Relazione finale entro un mese dalla notifica iniziale.\nLe misure devono includere procedure per la prevenzione, il rilevamento e la risposta agli incidenti."
    },
    {
        "folder": "specialist_business_continuity",
        "name": "Specialista Continuità Operativa",
        "description": "Agente specializzato nell'analisi dei piani di Disaster Recovery, Business Continuity e gestione delle crisi in caso di attacco informatico.",
        "model": "gemini-1.5-pro",
        "system_instruction": "Sei l'esperto NIS2 per la Continuità Operativa. Analizza i documenti di backup, disaster recovery e gestione crisi di Lepida. Accertati che ci siano procedure per il mantenimento o il ripristino delle funzioni aziendali vitali durante o dopo un incidente, compresi backup sicuri e isolati.",
        "normativa": "# Estratto D.Lgs. 138/2024 - Continuità Operativa\n\nLe misure di gestione dei rischi devono includere la gestione della continuità operativa, come ad esempio la gestione dei backup e il ripristino in caso di disastro (Disaster Recovery), nonché la gestione delle crisi.\nDeve essere garantito che i backup siano protetti contro la compromissione, possibilmente offline o immutabili, per resistere ad attacchi ransomware."
    },
    {
        "folder": "specialist_supply_chain",
        "name": "Specialista Supply Chain",
        "description": "Agente specializzato nella valutazione della sicurezza nei rapporti con i fornitori, inclusi i provider di servizi cloud e servizi gestiti.",
        "model": "gemini-1.5-pro",
        "system_instruction": "Sei l'esperto NIS2 per la Sicurezza della Supply Chain. Valuta i contratti e le procedure di qualifica fornitori di Lepida. Verifica che siano presi in considerazione i rischi specifici derivanti dai fornitori terzi (es. MSP, fornitori cloud) e che siano richiesti standard di sicurezza adeguati lungo tutta la catena di approvvigionamento.",
        "normativa": "# Estratto D.Lgs. 138/2024 - Sicurezza della Catena di Approvvigionamento\n\nI soggetti devono gestire i rischi per la sicurezza informatica nella catena di approvvigionamento. Questo include gli aspetti relativi alla sicurezza riguardanti le relazioni tra ogni soggetto e i suoi diretti fornitori o prestatori di servizi.\nSi deve tenere conto delle vulnerabilità specifiche di ciascun fornitore diretto e della qualità dei prodotti e delle pratiche di sicurezza informatica dei fornitori (inclusi processi di sviluppo sicuro)."
    },
    {
        "folder": "specialist_ict_security",
        "name": "Specialista Sicurezza Logica e Igiene TIC",
        "description": "Agente specializzato in crittografia, gestione delle vulnerabilità, controllo degli accessi MFA e sicurezza delle comunicazioni.",
        "model": "gemini-1.5-pro",
        "system_instruction": "Sei l'esperto NIS2 per l'Igiene TIC e Sicurezza Logica. Valuta le policy tecniche di Lepida. Verifica l'uso sistematico della crittografia, l'autenticazione a più fattori (MFA) per gli accessi, le procedure di patching e vulnerability assessment, e l'adozione di pratiche di igiene informatica di base.",
        "normativa": "# Estratto D.Lgs. 138/2024 - Igiene Informatica e Sicurezza Logica\n\nLe misure devono comprendere:\n- Pratiche di igiene informatica di base (aggiornamenti, gestione patch, configurazioni sicure).\n- Politiche sull'uso della crittografia e, ove opportuno, della cifratura end-to-end.\n- Controllo degli accessi, utilizzo dell'autenticazione a più fattori (MFA) o dell'autenticazione continua, comunicazioni vocali, video e testuali sicure.\n- Gestione e divulgazione coordinata delle vulnerabilità."
    }
]

for agent in agents:
    os.makedirs(agent['folder'], exist_ok=True)
    
    # Write configuration
    config_content = f"""# {agent['name']}

**Description:** {agent['description']}

**Suggested Model:** `{agent['model']}`

## System Instructions
```text
{agent['system_instruction']}
```
"""
    with open(os.path.join(agent['folder'], 'agent_config.md'), 'w') as f:
        f.write(config_content)
        
    # Write normativa
    with open(os.path.join(agent['folder'], 'normativa_estratto.md'), 'w') as f:
        f.write(agent['normativa'])

print("Struttura agenti generata con successo.")
