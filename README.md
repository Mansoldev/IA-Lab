# IA-Lab

Mi laboratorio de funcionalidades para la IA


## Configuración del proyecto:

.opencode/: configuración para opencode

.vscode/: configuracion para copilot en vscode, conecta herramientas al editor. Cómo quieres que se configure VS Code y qué herramientas pone a disposición de sus agentes.

.github/: instrucciones y personalización de copilot. Cómo quieres que trabaje Copilot.

| Archivo o carpeta                                | Para qué sirve                                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| `<span>.github/copilot-instructions.md</span>` | Explica las convenciones y arquitectura de todo el repositorio a Copilot.                    |
| `<span>.github/instructions/</span>`           | Instrucciones específicas para C#, Python, pruebas, etc.                                    |
| `<span>.github/skills/</span>`                 | Procedimientos reutilizables que Copilot puede consultar cuando los necesita.                |
| `<span>.github/agents/</span>`                 | Definiciones de agentes especializados para Copilot.                                         |
| `<span>.vscode/mcp.json</span>`                | Configura los servidores MCP que VSCode debe ofrecer a sus agentes.                          |
| `<span>.opencode/</span>`                      | Configuración específica de OpenCode, incluidos agentes, skills y otras personalizaciones. |
