"""
Motor Matemático Central - Método de Falsa Posición (Regula Falsi)
Proyecto de Aula: Optimización de Recursos en Infraestructura Cloud
Universidad de Santander (UDES)
"""

import math

def falsa_posicion(func_str, a, b, tol=0.0005, max_iter=100):
    """
    Ejecuta el método de la falsa posición para encontrar la raíz de una función f(x) en [a, b].
    Retorna la lista de iteraciones, el resultado final y el estado/mensaje.
    """
    # Compilar o evaluar funcion segura
    def f(x):
        # Entorno seguro para eval
        allowed_names = {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan, 
                           "exp": math.exp, "log": math.log, "sqrt": math.sqrt, "abs": abs, "__builtins__": {}}
        return eval(func_str, {"__builtins__": {}}, allowed_names)

    # Validaciones iniciales
    if a >= b:
        raise ValueError("El extremo izquierdo 'a' debe ser menor que el extremo derecho 'b'.")
    
    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función en los extremos: {e}")

    if math.isnan(fa) or math.isnan(fb) or math.isinf(fa) or math.isinf(fb):
        raise ValueError("La función no está definida o diverge en los extremos iniciales.")

    if fa == 0:
        return [{"iter": 0, "a": a, "b": b, "fa": fa, "fb": fb, "xr": a, "fxr": fa, "error": 0.0}], a, "Raíz exacta encontrada en el extremo a."
    if fb == 0:
        return [{"iter": 0, "a": a, "b": b, "fa": fa, "fb": fb, "xr": b, "fxr": fb, "error": 0.0}], b, "Raíz exacta encontrada en el extremo b."

    if fa * fb >= 0:
        raise ValueError(f"No hay cambio de signo en el intervalo [{a}, {b}]. f(a) = {fa}, f(b) = {fb}. f(a)*f(b) >= 0.")

    iterations = []
    xr_prev = None

    for i in range(1, max_iter + 1):
        # Fórmula de Falsa Posición
        # xr = b - (fb * (a - b)) / (fa - fb)  o  (a*fb - b*fa) / (fb - fa)
        denominator = fb - fa
        if abs(denominator) < 1e-15:
            raise ZeroDivisionError("Denominador demasiado cercano a cero (inestabilidad numérica).")

        xr = (a * fb - b * fa) / denominator
        
        try:
            fxr = f(xr)
        except Exception as e:
            raise ValueError(f"Error al evaluar f(xr) en xr = {xr}: {e}")

        # Cálculo del error relativo porcentual
        if xr_prev is not None and abs(xr) > 1e-15:
            error = abs((xr - xr_prev) / xr) * 100.0
        else:
            error = None  # No disponible en la primera iteración

        iterations.append({
            "iter": i,
            "a": a,
            "b": b,
            "fa": fa,
            "fb": fb,
            "xr": xr,
            "fxr": fxr,
            "error": error
        })

        # Comprobar raíz exacta
        if fxr == 0:
            return iterations, xr, "Raíz exacta encontrada."

        # Criterio de parada por error
        if error is not None and error <= tol:
            return iterations, xr, f"Criterio de parada alcanzado (Error relativo < {tol}%)."

        # Actualización de intervalo
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

        xr_prev = xr

    return iterations, xr_prev, "Se alcanzó el número máximo de iteraciones sin cumplir la tolerancia estricta."

if __name__ == "__main__":
    # Prueba con el caso del proyecto: f(x) = x^3 - 3x - 1 en [1, 2], tol = 0.05%
    func = "x**3 - 3*x - 1"
    iters, res, msg = falsa_posicion(func, 1.0, 2.0, tol=0.05, max_iter=20)
    print("Resultado:", res)
    print("Mensaje:", msg)
    for it in iters:
        err_str = f"{it['error']:.4f}%" if it['error'] is not None else "—"
        print(f"Iter {it['iter']}: a={it['a']:.6f}, b={it['b']:.6f}, xr={it['xr']:.6f}, f(xr)={it['fxr']:.6f}, Error={err_str}")
