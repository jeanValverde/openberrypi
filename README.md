# Aplicación de ChatGPT con interacción por comando de voz

Esta aplicación utiliza el API de ChatGPT de OpenAI para permitir la interacción con el modelo de lenguaje mediante comandos de voz en español.

## Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- openai
- speech_recognition
- gtts
- playsound
- cv2
- pyfiglet

Además, necesitarás tener una clave de API de OpenAI para utilizar el modelo de ChatGPT. Puedes obtener una clave de API en el sitio web de OpenAI.

## Instrucciones de ejecución

1. Clona este repositorio en tu máquina local o descarga los archivos en formato ZIP.

2. Abre el archivo `main.py` en tu editor de código preferido.

3. Configura la variable de entorno `OPENAI_API_KEY` con tu clave de API de OpenAI. Asegúrate de tenerla disponible en el entorno en el que ejecutarás la aplicación.

4. Coloca una imagen llamada `loading.png` en el mismo directorio que el archivo `main.py`. Esta imagen se mostrará mientras se espera la respuesta de ChatGPT.

5. Ejecuta el archivo `main.py` para iniciar la aplicación.

6. La aplicación te solicitará que digas un comando de voz. Habla claramente en español para que el reconocimiento de voz funcione correctamente.

7. Después de reconocer el comando de voz, la aplicación enviará la solicitud a ChatGPT y mostrará una imagen de "cargando".

8. Una vez que se reciba la respuesta de ChatGPT, se reproducirá en voz alta y se mostrará una animación de texto en la terminal.

9. La aplicación seguirá esperando nuevos comandos de voz hasta que la cierres.

## Notas

- Si encuentras problemas con el reconocimiento de voz, asegúrate de tener un micrófono configurado y funcional en tu dispositivo.

- Ten en cuenta que la biblioteca `pyfiglet` solo es compatible con fuentes de caracteres ASCII estándar, por lo que podría haber limitaciones en la animación del texto dependiendo de la respuesta generada por ChatGPT.



```sh
$ python main.py
Diga algo...
[Usuario]: Cuéntame un chiste por favor.
[La aplicación muestra una imagen de "cargando"...]
Reconociendo...
Comando de voz: cuéntame un chiste por favor.
Respuesta de ChatGPT: ¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.

[La respuesta se reproduce en voz alta y se muestra una animación de texto en la terminal]
 _______ _     _ _______ _     _ _______
 |_____| |_____| |______  \___/  |______
 |     | |     | |______ _/   \_ ______|

Diga algo...
```

```sh
$ python main.py
Diga algo...
[Usuario]: ¿Cuál es la capital de Francia?
[La aplicación muestra una imagen de "cargando"...]
Reconociendo...
Comando de voz: cuál es la capital de Francia.
Respuesta de ChatGPT: La capital de Francia es París.

[La respuesta se reproduce en voz alta y se muestra una animación de texto en la terminal]
  _____  _    _ _______ _     _ _______
 |_____]  \  /  |______  \___/  |______
 |       _\/_   |______ _/   \_ ______|

Diga algo...
```

