# Piano di Continuità Operativa e Disaster Recovery — Lepida SpA (SIMULATO)

**Codice Documento:** PX-SEC-BCP-002  
**Versione:** 2.4  
**Classificazione:** Riservato (C3)  
**Destinatari:** Infrastructure Team, Storage & Backup Administrators, Direttore Data Center, DPO  

---

## 1. Introduzione e Strategia di Resilienza
Il presente piano definisce la strategia di Lepida SpA per garantire la disponibilità dei servizi ICT erogati agli Enti Soci e la protezione delle basi di dati regionali, in conformità agli obblighi di continuità operativa stabiliti dall'Art. 24 comma 2 lettera c) del D.Lgs. 138/2024 (NIS2).  
La strategia si basa sulla ridondanza geografica dei Data Center di Lepida, dislocati in Emilia-Romagna su 4 siti principali (Bologna, Parma, Ravenna, Ferrara), interconnessi in fibra ottica proprietaria.

---

## 2. Politica di Gestione dei Backup

La gestione delle copie di sicurezza segue una rigida impostazione multi-livello per contrastare attacchi di tipo ransomware e guasti hardware estesi.

### Regola dei Backup (3-2-1-1)
*   **3 copie dei dati:** 1 produzione attiva e almeno 2 copie di backup.
*   **2 media differenti:** Utilizzo di storage di classe enterprise (SAN/NAS) e storage a oggetti immutabile.
*   **1 copia offsite:** Replicazione geografica asincrona dei backup su un Data Center Lepida secondario a distanza > 50km.
*   **1 copia offline / immutabile (Immutable Backup):** Configurazione dei bucket di backup con tecnologia **WORM (Write Once Read Many)**. I file di backup memorizzati non possono essere modificati, cancellati o sovrascritti da alcun utente (inclusi gli amministratori di dominio) per un periodo minimo di **30 giorni**.

### Frequenza e Retention
*   **Backup Incrementale:** Eseguito a cadenza giornaliera per tutti i server e database (retention: 30 giorni).
*   **Backup Full:** Eseguito a cadenza settimanale (retention: 90 giorni).
*   **Backup di Sistema (Immagini VM):** Eseguito mensilmente o ad ogni aggiornamento applicativo significativo.

---

## 3. Obiettivi di Ripristino (RTO e RPO) per Servizi Critici

Lepida classifica i propri servizi in 3 fasce di criticità. Ad ognuna sono associati specifici obiettivi di **Recovery Time Objective (RTO)** e **Recovery Point Objective (RPO)**:

| Servizio | Livello Criticità | RTO (Tempo max ripristino) | RPO (Perdita dati max tollerata) |
|---|---|---|---|
| **LepidaID (SPID)** | Livello 1 - Vitale | < 2 ore | < 15 minuti |
| **Cloud Regionale (IAAS PA)** | Livello 1 - Vitale | < 4 ore | < 1 ora |
| **PEC e Conservazione Digitale** | Livello 2 - Importante | < 12 ore | < 4 ore |
| **Sistemi Interni / Gestionali** | Livello 3 - Standard | < 24 ore | < 12 ore |

---

## 4. Procedure di Attivazione del Disaster Recovery (DR)

### Trigger di Attivazione
Il piano di Disaster Recovery viene attivato dal Comitato di Crisi qualora si verifichi una delle seguenti condizioni presso il Data Center Primario (Bologna):
*   Blackout elettrico totale prolungato (> 4 ore) con guasto simultaneo dei gruppi elettrogeni di continuità.
*   Incendio o allagamento catastrofico delle sale server.
*   Attacco ransomware generalizzato che compromette i sistemi di produzione.

### Fasi del Ripristino Geografico
1.  **Dichiarazione dello stato di emergenza:** Il Comitato di Crisi ordina lo switch-over sul Data Center di Disaster Recovery (Parma).
2.  **Riorientamento del traffico di rete:** Aggiornamento dei record DNS regionali tramite i sistemi di bilanciamento geografico globale (GSLB) per reindirizzare le chiamate utente sul sito secondario.
3.  **Montaggio delle repliche storage:** Attivazione dei volumi storage replicati in sincrono/asincrono sul sito di Parma.
4.  **Accensione e verifica delle Virtual Machine:** Avvio delle istanze VM nell'ordine di dipendenza stabilito (Database -> Middleware -> Applicativi Front-end).
5.  **Verifiche di integrità:** Test funzionali di login su LepidaID e connettività delle PA interessate prima dell'apertura del servizio agli utenti.

---

## 5. Test e Addestramento Periodico
Il presente piano viene sottoposto a test di efficacia con simulazioni reali di disastro:
*   **Test di DR LepidaID:** Eseguito a cadenza semestrale, con switch reale del traffico sul sito di Parma durante finestre di manutenzione notturna.
*   **Test di ripristino dei backup:** Eseguito mensilmente su base campionaria (ripristino e validazione di almeno il 5% delle VM su ambiente di staging isolato).
*   Ogni test viene documentato in un apposito **Verbale di Test di DR**, evidenziando i tempi di RTO effettivi registrati ed eventuali azioni correttive.
