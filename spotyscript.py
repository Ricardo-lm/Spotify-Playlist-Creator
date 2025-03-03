import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 🔹 Configura tus credenciales de Spotify
CLIENT_ID = 'TU_CLIENT_ID'
CLIENT_SECRET = 'TU_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-modify-public playlist-modify-private'

# 🔹 Autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def solicitar_canciones():
    print("🔹 Ingresa las canciones en el formato: 'artista - canción'.")
    print("🔹 Puedes pegar todas las canciones a la vez separadas por saltos de línea o comas.")
    print("🔹 Cuando termines, escribe 'FIN' y presiona ENTER.\n")
    
    canciones = []
    while True:
        entrada = input("➤ Pega todas las canciones y artistas: ")
        if entrada.strip().upper() == "FIN":
            break
        if entrada.strip():
            # Separar por salto de línea primero
            canciones_lista = entrada.splitlines()  # Separar por salto de línea

            if not canciones_lista:
                # Si no hay saltos de línea, separar por coma
                canciones_lista = entrada.split(",")  

            for item in canciones_lista:
                item = item.strip()
                if " - " in item:  # Verifica si el formato es correcto
                    partes = item.split(" - ")
                    if len(partes) == 2:
                        canciones.append((partes[1].strip(), partes[0].strip()))  # Ahora el orden correcto: (canción, artista)
                    else:
                        print("⚠️ Formato incorrecto. Usa: 'artista - canción'. Intenta de nuevo.")
                    
    return canciones

def crear_lista_reproduccion(nombre_lista, canciones):
    # Obtener el ID del usuario
    user_id = sp.current_user()['id']
    
    # Crear la lista de reproducción
    playlist = sp.user_playlist_create(user_id, nombre_lista, public=True)
    print(f"\n✅ Lista de reproducción '{nombre_lista}' creada.")

    # Buscar canciones y obtener sus IDs
    track_ids = []
    for cancion, artista in canciones:
        result = sp.search(q=f"track:{cancion} artist:{artista}", type="track", limit=1)
        tracks = result['tracks']['items']
        if tracks:
            track_ids.append(tracks[0]['id'])
        else:
            print(f"⚠️ No se encontró la canción: {cancion} - {artista}")

    # Agregar canciones a la lista de reproducción
    if track_ids:
        sp.playlist_add_items(playlist['id'], track_ids)
        print(f"🎵 {len(track_ids)} canciones añadidas a la lista.")

# 🔹 Pedir el nombre de la playlist
nombre_lista = input("\n📌 Ingresa el nombre de la nueva lista de reproducción: ")

# 🔹 Pedir canciones y artistas
canciones_y_artistas = solicitar_canciones()

# 🔹 Crear la lista de reproducción
crear_lista_reproduccion(nombre_lista, canciones_y_artistas)
