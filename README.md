# Spotify Playlist Creator

Este proyecto permite crear listas de reproducción en Spotify mediante un script de Python. El usuario puede ingresar una lista de canciones y artistas en el formato "artista - canción", y el script buscará esas canciones en Spotify, creará una lista de reproducción, y agregará las canciones encontradas.

## Características

- Crear listas de reproducción públicas o privadas en Spotify.
- Buscar canciones en Spotify mediante el nombre del artista y la canción.
- Agregar canciones a la lista de reproducción a partir de un formato específico: "artista - canción".
- Permite pegar varias canciones en una sola entrada, separadas por saltos de línea o comas.
- Soporta autenticación con la API de Spotify mediante OAuth.

## Requisitos

- Python 3.6 o superior.
- Biblioteca `spotipy` para interactuar con la API de Spotify.
- Una cuenta de Spotify y un "Client ID" y "Client Secret" configurados en el [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

## Instalación

### Paso 1: Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

bash
git clone https://github.com/tu-usuario/spotify-playlist-creator.git
cd spotify-playlist-creator

### Paso 2: Crear un entorno virtual (opcional pero recomendado)
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:

python -m venv venv

### Paso 3: Activar el entorno virtual
En Windows: 

venv\Scripts\activate

En macOS o Linux:

source venv/bin/activate

### Paso 4: Instalar las dependencias
Instala la biblioteca spotipy utilizando pip:

pip install spotipy

### Paso 5: Configuración de las credenciales de Spotify
Para poder usar el script, necesitas configurar tu "Client ID" y "Client Secret" de Spotify:

Dirígete al Spotify Developer Dashboard.
Crea una nueva aplicación y toma nota de tu "Client ID" y "Client Secret".
Modifica el archivo spotify_playlist_creator.py y reemplaza las variables CLIENT_ID y CLIENT_SECRET con los valores obtenidos.

CLIENT_ID = 'TU_CLIENT_ID'
CLIENT_SECRET = 'TU_CLIENT_SECRET'

### Paso 6: Ejecutar el script
Para ejecutar el script, simplemente corre el siguiente comando:

python spotify_playlist_creator.py

### Paso 7: Autenticación con Spotify
Al ejecutar el script por primera vez, se abrirá una ventana de navegador para que te autentiques con tu cuenta de Spotify y concedas permisos al script.

Una vez autenticado, podrás empezar a crear listas de reproducción.

### Uso
Crear lista de reproducción: El script te pedirá que ingreses un nombre para la nueva lista de reproducción.
Ingresar canciones y artistas: Luego, podrás pegar una lista de canciones en el formato "artista - canción". Puedes pegar varias canciones separadas por saltos de línea o comas. Cuando termines, escribe FIN y presiona ENTER.
Verificación: El script buscará las canciones en Spotify, y agregará aquellas que encuentre a la lista de reproducción creada.
