# ISS Tracker + Astronautas

## Descripción
Aplicación desarrollada en Python que consume APIs públicas para obtener:

- ubicación actual de la Estación Espacial Internacional (ISS)
- listado de astronautas actualmente en el espacio

La aplicación fue containerizada con Docker y automatizada mediante Jenkins.

---

## Stakeholder
Centro educativo de monitoreo espacial.

---

## Problema
Se requiere una herramienta simple que permita visualizar información espacial en tiempo real usando APIs públicas.

---

## Tecnologías utilizadas

- Python
- Requests
- Docker
- Git
- GitHub
- Jenkins

---

## APIs utilizadas

### ISS Current Location
http://api.open-notify.org/iss-now.json

### Astronauts in Space
http://api.open-notify.org/astros.json

---

## Ejecución local

```bash
python app.py