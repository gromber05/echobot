## Ciclo de vida del dato (5b)

### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
En mi proyecto, los datos siguen un ciclo de vida estructurado:
1. **Generación**: Los datos se toman a partir de los mensajes enviados en discord
2. **Almacenamiento**: Se guardan temporalmente los datos de manera temporal mientras se ejecuta la función
3. **Procesamiento**: Se pasan los datos a la IA mediante el token para generar el mensaje.
4. **Distribución**: Se envía el mensaje al mismo canal de texto en Discord al cuál se ha realizado la petición.
5. **Archivado/Eliminación**: Como los datos se guardan de manera temporal, al finalizar, todos los datos se borran.

### ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
- El uso de datos temporales para que se realicen un borrado de datos al terminar de tratar con ellos.

### Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
Una lista interna que los almacene mientras no los estoy utilizando.

---

## Almacenamiento en la nube (5f)

### Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?
- Mi software podría hostearse entero en en la consola, y podría garantizar la seguridad cifrando los datos a la hora de realizar las peticiones a la IA.

### ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?
- Mis datos se almacenan de forma temporal, con lo cuál no he usado ninguna base de datos para almacenar dicha información

### Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
- Podría usar la nube para hostear el bot sin tener que tenerlo hosteado en local y esté constantemente en funcionamiento.

---

## Seguridad y regulación (5i)

### ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
- He usado varios "token" para realizar vinculaciones con la API como es Discord API o la API de Groq para usar el modelo "Llama" proveniente de la plataforma "Groq" usando claves cifradas para las llamadas al modelo de lenguaje que he escogido.

### ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
- **GDPR**: Se implementan controles de acceso, derecho al olvido y consentimiento explícito.

### Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
Los principales riesgos incluyen brechas de datos y accesos no autorizados. Se podría manejar con un manejo seguro de autenticación a la hora de acceder a las configuraciones del bot.

---

## Implicación de las THD en negocio y planta (2e)

### ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?
Podría mejorar la eficiencia de escritores buscando otras maneras de escribir algo y/o resumiendo algún artículo.

### ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
- Podría mejorar los procesos concretando más los "prompts" de las búsquedas y/o buscando otras maneras de optimizar las peticiones que se le realizan al modelo de lenguaje.

### Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
Podrían 

---

## Mejoras en IT y OT (2f)

### ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?
- Mediante **APIs y protocolos estándar** para comunicación entre sistemas.
- Implementando **IIoT** (Internet Industrial de las Cosas) para conectar dispositivos industriales con sistemas IT.

### ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
- **Supervisión remota de equipos**.
- **Control de calidad automatizado** con algoritmos de análisis.
- **Mantenimiento predictivo** con aprendizaje automático.

### Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?
Se podría adaptar para gestionar **infraestructura en la nube**, permitiendo optimizar despliegues y escalabilidad.

---

## Tecnologías Habilitadoras Digitales (2g)

### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
- **Big Data** para procesamiento masivo de datos.
- **Inteligencia Artificial** para análisis predictivo.
- **Cloud Computing** para almacenamiento escalable.

### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
- Permiten una **mayor escalabilidad**.
- Mejoran la **automatización y análisis** de datos.
- Facilitan la **integración con otros sistemas**.

### Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?
Podría incorporar **Machine Learning** para mejorar la toma de decisiones y personalización de servicios.

