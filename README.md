# Echobot

Este es un bot de Discord desarrollado en Python que utiliza la API de Groq para realizar tareas como parafrasear y traducir texto. Está basado en `discord.py` y usa `dotenv` para manejar las credenciales de manera segura.

## 🚀 Características
- **Parafraseo de texto** usando un modelo de inteligencia artificial.
- **Traducción de texto al español**.
- **Comandos personalizables** con prefijo `?`.

## 📦 Requisitos

Antes de ejecutar el bot, asegúrate de tener instalados los siguientes requisitos:

- Python 3.8 o superior
- Un bot de Discord configurado y su token
- Una cuenta y clave API de [Groq](https://groq.com/)

## 🛠 Instalación

1. Clona este repositorio o descarga los archivos.

   ```sh
   git clone https://github.com/gromber05/echobot.git
   cd echobot
   ```

2. Instala las dependencias necesarias:

   ```sh
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno creando un archivo `.env` dentro de la carpeta `project/`:

   ```sh
   DISCORD_TOKEN=tu_token_aqui
   GROQ_API_KEY=tu_clave_api_aqui
   ```

## 🚀 Uso

Ejecuta el bot con el siguiente comando:

```sh
python bot.py
```

Una vez ejecutado, el bot estará activo y responderá a los siguientes comandos en Discord:

### 📌 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `?test <texto>` | Devuelve el texto ingresado para probar que el bot responde. |
| `?parafrasea <texto>` | Parafrasea el texto ingresado usando Groq. |
| `?traduce <texto>` | Traduce el texto ingresado al español. |

## 🛠 Troubleshooting

### `pip` no funciona
Si `pip` no es reconocido como un comando, intenta:
```sh
python -m ensurepip --default-pip
```

### Error de permisos en Windows
Si el bot no se ejecuta correctamente en Windows, intenta ejecutar el terminal como administrador.

### Groq no responde
- Asegúrate de que la API key de Groq es válida.
- Revisa los logs en la consola para posibles errores.

## 📝 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de modificarlo y mejorarlo! 🚀

