# CaffeinaMetrics: Sistema de Gestión de Cafetería de Especialidad

CaffeinaMetrics es una plataforma web para entusiastas del café de especialidad que buscan llevar un control técnico y detallado de sus extracciones. Permite registrar variables críticas como el origen del grano, el método de preparación, el ratio de extracción y el puntaje de catación.

## 🚀 Información del Sistema
El proyecto está desarrollado con las siguientes tecnologías:
* **Lenguaje:** Python 3.9+
* **Framework Web:** Flask
* **ORM:** SQLAlchemy
* **Gestión de Seguridad y UI:** Flask-AppBuilder (FAB)
* **Base de Datos:** MySQL
* **Visualización:** Gráficas dinámicas integradas con FAB

## 🛠️ Requisitos Previos
* Servidor MySQL en ejecución.
* Base de datos llamada `cafeteria` creada:
  ```sql
  CREATE DATABASE cafeteria;
  ```

## 📦 Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd cafeteria
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos:**
   Edita el archivo `config.py` y asegúrate de que la variable `SQLALCHEMY_DATABASE_URI` apunte a tu instancia de MySQL:
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<usuario>:<password>@localhost/cafeteria'
   ```

5. **Inicializar la Base de Datos y el Administrador:**
   ```bash
   export FLASK_APP=run.py
   flask fab create-db
   flask fab create-admin
   ```

## ⚡ Ejecución
Para iniciar el servidor de desarrollo, simplemente ejecuta:
```bash
python3 run.py
```
El sistema estará disponible en `http://localhost:8080/`.

## 🧪 Pruebas Unitarias
El proyecto incluye pruebas para validar los modelos y relaciones:
```bash
python3 -m unittest tests/test_models.py
```

## 📝 Notas de Seguridad
Debido a compatibilidad con versiones específicas de OpenSSL/LibreSSL, el sistema utiliza un `CustomSecurityManager` que implementa hashing mediante `pbkdf2:sha256` para garantizar un inicio de sesión funcional en cualquier entorno.
