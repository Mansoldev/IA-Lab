# CONOCIDOS

```
[LangGraph] (Orquesta el grafo de estado y la memoria)
  └── [Agente] (Supervisa la meta global)
        ├── [Prompt] ("Eres un analista de datos. Usa tus skills cuando corresponda.")
        ├── [Skill: Análisis de Datos]
        │     ├── [LLM] (Razona: "Primero necesito leer el CSV")
        │     └── [MCP Server / Tool: Leer Archivos] ──► Ejecuta la lectura de datos
        └── [Skill: Comunicación]
              ├── [LLM] (Razona: "Ahora enviaré el resultado por Slack")
              └── [MCP Server / Tool: Slack API] ──► Envía el mensaje
```

## LLM:

El motor probabilístico que procesa texto, comprende la intención y genera razonamientos.

## PROMPT:

Es la **instrucción o contexto de entrada** que se le entrega a un LLM para guiarlo sobre qué rol asumir, cómo razonar, qué formato usar y qué reglas debe respetar.

## TOOL:

Es una **función ejecutable** (código en Python, API REST, consulta SQL) con un nombre, una descripción clara y un esquema de parámetros que el modelo puede decidir invocar cuando necesita realizar una acción o consultar datos externos.

## SKILL:

En arquitecturas de agentes modernas, una **"Skill" (Habilidad)** es un paquete modular y autocontenido que le enseña al agente **cómo** resolver un tipo específico de tarea compleja. A diferencia de una simple herramienta ( *tool* ) que ejecuta una función atómica (ej.`get_weather()`), una skill agrupa:

1. **Un prompt especializado** con instrucciones paso a paso o heurísticas.
2. **Un subconjunto de herramientas (tools)** exclusivas para esa tarea.
3. **Ejemplos de pocas muestras ( *few-shot examples* )** de cómo abordar el problema.

## AGENT:

Es una entidad de software compuesta por un  **LLM (cerebro) + Memoria + Herramientas + Bucle de Razonamiento** . A diferencia de una llamada simple a un LLM, el agente evalúa una meta, decide qué herramientas usar, analiza el resultado devuelto por la herramienta y repite el proceso de forma autónoma hasta resolver la tarea.

## MCP (Model Context Protocol):

Desarrollado por  **Anthropic** , el **Model Context Protocol (MCP)** es un estándar abierto que funciona como un  **"puerto USB-C" para la Inteligencia Artificial** .

Antes de MCP, si querías que un agente de LangChain se conectara a GitHub, a una base de datos PostgreSQL, a Slack y a tu sistema de archivos local, tenías que escribir (o importar) integraciones y wrappers personalizados para cada servicio, lidiando con APIs y esquemas distintos.

* **¿Cómo funciona?** Separa la arquitectura en dos:
  * **Servidores MCP:** Aplicaciones ligeras que exponen datos, recursos o herramientas de forma estandarizada (ej. un servidor oficial de GitHub que expone herramientas para buscar repos o crear issues).
  * **Clientes MCP:** Tu agente o aplicación de IA que se conecta a esos servidores de forma genérica.
* **¿Cómo se aplica a los agentes?**
  En lugar de codificar herramientas estáticas dentro de tu grafo de LangGraph, tu agente actúa como un  **cliente MCP** . Al iniciar, el agente consulta dinámicamente a los servidores MCP conectados qué herramientas ( *tools* ), recursos ( *resources* ) y plantillas de prompts ( *prompts* ) tienen disponibles en ese momento. Esto hace que tus agentes sean altamente modulares, interoperables y capaces de descubrir capacidades nuevas sin modificar su código base.

## Entorno de agente:

Es el entorno que permite la ejecución del modelo LLM, puede ser de tipo motor simple (capa 2) como Ollama o de tipo aplicación/editor (capa 6) como copilot.

* **GitHub Copilot NO es el LLM** : Copilot es el  **Entorno de Agente / Aplicación (Capas 6, 7 y 8)** .
* Copilot combina una interfaz de usuario en VS Code + un bucle de agentes + un sistema de inyección de contexto (Indexación RAG del workspace,`tools` como la terminal o lectura de archivos).
* **El LLM (Capa 1)** en Copilot es  **GPT-4o, Claude 3.5 Sonnet, etc.** , corriendo en los servidores de GitHub/Microsoft.

Y hay 3 tipos:

1. Online: tipo chatgpt, gemini, deep seek.
2. Local editor: tipo copilot, cursor, open code, claude code, codex
3. Local motor: tipo Ollama o LM Studio

# CAPAS DEL ECOSISTEMA IA:

Para visualizar cómo se construye y funciona cualquier solución de Inteligencia Artificial (desde un simple bot hasta un agente complejo en VS Code), podemos dividir la arquitectura en  **6 capas principales** , ordenadas desde el motor físico/matemático hasta la interfaz final con el usuario:

```
[ Capa 6: Aplicación / Editor ]   ──► GitHub Copilot, Continue, Roo Code
[ Capa 5: Agente / Orquestación] ──► LangGraph, CrewAI, AutoGen
[ Capa 4: Contexto / Conexión ]  ──► MCP (Model Context Protocol), RAG, Vector DBs
[ Capa 3: Framework Base ]       ──► LangChain, LlamaIndex, SDKs oficiales
[ Capa 2: Motor / Inferencia ]   ──► LM Studio, Ollama, vLLM, OpenAI API
[ Capa 1: Modelo (LLM/Peso) ]    ──► GPT-4o, Claude 3.5 Sonnet, Llama 3, DeepSeek-V3
```

## 1 Capa de Modelo (El "Cerebro" o Pesos)

¿Qué es? Las redes neuronales entrenadas (los archivos con miles de millones de parámetros/pesos matemáticos). No "ejecutan" nada por sí solos; son el conocimiento puro comprimido.

Ejemplos: Claude 3.5 Sonnet (Anthropic), GPT-4o (OpenAI), Llama 3.3 (Meta, Open Source), DeepSeek-V3 / R1 (DeepSeek, Open Source), Gemini 2.5 Pro (Google).

## 2 Capa de Inferencia / Motor de Ejecución

¿Qué es? El software o infraestructura que carga el modelo en la memoria (VRAM/RAM) y realiza los cálculos matemáticos para transformar tus tokens de entrada en tokens de respuesta.

Ejemplos:

Nube: OpenAI API, Google AI Studio, Groq (muy famoso por usar chips LPU ultra rápidos).

Local: LM Studio, Ollama, vLLM, llama.cpp, Claude Code, Codex, OpenCode, Open Claw, Hermes.

## 2 Capa de Framework Base

¿Qué es? Las librerías de programación que estandarizan el envío de prompts, el manejo de memoria básica, las llamadas a APIs y la creación de esquemas para funciones (tools).

Ejemplos: LangChain (Python/JS), LlamaIndex (especializado en datos y RAG), SDKs oficiales de OpenAI/Anthropic.

## 4 Capa de Contexto y Conexión (Protocolos y Datos)

¿Qué es? La capa que conecta al LLM con el mundo exterior: archivos, bases de datos externas o herramientas, asegurando que el modelo reciba la información correcta en el momento adecuado.

Ejemplos: MCP (Model Context Protocol) para estandarizar la conexión a APIs, bases de datos vectoriales como ChromaDB o Qdrant (para RAG).

## 5 Capa de Agente y Orquestación

¿Qué es? El motor de lógica de alto nivel que gestiona ciclos de autonomía, decisiones multi-paso, corrección de errores, memoria a largo plazo y estados persistentes.

Ejemplos: LangGraph (grafos de estado), CrewAI (agentes por roles), AutoGen (de Microsoft).

## 6 Capa de Aplicación / Interfaz

¿Qué es? La herramienta, extensión o aplicación con la que interactúa el ser humano de forma directa.

Ejemplos: La interfaz web de ChatGPT, extensiones de VS Code como GitHub Copilot, Continue, Roo Code, o aplicaciones CLI de terminal como Claude Code.

# Opciones para ejecutar IA:

```
			   ┌──────────────────────────────────────────┐
               │    ¿CÓMO USAS LA IA EN TU EQUIPO?        │
               └────────────────────┬─────────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
[ 1. NUBE PURA ]           [ 2. HÍBRIDO / LOCAL-FIRST ]  [ 3. 100% LOCAL ]
- Web Apps / SaaS          - IDEs, Agentes en CLI        - Ejecución en GPU/RAM
- Procesa: Servidores      - Procesa: Servidores (APIs)  - Procesa: Tu hardware
- Ej: ChatGPT, Claude.ai   - Ej: Copilot, Roo Code       - Ej: LM Studio, Ollama
```

### Opción 1: Nube Pura (SaaS / Web App)

Todo ocurre en los servidores del proveedor. Tu ordenador actúa únicamente como un navegador visualizando una web.

* **Cómo funciona:** Abres una pestaña en el navegador, envías un mensaje y los superordenadores de la empresa procesan todo.
* **Tecnologías más utilizadas:**`ChatGPT` (OpenAI),`Claude.ai` (Anthropic),`Google Gemini`.
* **🔥 Lo más aclamado/Tendencia:**
  * **DeepSeek Chat:** Aclamado mundialmente por ofrecer capacidades de razonamiento profundo al nivel de OpenAI a un precio ultra accesible o de uso gratuito.
  * **OpenAI o3 / ChatGPT Search:** Modelos con capacidades de razonamiento complejo (Reasoning models) integrados directamente con navegación web en tiempo real.

### Opción 2: Híbrido / Local-First (Agentes que leen tu equipo pero procesan en Nube)

El software se ejecuta localmente en tu ordenador (lee tus carpetas, archivos, terminal, navega por tu sistema), pero  **el razonamiento pesado se envía mediante clave API a modelos en la nube** .

* **Cómo funciona:** Instalas una herramienta o extensión en tu equipo. Esta recopila el contexto local (tu código, un archivo `.pdf`, etc.) y se lo envía a un LLM en la nube para que le devuelva las instrucciones de qué hacer en tu sistema.
* **Tecnologías más utilizadas:** **GitHub Copilot** ,**Cursor** (un editor fork de VS Code diseñado para IA), **Continue** ,**Roo Code** (extensión de VS Code para agentes).
* **🔥 Lo más aclamado/Tendencia:**
  * **Claude Code:** Herramienta de terminal lanzada por Anthropic que actúa como un agente de desarrollo autónomo directamente en tu línea de comandos.
  * **Roo Code + MCP:** Agentes dentro de VS Code capaces de conectarse a múltiples servidores MCP locales (Postgres, GitHub, terminal) mientras usan modelos potentes como Claude 3.5 Sonnet o DeepSeek V3.

### Opción 3: 100% Local (Soberanía de Datos / Desconectado de Internet)

El modelo corre  **literalmente dentro de tu tarjeta gráfica (GPU) o tu procesador (RAM/Apple Silicon)** . No sale ni un solo byte a internet.

* **Cómo funciona:** Descargas la aplicación local, descargas el archivo del modelo (formatos como `.GGUF`) y tu hardware realiza todos los cálculos.
* **Tecnologías más utilizadas:**
  * **LM Studio:** La aplicación con interfaz gráfica ( *GUI* ) más popular y fácil de usar para explorar, descargar y ejecutar modelos locales.
  * **Ollama:** La herramienta de línea de comandos ( *CLI* ) por excelencia para levantar servidores de modelos locales en segundos con un simple `ollama run llama3`.
  * **Jan.ai:** Una alternativa *open-source* a LM Studio muy apreciada por su privacidad.
* **🔥 Lo más aclamado/Tendencia:**
  * **DeepSeek-R1 (versiones destiladas):** Modelos de razonamiento avanzado que han sido comprimidos (ej. versiones de 8B o 14B parámetros) para poder ejecutarse en ordenadores portátiles de consumo o MacBooks con chips M1/M2/M3/M4.
  * **Qwen 2.5 Coder / Qwen 2.5:** La familia de modelos open-source desarrollada por Alibaba, actualmente considerada la mejor opción abierta para autocompletado y generación de código en local.

# OTROS:

Habiendo pasado por LLMs, herramientas y grafos de estado, ya manejas la capa de aplicación principal. Para pasar al siguiente nivel como arquitecto de IA, te recomiendo explorar los siguientes bloques:

* **RAG Avanzado y GraphRAG:** Ir más allá de la búsqueda básica por vectores (embeddings). Aprende sobre estrategias de *chunking* inteligente, re-ranking (Cohere Rerank), consultas híbridas (BM25 + vectores) y **GraphRAG** (combinar bases de datos de grafos con recuperación de información para conectar entidades complejas).
* **Evaluación y Observabilidad (Evals & Tracing):** Los agentes son estocásticos (pueden fallar de formas impredecibles). Herramientas como  *LangSmith* ,*Arize Phoenix* o *TruLens* te enseñan a medir la calidad de las respuestas, detectar alucinaciones en bucles de agentes y hacer pruebas automatizadas ( *evals* ) antes de llevar un agente a producción.
* **Memoria Avanzada y Persistencia:** Más allá del historial de chat básico. Necesitas dominar la memoria episódica, la semántica (perfiles de usuario a largo plazo) y la gestión de checkpoints y estado distribuido en bases de datos (como PostgreSQL) para que tus agentes puedan pausar, reanudar o corregir errores a mitad de un flujo largo.
* **Orquestación Multi-Agente Avanzada:** Patrones más complejos que un supervisor simple, como arquitecturas jerárquicas, equipos colaborativos autónomos, sistemas de debate/consenso y agentes que escriben y ejecutan código de forma aislada (sandboxing).
* **Fine-Tuning y Alineación (Alignment):** Si en algún momento necesitas entrenar o ajustar modelos open-source (como Llama 3 o Mistral) usando técnicas como LoRA, QLoRA o DPO para que dominen un dominio o tono específico sin depender de APIs de terceros.
