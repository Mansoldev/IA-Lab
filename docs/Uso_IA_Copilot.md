## Modo Agente vs. Agente Concreto

* **Usar la IA en "Modo Agente" (Agent Mode):** Es una **modalidad de trabajo o un entorno de ejecución** de Copilot Chat.**En este modo, Copilot deja de responder como un simple autocompletar o chat y obtiene ** **permiso para ejecutar bucles de autonomía** **: explorar la estructura de tu proyecto, leer múltiples archivos, ejecutar comandos en la terminal (**`<span class="citation-194">npm test</span>`, `<span class="citation-194">git status</span>`), evaluar errores y aplicar parches de código por sí mismo.
* **Usar un "Agente Concreto" (Custom Agent):**Es un **rol o perfil especializado** cargado *dentro* del modo agente.^^Es un conjunto delimitado de  *Prompts* **, ***Skills* y *Tools* diseñados para resolver un problema específico (ejemplo: un  *Agente de Accesibilidad Web* **, un ** *Agente de Refactorización de BD* **, o un ** *Agente de Code Review* **).**

**En resumen:** El *Modo Agente* es el motor o la capacidad de actuar de forma autónoma; **un ***Agente Concreto* es el "traje" o la especialidad que le pones a ese motor para que cumpla una función con reglas y herramientas estrictas.

## ¿Cómo se cargan Agentes y Skills en VS Code con Copilot?

**VS Code permite extender Copilot mediante archivos Markdown estructurados con ** **YAML frontmatter** **.**^^ Se pueden definir a nivel global (para todos tus proyectos) o a nivel de espacio de trabajo (`.github/` en la raíz de tu repositorio) para compartirlos con tu equipo.

```
mi-proyecto/
└── .github/
    ├── agents/               <── Agentes Concretos
    │   └── accessibility.md
    └── skills/               <── Skills Reutilizables
        └── db-migrator/
            ├── SKILL.md
            └── schema-template.sql
```

### A. Crear un Agente Concreto (`.github/agents/`)

**Los agentes personalizados combinan instrucciones de rol y restricciones de herramientas.**^^Se definen en la carpeta `<span class="citation-187">.github/agents/</span>` creando un archivo `<span class="citation-187">.md</span>`

**Ejemplo:**`<span class="citation-186 citation-end-186">.github/agents/accessibility.md</span>`

**Markdown**

```Markdown
---
name: Accessibility Specialist
description: Agente experto en accesibilidad web (WCAG 2.1) y pruebas ARIA.
---

# Rol de Accesibilidad
Eres un agente especializado en auditoría e implementación de accesibilidad.

## Instrucciones y Reglas:
1. Siempre revisa los componentes HTML/JSX buscando atributos `aria-*` faltantes.
2. Comprueba el contraste de color según el estándar WCAG AA.
3. Si generas código, crea también sus pruebas asociadas usando Testing Library.
```

**Cómo usarlo en VS Code:** En el panel de Copilot Chat, abre el menú desplegable de agentes (donde normalmente dice "default") y selecciona tu  **Accessibility Specialist** . Todo el diálogo y el bucle de ejecución se acotarán a esas reglas.

### B. Crear una Skill Personalizada (`<span class="citation-185">.github/skills/</span>`)

**Una ****Skill** es un paquete con un procedimiento guiado paso a paso, ejemplos o archivos de soporte (como scripts o plantillas).

**Ejemplo:**`<span class="citation-183 citation-end-183">.github/skills/db-migrator/SKILL.md</span>`

```Markdown
---
name: db-migrator
description: Procedimiento para crear migraciones de base de datos de forma segura.
---

# Guía de Migración de Base de Datos

Cuando el usuario pida crear una nueva migración:
1. Revisa el archivo `schema.prisma` actual.
2. Genera el script SQL en la carpeta `prisma/migrations/`.
3. Valida que no incluya operaciones destructivas como `DROP TABLE` sin advertencia previa.
```

**Cómo usarlo en VS Code:** Las skills se invocan directamente desde el chat escribiendo un **slash command** (`/`):

```
/db-migrator añade la columna 'status' a la tabla de usuarios
```

### C. Conectar Servidores MCP en VS Code

Si tu agente o skill necesita consultar una API externa (por ejemplo, PostgreSQL, GitHub o Jira), puedes configurar servidores MCP desde los ajustes de VS Code:

1. **Presiona **`<span class="citation-182">Ctrl+Shift+P</span>` (o `<span class="citation-182">Cmd+Shift+P</span>` en Mac) y selecciona **Chat: Open Customizations** o busca la configuración de MCP.^^
2. Define el servidor MCP en tu archivo de configuración de VS Code (`settings.json` o configuración de Copilot):

```JSON
"github.copilot.chat.mcpServers": {
  "mi-postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/db"]
  }
}
```

Copilot descubrirá dinámicamente las **Tools** expuestas por el servidor de Postgres y el modo agente podrá utilizarlas para consultar tablas o esquemas.

## ¿Cómo puedes reutilizar lo que aprendiste en Python dentro de Copilot?

Aunque el código ejecutable de Python no corra nativamente dentro de la interfaz de Copilot,**sí puedes aprovechar tus conocimientos y conectar ambos entornos** de tres formas:

### A. Traduciendo la lógica a ficheros estándar (`.agent.md` y `SKILL.md`)

**La estructura mental que aprendiste para diseñar un agente (definir un system prompt estricto, darle un conjunto de reglas, estructurar instrucciones paso a paso) es exactamente la misma que usa VS Code para los agentes personalizados.**^^

* **Tu lógica en Python te enseña ***cómo* estructurar las instrucciones.^^Luego, escribes esos mismos comportamientos en formato Markdown para que Copilot los entienda de forma nativa en tu IDE.^^

### B. Usando MCP (Model Context Protocol) como pasarela de integración

Aquí es donde Python y Copilot se unen de verdad. **MCP es agnóstico del lenguaje** .

* Puedes escribir un servidor MCP en **Python** (usando la librería oficial de MCP para Python) que contenga tus herramientas personalizadas, lógica de negocio o conexiones a bases de datos.
* Luego, configuras ese servidor Python en el `settings.json` de VS Code para que  **GitHub Copilot lo consuma como cliente** . De este modo, cuando estés chateando en el editor, Copilot llamará por debajo a las herramientas que programaste en Python.

### C. Exponiendo tu Agente de LangGraph como una API (FastAPI)

Si creaste un agente súper complejo en LangGraph que hace flujos de múltiples pasos, puedes levantarlo como un microservicio en Python usando  **FastAPI** .

* Después, puedes construir una pequeña extensión de VS Code o conectar Copilot (mediante un agente personalizado y un servidor MCP puente) para que envíe peticiones a tu API de Python y reciba las respuestas procesadas por tu grafo.

## Haciendo un MCP:

**Construir un servidor MCP en Python es mucho más fácil de lo que imaginas, especialmente si ya sabes escribir funciones y herramientas (** *tools* **) en Python.**^^La forma estándar y más limpia hoy en día es utilizando **FastMCP** (la abstracción de alto nivel del SDK oficial de MCP).

Aquí tienes un ejemplo práctico paso a paso de cómo crear un servidor MCP en Python y cómo conectarlo directamente a VS Code para que Copilot lo utilice.

### Paso 1: Crear el Servidor MCP en Python

**Primero, instala la librería en tu entorno virtual:**

```
pip install fastmcp
```

Luego, crea un archivo llamado `server.py`. En este script definirás tus herramientas usando decoradores. FastMCP se encarga automáticamente de leer los tipos de datos y los *docstrings* para explicarle al LLM cómo usarlas:

```Python
# server.py
from fastmcp import FastMCP

# 1. Inicializamos el servidor MCP
mcp = FastMCP("MiAgentePythonMCP")

# 2. Definimos una herramienta (igual que harías en LangChain)
@mcp.tool()
def calcular_metricas_ventas(producto: str, meses: int) -> str:
    """Calcula las métricas de ventas simuladas para un producto dado un número de meses."""
    # Lógica de negocio de tu agente / base de datos / API
    volumen_estimado = meses * 1250
    return f"El producto '{producto}' generó un estimado de {volumen_estimado} unidades en los últimos {meses} meses."

@mcp.tool()
def buscar_en_documentacion_interna(termino: str) -> str:
    """Busca en la base de conocimientos interna de la empresa."""
    return f"Resultado simulado para '{termino}': Las políticas de despliegue requieren aprobación previa en staging."

# 3. Ejecutamos el servidor (por defecto usa transporte STDIO, ideal para IDEs)
if __name__ == "__main__":
    mcp.run()
```

### Paso 2: Conectar tu Servidor Python a VS Code (GitHub Copilot)

Para que Copilot pueda invocar las funciones que acabas de escribir en Python, debes registrar el script en la configuración de VS Code.

1. Abre la paleta de comandos de VS Code (`Ctrl+Shift+P` o `Cmd+Shift+P`).
2. Escribe y selecciona **Preferences: Open User Settings (JSON)** (o busca la configuración de servidores MCP de Copilot).
3. Añade la configuración de tu servidor local apuntando al intérprete de Python de tu entorno y a la ruta absoluta de tu archivo `server.py`:

```JSON
"github.copilot.chat.mcpServers": {
  "agente-python-local": {
    "command": "python",
    "args": ["/ruta/completa/a/tu/proyecto/server.py"]
  }
}
```

### Paso 3: Usarlo en el Chat de Copilot

Una vez guardada la configuración y reiniciado VS Code:

1. Abre el panel de **GitHub Copilot Chat** en modo agente.
2. Al iniciar, Copilot se comunicará de forma silenciosa e invisible con tu script de Python (`server.py`) a través de la entrada/salida estándar ( *stdio* ) para **descubrir automáticamente** tus herramientas (`calcular_metricas_ventas` y `buscar_en_documentacion_interna`).
3. Ahora puedes pedirle directamente en el chat:
   > *"Oye, usa la herramienta de métricas para calcular las ventas de 'SaaS Enterprise' durante 6 meses."*^^
   >

Copilot interpretará la orden, decidirá invocar tu función escrita en Python, recibirá el resultado que programaste y te mostrará la respuesta integrada en el editor.

## Conectando un agente gemini a vscode

**Puedes lograr exactamente ese flujo (leer tu proyecto en VS Code y escribir código con Gemini), pero no "enganchando" Gemini directamente por dentro de GitHub Copilot de forma nativa** , sino usando la arquitectura adecuada para ello.

Para entender por qué y cómo hacerlo, hay que separar el **modelo** (Google Gemini) de la **interfaz de desarrollo** (VS Code y los editores de código).

## 1. ¿Se puede usar el LLM de Google dentro de GitHub Copilot?

**GitHub Copilot** está fuertemente acoplado al ecosistema de modelos de OpenAI (GPT-4o, etc.) y Anthropic (según la configuración de GitHub).^^Aunque VS Code ha introducido de forma reciente opciones de *Custom Endpoints* (puntos de conexión personalizados para usar tus propias claves de modelos), el chat oficial de Copilot y sus características propietarias de indexación del workspace están diseñados para trabajar con sus modelos predeterminados.^^

Sin embargo, **no necesitas a Copilot para tener un Copilot propio con Gemini** .**Hoy en día existen extensiones y herramientas en VS Code creadas específicamente para esto.**^^

## 2. ¿Cómo montar tu propio "Copilot" con Gemini en VS Code?

Tienes dos caminos excelentes para conseguir que Gemini lea tu proyecto abierto y escriba código por ti en VS Code:

### Camino A: Usar extensiones de código abiertas orientadas a Agentes (La ruta más rápida)

**En lugar de forzar a GitHub Copilot a usar Gemini, puedes usar editores o extensiones de código modulares (como ****Roo Code** —anteriormente  *Roo Cline* **—, ** **Cline** **, o ** **Continue** **) que se instalan directamente en VS Code como paneles de chat laterales (igual que Copilot).**^^

1. Instalas la extensión (por ejemplo,**Continue** o  **Roo Code** ) en VS Code.
2. En la configuración de la extensión, seleccionas **Google Gemini** como proveedor de LLM e introduces tu clave de API de Google AI Studio (`GEMINI_API_KEY`).
3. **¿El resultado?** Obtienes un "Agente Copilot" propio donde:
   * El agente tiene acceso nativo al **Workspace** (lee todos los archivos de tu proyecto abierto en VS Code).
   * **Puede ejecutar comandos en tu terminal, buscar archivos y ****escribir código directamente en tus ficheros** mediante parches automáticos guiados por tus prompts.^^

### Camino B: Crear tu propio Agente en Python con LangGraph + MCP y conectarlo

Si lo que quieres es aplicar estrictamente lo que aprendiste en tu curso de LangChain y LangGraph:

1. Creas un agente en Python utilizando `ChatGoogleGenerativeAI` como tu LLM principal.
2. Le configuras **herramientas ( *tools* )** de lectura de archivos locales (`read_file`,`list_directory`,`write_file`) apuntando a la ruta de tu proyecto.
3. Lo levantas como un **Servidor MCP** (como vimos en el paso anterior).
4. Conectas ese servidor MCP a una interfaz de chat en VS Code compatible con MCP.**De esta forma, el agente impulsado por Gemini leerá tus archivos locales y te devolverá las modificaciones a través del protocolo estándar.**

## Configurar VS Code para usar Gemini:

Configurar **Continue** (o extensiones similares como Roo Code) en VS Code para usar **Google Gemini** como tu agente personal de programación es un proceso directo. Esta extensión actúa exactamente como un "Copilot privado", leyendo tu repositorio, indexando tu código y permitiéndote modificar archivos mediante  *prompts* .

Aquí tienes la guía paso a paso para montarlo:

### Paso 1: Instalar la extensión en VS Code

1. Abre tu  **VS Code** .
2. Ve al mercado de extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X`).
3. Busca e instala **Continue** (es una de las herramientas de código abierto más potentes para conectar cualquier LLM a tu editor).

### Paso 2: Obtener tu API Key de Google

1. Entra en [Google AI Studio](https://aistudio.google.com/).
2. Genera una clave de API ( *API Key* ) gratuita o de pago para usar el modelo más reciente (como **Gemini 1.5 Pro** o  **Gemini 2.5 Flash** , según prefieras velocidad o razonamiento profundo).

### Paso 3: Configurar Continue para usar Gemini

Una vez instalada la extensión, verás que aparece un icono de Continue en la barra lateral izquierda de VS Code.

1. Haz clic en el icono de Continue y abre su archivo de configuración (suele estar en tu directorio de usuario en `~/.continue/config.json`, o puedes editarlo directamente desde el engranaje de configuración de la extensión).
2. Modifica el archivo `config.json` para añadir a **Gemini** como tu modelo principal ( *models* ) y como el modelo de autocompletar (*tabAutocompleteModel* si lo deseas):

```JSON
{
  "models": [
    {
      "title": "Gemini 1.5 Pro",
      "provider": "gemini",
      "model": "gemini-1.5-pro-latest",
      "apiKey": "TU_API_KEY_DE_GOOGLE_AQUI"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Gemini Flash",
    "provider": "gemini",
    "model": "gemini-1.5-flash-latest",
    "apiKey": "TU_API_KEY_DE_GOOGLE_AQUI"
  }
}
```

### Paso 4: ¡A usar tu "Copilot" con Gemini!

Una vez guardado el archivo de configuración:

* **Chat lateral (`Ctrl+I` o `Cmd+I`):** Puedes chatear con Gemini preguntándole por la estructura de tu proyecto. Al escribir `@file` o `@codebase`, la extensión le inyectará el contexto de los archivos abiertos en VS Code para que Gemini los lea.
* **Edición en línea (`Ctrl+I` en el editor de código):** Selecciona un bloque de código en tu archivo, presiona el atajo de edición y pídele a Gemini que lo refactorice, añada tipos o cree pruebas unitarias. Gemini escribirá el código directamente en tu archivo, dándote la opción de aceptarlo o rechazarlo ( *diff view* ).
