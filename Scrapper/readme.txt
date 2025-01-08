########################################################
#                    Analizador de Cuentas de Instagram
########################################################

Este script utiliza la librería Instaloader para analizar cuentas de Instagram y calcular un puntaje de calidad basado en diferentes métricas. 
Proporciona información detallada sobre la actividad y calidad de un perfil, como el número de seguidores, engagement, uso de hashtags y frecuencia 
de publicación.

========================================================
                       Características
========================================================
- Analiza cuentas de Instagram basándose en las últimas 10 publicaciones.
- Calcula el puntaje de calidad del perfil (PCP) considerando:
  - Relación seguidores/seguidos.
  - Engagement.
  - Repetición de hashtags y leyendas.
  - Frecuencia de publicación.
  - Biografía del perfil.
- Clasifica el perfil como:
  - Sospechoso.
  - Calidad moderada.
  - Alta calidad.
- Interfaz de usuario mejorada con separadores y mensajes claros.

========================================================
                         Requisitos
========================================================
1. Python 3.7 o superior.
2. Librerías necesarias:
   - instaloader
   - collections
   - time
   - random

   Puedes instalar Instaloader ejecutando:
   pip install instaloader

========================================================
                   Instrucciones de Uso
========================================================
1. Clonar el repositorio o copiar el script.
2. Ejecutar el script utilizando el comando:
   python <nombre_del_archivo>.py
3. Seguir los pasos en pantalla:
   - Ingresa tu nombre de usuario y contraseña de Instagram para autenticarte (solo la primera vez).
   - Proporciona el nombre de usuario de la cuenta a analizar.
4. Resultados del análisis:
   - Verás métricas clave y el puntaje de calidad del perfil.
   - Una clasificación indicando la calidad del perfil.

========================================================
                    Estructura del Script
========================================================
1. Funciones principales:
   - calcular_puntaje_calidad: Calcula el puntaje de calidad del perfil basándose en varias métricas.
   - analizar_cuenta: Realiza el análisis del perfil y presenta los resultados.
2. Estilo visual:
   - Separadores (mostrar_separador) para mejorar la visualización de los datos.
   - Entrada de datos estilizada (entrada_usuario).

========================================================
                      Notas Importantes
========================================================
- El análisis se limita a las 10 publicaciones más recientes para evitar exceder los límites y obtener un bloqueo por parte de Instagram.
- Autenticación:
  - Es necesario proporcionar tus credenciales de Instagram para cargar perfiles privados.
  - La sesión se guarda localmente para evitar ingresar las credenciales repetidamente.
- Seguridad:
  - Asegúrate de usar este script en un entorno seguro para proteger tus credenciales.

========================================================
                        Advertencia
========================================================
El uso de herramientas como Instaloader puede estar sujeto a los términos y condiciones de Instagram. 
Úsalo únicamente para análisis personales y no para actividades ilícitas o no autorizadas.
Su uso es autorizado solamente con fines educativos y de investigacion.
