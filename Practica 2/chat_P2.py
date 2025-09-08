#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############ Coincidencia exacta/similitud (difflib).
############ Si no hay "match" suficiente, pide aclaración y permite aprender una respuesta.
############ Base de conocimiento persistente en kb.json


import json
import os
import difflib

KB_FILE = os.path.join(os.path.dirname(__file__), "kb.json")

############################################################  Conocimiento (kb.json. Si existe)
INITIAL_KB = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy muy bien, gracias. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de tecnología, música o lo que tú quieras."
}

EXIT_WORDS = {"salir", "adios", "adiós", "chao", "bye"}

def normalize(text: str) -> str:
    return " ".join(text.strip().lower().replace("¿","").replace("?","").replace("¡","").replace("!","").split())

def load_kb() -> dict:
    kb = {}
    if os.path.exists(KB_FILE):
        try:
            with open(KB_FILE, "r", encoding="utf-8") as f:
                kb = json.load(f)
        except Exception:
            kb = {}
    ################################################Fusionar sin pisar intencionalmente lo ya guardado
    for k, v in INITIAL_KB.items():
        kb.setdefault(k, v)
    return kb

def save_kb(kb: dict) -> None:
    with open(KB_FILE, "w", encoding="utf-8") as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)

def best_match(kb_keys, query, cutoff=0.8):
    """Devuelve la mejor coincidencia por similitud o None."""
    matches = difflib.get_close_matches(query, kb_keys, n=1, cutoff=cutoff)
    return matches[0] if matches else None

def main():
    print("Asistente: Hola holaaa. Escribe algo (o 'salir' para terminar).")
    kb = load_kb()
    save_kb(kb)  ############################################################ asegurar que exista kb.json al comenzar

    while True:
        try:
            user = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAsistente: ¡Hasta luego!")
            break

        if not user:
            continue

        if normalize(user) in EXIT_WORDS:
            print("Asistente: ¡Hasta luego! 👋")
            break

        q = normalize(user)

        ################################################  1) Coincidencia exacta
        if q in kb:
            print("Asistente:", kb[q])
            continue

        ################################################  2) Coincidencia aproximada
        approx = best_match(list(kb.keys()), q, cutoff=0.82)
        if approx:
            print("Asistente:", kb[approx])
            continue

       ################################################  3) No se encontró match: pedir aclaración y aprender
       
        print("Asistente: Disculpe, no le entendí. ¿Podría repetir lo que dijo?")
        print("Asistente: Si desea, indíqueme qué debería responder a: «%s»" % user)
        teach = input("Enséñame la respuesta (o deje vacío para omitir): ").strip()

        if teach:
            kb[q] = teach
            try:
                save_kb(kb)
                print("Asistente: ¡Gracias! He aprendido algo nuevo.")
            except Exception as e:
                print("Asistente: Hubo un problema al guardar lo aprendido:", e)
        else:
            print("Asistente: Entendido, continuemos.")

if __name__ == "__main__":
    main()
