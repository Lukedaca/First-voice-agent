# Hlasový Asistent s GUI 🎙️🤖

Jednoduchý hlasový asistent s textovým rozhraním, který odpovídá na dotazy z technické příručky. Podporuje **hlasový i textový vstup**.

---

## Instalace

### 1. Naklonujte repozitář
```bash
git clone https://github.com/vas-username/voice-assistant.git
cd voice-assistant
2. Nainstalujte závislosti
bash

pip install -r requirements.txt
3. Stáhněte Vosk model
Stáhněte český model: vosk-model-small-cs-0.4-rhasspy.zip

Rozbalte složku a přejmenujte ji na vosk-model-small-cs-0-4.

Přesuňte ji do kořenové složky projektu.

Použití
bash

python main.py
Funkce:
🟢 Start poslechu: Nahrává z mikrofonu.

🔴 Stop poslechu: Zastaví nahrávání.

📝 Textový vstup: Pište dotazy do pole a potvrďte Enter nebo tlačítkem.

Přizpůsobení
Vytvořte soubor data_manual.txt s vlastními odpověďmi (formát: jedna odpověď na řádek).
Příklad:


Pro reset zařízení podržte tlačítko Power.
Kontaktujte podporu na podpora@firma.cz.
Změňte rychlost řeči v main.py:

python
self.engine.setProperty("rate", 150)  # 150 = střední rychlost
Technologie
Rozpoznávání řeči: Vosk

Text-to-speech: pyttsx3

GUI: tkinter

Licence
MIT License. Více v LICENSE.

Problémy? Napište zde nebo kontaktujte lukas.drsticka@gmail.com



