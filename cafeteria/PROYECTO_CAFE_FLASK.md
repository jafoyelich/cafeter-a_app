# CaffeinaMetrics: Sistema de Gestión de Cafetería de Especialidad

## 1. Descripción del Proyecto
CaffeinaMetrics es una plataforma web desarrollada para entusiastas del café de especialidad que buscan llevar un control técnico y detallado de sus extracciones. El sistema permite registrar variables críticas como el origen del grano, el método de preparación, el ratio de extracción y el puntaje de catación, facilitando el análisis de datos para mejorar la calidad de cada taza.

### Problemática que resuelve
La preparación de café de especialidad involucra múltiples variables (molienda, temperatura, tiempo, origen) que son difíciles de recordar o comparar sin un registro formal. Este sistema centraliza la información, permitiendo identificar qué combinaciones de grano y método producen los mejores resultados mediante estadísticas y gráficas dinámicas.

---

## 2. Requerimientos Técnicos
Para cumplir con los estándares del examen de Segundo Parcial, el proyecto utiliza las siguientes tecnologías:

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **ORM:** SQLAlchemy
* **Gestión de Seguridad y UI:** Flask-AppBuilder
* **Base de Datos:** SQLite (desarrollo)
* **Control de Versiones:** Git y GitHub

---

## 3. Arquitectura de la Base de Datos
El sistema implementa una base de datos relacional con 4 tablas principales, cumpliendo con el requisito de uso de `ForeignKey`, `relationship` y `back_populates`:

1.  **Origen:** Almacena los países o regiones productoras (ej: Bolivia, Etiopía).
2.  **Café:** Información del grano (nombre, tipo de tueste) vinculada a un **Origen** (Relación 1:N).
3.  **Método:** Catálogo de dispositivos de extracción (ej: V60, Flair Pro 2, Prensa Francesa).
4.  **Registro de Extracción:** Tabla central que vincula un **Café**, un **Método** y las variables técnicas (temperatura, ratio, puntaje). Incluye protección de vista para usuarios autenticados.

---

## 4. Funcionalidades Principales

### Autenticación y Seguridad
* **Módulo de Seguridad:** Implementado mediante Flask-AppBuilder.
* **Login/Logout:** Sistema de inicio de sesión funcional con roles de usuario.
* **Protección de Vistas:** Restricción de acceso a los módulos de registro y reportes para usuarios no autenticados.

### Gestión de Datos (CRUD)
* Operaciones completas de **Crear, Listar, Editar y Eliminar** en las cuatro tablas del sistema.

### Reportes y Analítica
* **Módulo de Reportes:** Consultas dinámicas basadas en conteos y agrupaciones de la base de datos.
* **Gráfica Dinámica:** Visualización (PieChart/BarChart) de la distribución de extracciones por método de preparación.

---

## 5. Metodología de Trabajo Colaborativo
A pesar de ser un desarrollo individual por motivos de disponibilidad laboral, el proyecto sigue estrictamente el flujo de trabajo en equipo mediante GitHub:

* **Flujo de Ramas (Git Flow):**
    * `setup/project`: Configuración inicial.
    * `feature/models`: Definición de la lógica de base de datos.
    * `feature/views`: Implementación de la interfaz y CRUDS.
    * `feature/reports`: Desarrollo de estadísticas y gráficas.
* **Gestión de Cambios:** Uso de **Pull Requests (PR)** para la integración de cada funcionalidad en la rama `main`, permitiendo una revisión de código estructurada.

---

## 6. Instalación y Despliegue
1.  Clonar el repositorio.
2.  Crear y activar un entorno virtual: `python -m venv venv`.
3.  Instalar dependencias: `pip install flask-appbuilder flask-sqlalchemy`.
4.  Inicializar base de datos y administrador:
    * `flask fab create-db`
    * `flask fab create-admin`
5.  Ejecutar la aplicación: `flask run`.

---
**Autor:** Marcos Telles Torres
**Fecha de Entrega:** 18 de mayo de 2026
