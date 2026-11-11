# Método de Falsa Posición (Regula Falsi)

Proyecto educativo e interactivo para aprender, aplicar y practicar el **método numérico de Falsa Posición**, también conocido como *Regula Falsi*. El proyecto integra una página web explicativa, una calculadora del método, un juego educativo y una implementación del algoritmo en Python.

## Objetivo

Explicar el funcionamiento del método de Falsa Posición y mostrar cómo se utiliza para aproximar raíces reales de funciones continuas en un intervalo donde existe un cambio de signo. El proyecto contextualiza el método mediante un ejemplo relacionado con la optimización de recursos en infraestructura Cloud.

## Contenido del proyecto

| Archivo | Descripción |
|---|---|
| `index.html` | Sitio web principal: introducción, fundamentos teóricos, fórmula, ejemplo aplicado y calculadora interactiva. |
| `juego.html` | Juego educativo con cuatro niveles para reforzar los conceptos y el procedimiento del método. |
| `falsaposicion.py` | Implementación del algoritmo de Falsa Posición en Python. |
| `test_falsaposicion.py` | Pruebas unitarias para validar el algoritmo y algunos casos límite. |
| `manifest.json` | Manifiesto de la aplicación web. |
| `service-worker.js` | Archivo de soporte para las funciones de aplicación web progresiva (PWA). |

## Fundamento matemático

El método requiere una función continua en el intervalo \([a,b]\) y valores en los extremos con signos opuestos:

\[
f(a)\cdot f(b)<0
\]

La aproximación de la raíz se calcula mediante:

\[
x_r=\frac{a f(b)-b f(a)}{f(b)-f(a)}
\]

Después de calcular \(x_r\), se evalúa \(f(x_r)\) y se actualiza uno de los extremos del intervalo, conservando el cambio de signo. El proceso se repite hasta cumplir el criterio de tolerancia o alcanzar el máximo de iteraciones.

## Ejemplo incluido

El caso principal del proyecto utiliza la función:

\[
f(x)=x^3-3x-1
\]

con el intervalo inicial \([1,2]\) y una tolerancia de error relativo porcentual de \(0.05\%\).

La implementación de Python incluye este ejemplo y pruebas que verifican el resultado aproximado, la detección de intervalos sin cambio de signo, una raíz exacta en un extremo y un intervalo inválido.

## Tecnologías utilizadas

- **HTML5** para la estructura de las páginas.
- **CSS** y **Tailwind CSS** para los estilos y el diseño adaptable.
- **JavaScript** para la interacción de la calculadora y el juego.
- **MathJax** para mostrar las expresiones matemáticas y fórmulas.
- **Chart.js** para la visualización gráfica.
- **Python 3** para la implementación del algoritmo y sus pruebas.
- **unittest** para las pruebas automatizadas.

> Nota: la página web carga Tailwind CSS, MathJax y Chart.js desde servicios CDN. Por ello, se necesita conexión a Internet para que esos recursos externos se visualicen correctamente.

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Reemplaza `URL_DEL_REPOSITORIO` por la dirección HTTPS o SSH de tu repositorio en GitHub.

### 2. Abrir el sitio web

Abre el archivo `index.html` en un navegador moderno. Desde la página principal puedes acceder al juego educativo y a la calculadora.

No se necesita instalar dependencias de Python para utilizar la versión web.

### 3. Ejecutar el algoritmo en Python

Se requiere Python 3.8 o superior. Desde la carpeta del proyecto, ejecuta:

```bash
python falsaposicion.py
```

### 4. Ejecutar las pruebas

```bash
python -m unittest -v test_falsaposicion.py
```

Las pruebas comprueban el caso principal y diferentes condiciones de validación del algoritmo.

## Publicar en GitHub Pages

Si deseas publicar la página web para que pueda consultarse desde Internet:

1. Sube los archivos del proyecto a un repositorio de GitHub.
2. Entra en **Settings** del repositorio.
3. Abre la sección **Pages**.
4. En **Build and deployment**, selecciona **Deploy from a branch**.
5. Selecciona la rama principal (por ejemplo, `main`) y la carpeta raíz (`/root`).
6. Guarda los cambios y espera a que GitHub Pages publique el sitio.

El archivo `index.html` está en la raíz del proyecto, por lo que funciona como página de entrada. El juego se encuentra en `juego.html`.

## Estructura del repositorio

```text
Proyecto-Falsa_posición/
├── index.html
├── juego.html
├── falsaposicion.py
├── test_falsaposicion.py
├── manifest.json
├── service-worker.js
└── README.md
```

## Contexto académico

**Universidad de Santander (UDES)**  
**Programa:** Ingeniería de Software  
**Asignatura:** Métodos Numéricos  
**Autores:**
- David Alejandro Martínez Peralta - 01240371057
- Danilo Andrés Mattos Rodríguez - 01240372021
- Valery Montes Echavez - 01240372023

Proyecto académico desarrollado con fines educativos para estudiar y aplicar el método de Falsa Posición.

