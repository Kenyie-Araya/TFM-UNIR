import instaloader
import time
import random
from collections import Counter

def calcular_puntaje_calidad(profile, engagement_score, repeated_captions, repeated_hashtags, post_dates):
    """
    Calcula un puntaje de calidad basado en múltiples factores del perfil.
    """
    puntaje = 100  # Puntaje inicial

    # Proporción seguidores/seguidos
    if profile.followers > 0 and profile.followees > 0:
        ratio_followers_followees = profile.followers / profile.followees
        if ratio_followers_followees < 0.5:
            puntaje -= 15  # Relación baja seguidores/seguidos
        elif ratio_followers_followees < 1:
            puntaje -= 10
    else:
        puntaje -= 20  # Sin seguidores o seguidos

    # Calculo de Engagement
    if engagement_score < 1:
        puntaje -= 20  # Muy bajo engagement
    elif engagement_score < 3:
        puntaje -= 10  # Engagement moderado

    # Repetición de leyendas
    if repeated_captions > 0:
        puntaje -= 5

    # Exceso de hashtags repetidos
    if len(repeated_hashtags) > 3:
        puntaje -= 5

    # Frecuencia de publicación
    if len(post_dates) > 1:
        differences = [abs((post_dates[i] - post_dates[i + 1]).days) for i in range(len(post_dates) - 1)]
        avg_frequency = sum(differences) / len(differences)
        if avg_frequency > 30:
            puntaje -= 10  # Baja frecuencia de publicación
    else:
        puntaje -= 15  # Muy pocas publicaciones recientes

    # Diversidad de hashtags
    if len(set(repeated_hashtags)) < 5:
        puntaje -= 5

    # Biografía
    if not profile.biography:
        puntaje -= 5

    return max(puntaje, 0)

def mostrar_separador():
    print("\n" + "=" * 50 + "\n")

def entrada_usuario(prompt):
    print("-" * 50)
    return input(f"{prompt}\n>>> ").strip()

def analizar_cuenta(username):
    """
    Analiza la cuenta de Instagram y recopila datos sobre publicaciones,
    hashtags, leyendas repetidas y engagement.
    """
    # Inicializar Instaloader
    L = instaloader.Instaloader()

    # Intentar cargar sesión existente
    try:
        L.load_session_from_file("mi_usuario")
    except FileNotFoundError:
        username_input = entrada_usuario("Ingresa tu nombre de usuario de Instagram")
        password_input = entrada_usuario("Ingresa tu contraseña de Instagram")
        L.login(username_input, password_input)  # Iniciar sesión
        L.save_session_to_file()  # Guardar sesión

    try:
        # Cargar el perfil
        profile = instaloader.Profile.from_username(L.context, username)

        mostrar_separador()
        print(f"Analizando la cuenta: {username}")
        print(f"Seguidores: {profile.followers}")
        print(f"Seguidos: {profile.followees}")
        print(f"Publicaciones: {profile.mediacount}")
        print(f"Biografía: {profile.biography or 'No disponible'}")
        mostrar_separador()

        # Variables para análisis
        hashtags = []
        captions = []
        total_likes = 0
        total_comments = 0
        post_dates = []

        # Limitar el análisis a las primeras 10 publicaciones
        print("Analizando publicaciones...\n")
        for i, post in enumerate(profile.get_posts()):
            if i >= 10:
                break  # Limitar a 10 publicaciones

            # Recolectar datos
            hashtags.extend(post.caption_hashtags)
            captions.append(post.caption or "")
            total_likes += post.likes
            total_comments += post.comments
            post_dates.append(post.date)

            # Pausa aleatoria para evitar bloqueos
            time.sleep(random.uniform(2, 5))

        # Análisis de hashtags
        hashtag_counter = Counter(hashtags)
        repeated_hashtags = [tag for tag, count in hashtag_counter.items() if count > 1]

        # Análisis de leyendas repetidas
        repeated_captions = len(captions) - len(set(captions))

        # Promedio de interacciones
        promedio_likes = total_likes / 10 if total_likes > 0 else 0
        promedio_comments = total_comments / 10 if total_comments > 0 else 0

        # Puntuación de engagement
        engagement_score = (promedio_likes + promedio_comments) / profile.followers * 100 if profile.followers > 0 else 0

        # Calcular el Puntaje de Calidad del Perfil (PCP)
        pcp = calcular_puntaje_calidad(profile, engagement_score, repeated_captions, repeated_hashtags, post_dates)

        # Mostrar resultados
        mostrar_separador()
        print("Resultados del análisis:")
        print(f"Hashtags utilizados: {len(hashtags)}")
        print(f"Hashtags repetidos: {', '.join(repeated_hashtags) if repeated_hashtags else 'Ninguno'}")
        print(f"Leyendas repetidas: {repeated_captions}")
        print(f"Promedio de likes por publicación: {promedio_likes:.2f}")
        print(f"Promedio de comentarios por publicación: {promedio_comments:.2f}")
        print(f"Puntuación de engagement: {engagement_score:.2f}%")
        print(f"\nPuntaje de Calidad del Perfil (PCP): {pcp}/100")
        mostrar_separador()

        # Clasificación del perfil
        if pcp < 50:
            print("La cuenta presenta características sospechosas.")
        elif pcp < 80:
            print("La cuenta tiene calidad moderada.")
        else:
            print("La cuenta parece legítima y de alta calidad.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"La cuenta '{username}' no existe.")
    except Exception as e:
        print(f"Error al analizar la cuenta: {e}")

if __name__ == "__main__":
    mostrar_separador()
    print("Bienvenido al analizador de cuentas de Instagram")
    mostrar_separador()
    username = entrada_usuario("Ingrese el nombre de usuario de Instagram a analizar")
    if username:
        analizar_cuenta(username)
    else:
        print("No se ingresó un nombre de usuario válido.")
