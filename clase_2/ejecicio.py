from genericpath import isfile
from openai import OpenAI
from env import API_KEY
import os
import json

client = OpenAI(api_key=API_KEY)

def generar_tarea_para_evento(tipo_evento):
  prompt = f"Genera sólo una tarea pendiente para el evento de {tipo_evento}"

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ]
  )

  tarea_pendiente = response.choices[0].message.content
  
  return tarea_pendiente

if __name__ == "__main__":
  tipo_evento = input("Ingresa el tipo de evento: ")
  tarea_pendiente = generar_tarea_para_evento(tipo_evento)

  print(f"La tarea pendiente para el evento de {tipo_evento} es: {tarea_pendiente}") 

  archivo = "tareas_pendientes.json"

  # Creamos el archivo sino existe
  if os.path.isfile(archivo) == False:
    with open(archivo, "w+") as f:
      json.dump([], f, indent=2, ensure_ascii=False)
  

  # Abrimos el archivo para modificarlo
  with open(archivo, "r+", encoding="utf-8") as f:

    tareas = f.read()

    if len(tareas) != 0:
      tareas = json.loads(tareas)
    else:
      tareas = []

    tarea = {
      "tipo_evento": tipo_evento,
      "tarea_pendiente": tarea_pendiente
    }

    tareas.append(tarea)

    f.seek(0)
    f.truncate()
    json.dump(tareas, f, indent=2, ensure_ascii=False)