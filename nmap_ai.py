import os
import subprocess
from groq import Groq

api_key = input("groq api key: ").strip()
target = input("target: ").strip()

print("running nmap...")
proc = subprocess.run(
    ["nmap", "-p-", "-sS", "-O", "-T5", target],
    capture_output=True, text=True
)
nmap_out = proc.stdout

if not nmap_out.strip():
    print("nmap nothing returned, try sudo")
    exit(1)

client = Groq(api_key=api_key)

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"""
ты эксперт по пентесту. проанализируй вывод nmap и напиши отчет на русском.
цель: {target}

nmap output:
{nmap_out}

структура отчета:
1. краткое резюме
2. информация о цели
3. таблица открытых портов
4. анализ каждого сервиса
5. возможные риски
6. рекомендации
7. следующие шаги
8. итог

не придумывай cve и факты которых нет в выводе
"""
        }
    ],
    temperature=0.7,
    max_completion_tokens=1024,
    stream=True,
)

for chunk in completion:
    content = chunk.choices[0].delta.content or ""
    print(content, end="", flush=True)

print()
