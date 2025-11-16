# Eclipse Rendering – Python + ModernGL
Projekt realizowany w ramach kursu **Techniki Renderingu i Animacja Komputerowa**.  
Celem jest implementacja **fizycznie poprawnego renderingu zaćmień** w czasie rzeczywistym na podstawie artykułu:

**Physically Based Real-Time Rendering of Eclipses**  
https://cgvr.cs.uni-bremen.de/papers/cgf25/paper1037_CRC-1.pdf

---

## 🎯 Funkcjonalności (plan projektu)
- Rendering sceny 3D: **Słońce – Ziemia – Księżyc**
- Kamera 3D z możliwością ruchu
- Proceduralne generowanie sfer (bez modeli .obj)
- Shader obliczający:
  - stożek cienia (umbra)
  - półcień (penumbra)
  - modulację oświetlenia zgodnie z artykułem
- Prosty interfejs (GUI) do zmiany parametrów:
  - promienie ciał niebieskich,
  - odległości,
  - kierunek światła,
  - faza zaćmienia.
- Rendering w czasie rzeczywistym (ModernGL)
- Finalna animacja wideo

---

## 🧰 Wykorzystane technologie
- **Python 3.x**
- **ModernGL** – rendering OpenGL
- **moderngl-window** – obsługa okna i kamery
- **NumPy** – obliczenia matematyczne
- **Pillow** – wczytywanie tekstur
- **Pyrr / glm-python** – macierze i transformacje
- (opcjonalnie) **DearPyGui / ImGui** – GUI

---

## 📦 Instalacja
```bash
pip install moderngl moderngl-window numpy pillow pyrr
