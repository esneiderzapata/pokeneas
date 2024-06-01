## Explicación de Uso Local

1. **Para correr el programa**:
    - Asegurate de tener Docker correctamente instalado en tu maquina
    - Luego, ejecuta el siguiente comando para crear una imagen: `docker build -t pokeneas-image .`.
    - Finalmente, ejecuta el contenedor en el puerto HTTP por defecto: `docker run -p 80:80 pokeneas-image`.     

2. **Para ver la imagen y frase de un Pokémon**:
    - Abre tu navegador web y navega a la siguiente URL: `http://127.0.0.1:5000/pokeneas`.
    - Verás una página HTML con la imagen del Pokémon, su nombre, una frase y el ID del contenedor del servidor.

3. **Para obtener la información de un Pokémon en JSON**:
    - Abre tu navegador web y navega a la siguiente URL: `http://127.0.0.1:5000/pokeneas/json`.
    - Verás una respuesta JSON con la información del Pokémon aleatorio.
