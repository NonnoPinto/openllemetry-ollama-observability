🤖 Ollama Local LLM + OpenLLMetry + Traceloop
=============================================

Questo progetto implementa una **CLI Chat interattiva** che utilizza un modello di linguaggio (LLM) eseguito interamente in locale tramite **Ollama**, monitorato professionalmente con **OpenLLMetry** e visualizzato sulla dashboard cloud di **Traceloop**.

🏗️ Architettura
----------------

*   **Ollama (Docker):** Motore di inferenza locale. Scarica ed esegue i modelli (Llama 3.2).
    
*   **Python App (Docker):** Script interattivo che comunica con Ollama tramite l'SDK ufficiale.
    
*   **OpenLLMetry (SDK):** Strumentazione automatica che cattura prompt, risposte e latenze.
    
*   **Traceloop Cloud:** Backend di osservabilità dove vengono inviate le tracce (OTLP).
    

🚀 Requisiti Preliminari
------------------------

1.  **Docker** e **Docker Compose** installati.
    
2.  Un account gratuito su [Traceloop Cloud](https://app.traceloop.com).
    
3.  La tua **API Key** di Traceloop.
    

🛠️ Configurazione
------------------

1.  Crea un file .env come nell'esempio .env.example
    
2.  Inserisci la tua API key al posto del placeholder
    

🚦 Come Avviare il Progetto
---------------------------

### 1\. Build e Avvio dei Servizi

Scarica le immagini e avvia Ollama in background:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker compose up -d   `

### 2\. Verifica del Modello (opzionale)

Il servizio ollama-puller scaricherà automaticamente llama3.2:1b (circa 1.3GB). Verifica lo stato con:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker exec ollama ollama list   `

### 3\. Avvio della Chat Interattiva

Per interagire con il modello e inviare le tracce al cloud, esegui:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker compose run --rm app   `

📊 Osservabilità (Cosa controllare)
-----------------------------------

Una volta avviata la chat e inviato il primo messaggio:

1.  Accedi a [Traceloop Cloud](https://www.google.com/search?q=https://app.traceloop.com/traces).
    
2.  Troverai una traccia chiamata ollama-pure-chat.
    
3.  **Dettagli visibili:**
    
    *   **Prompt & Completion:** Il testo esatto della conversazione (grazie al supporto nativo).
        
    *   **Latenza:** Tempo di generazione del primo token e durata totale.
        
    *   **Modello:** Conferma dell'uso di llama3.2:1b.
        

🧹 Pulizia
----------

Per fermare tutti i servizi e rimuovere i container:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker compose down   `

_Nota: I modelli scaricati rimarranno salvati nel volume ollama\_storage per il prossimo avvio._
