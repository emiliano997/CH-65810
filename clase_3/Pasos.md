# Usar AutoGPT

Pasos con Docker Compose 0. Tener docker desktop instalado

1. Crea un archivo docker-compose.yml
2. Copiar el archivo .env.template y renombrarlo como .env
3. Ejecutar el siguiente comando: docker pull significantgravitas/auto-gpt
4. Instalamos streamlit (Opcional)
5. docker compose run --rm auto-gpt

# Propmts

Quiero generar un script en python que trabaje con streamlit, el script se llamara streamlit_N.py y le permitira al usuario ingresar un numero natural a traves de un input_text y mostra a la salida un numero que sea el doble del que se introdujo a la entrada. El mensaje de salida debe hacerse con un st.write
