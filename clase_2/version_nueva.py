from openai import OpenAI
from env import API_KEY

client = OpenAI(api_key=API_KEY)

def generar_tarea_para_reunion(tipo_reunion):
  prompt = f"Genera una tarea pendiente para la reunión de {tipo_reunion}:"

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
      {
      "role": "user",
      "content": prompt
      }
    ],
    max_tokens=50
  )

  tarea_pendiente = response.choices[0].message.content

  return tarea_pendiente

if __name__ == "__main__":
  tipo_reunion = "cumpleaños"
  tarea_pendiente = generar_tarea_para_reunion(tipo_reunion)
  print(f"La tarea pendiente para la {tipo_reunion} es: {tarea_pendiente}")
  
