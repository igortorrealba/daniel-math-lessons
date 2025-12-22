# 🚀 CÓMO REANUDAR DESPUÉS DEL LÍMITE DE CRÉDITOS

## 🎯 COMANDO SIMPLE

Cuando los créditos se reinicien, en **LA MISMA VENTANA** de chat escribe:

```
resume
```

**Eso es todo.** Claude leerá `.claude_checkpoint.md` y continuará exactamente donde paró.

---

## 📋 COMANDOS ALTERNATIVOS

Si `resume` no funciona, prueba:

```
Continúa desde el checkpoint. Lee .claude_checkpoint.md y continúa con la próxima lección pendiente.
```

O más específico:

```
Lee el archivo C:\Users\igort\Documents\Claude Agency\00 - My Second Brain\02_AREAS\Personal Life\Daniel's Education\.claude_checkpoint.md y continúa desde donde paraste.
```

---

## 🔄 SI LA INTERFAZ SE BLOQUEA

**SITUACIÓN REAL:** La ventana se congela y no puedes escribir

**✅ LO QUE DEBES HACER:**

1. **Reinicia la computadora** si es necesario
2. **Abre NUEVA ventana** de Claude Code (no hay problema)
3. **Navega al directorio:**
   ```bash
   cd "C:\Users\igort\Documents\Claude Agency\00 - My Second Brain\02_AREAS\Personal Life\Daniel's Education"
   ```
4. **Escribe simplemente:**
   ```
   resume
   ```

**¿Por qué funciona?**
- ✅ Cada lección se commitea inmediatamente a Git
- ✅ Todo está en GitHub
- ✅ El checkpoint tiene el estado exacto
- ✅ No se pierde ningún progreso

**Alternativa si es ventana nueva:**
```
Lee .claude_checkpoint.md en "C:\Users\igort\Documents\Claude Agency\00 - My Second Brain\02_AREAS\Personal Life\Daniel's Education" y continúa el proyecto de matemáticas de Daniel
```

---

## 🔍 VERIFICAR PROGRESO

Para ver cuánto falta:

```
¿Cuántas lecciones faltan? Muestra el progreso actual.
```

Para ver qué archivo se está creando:

```
¿En qué estás trabajando ahora?
```

---

## 🛠️ EN CASO DE EMERGENCIA

Si algo sale mal y necesitas reiniciar completamente:

```
Ignora el checkpoint. Lee RESUME_INSTRUCTIONS.md y explícame la situación actual del proyecto.
```

---

## 📊 MONITOREAR CRÉDITOS

Claude te avisará cuando queden ~20,000 tokens:

```
⚠️ Quedán ~20,000 tokens. Voy a:
1. Guardar progreso en .claude_checkpoint.md
2. Hacer commit y push a GitHub
3. Actualizar el estado

Cuando se reinicien los créditos, escribe: resume
```

---

## ✅ EJEMPLO DE FLUJO

```
[Trabajando en lección 3...]

Claude: "⚠️ Límite de créditos alcanzado. Progreso guardado en .claude_checkpoint.md
         Estado: 3/11 lecciones completas (27%)
         Última completada: 20251221_02_RectaNumerica
         Cuando se reinicien, escribe: resume"

[Esperas 12:00 PM - créditos reiniciados]

Tú: "resume"

Claude: "✅ Checkpoint cargado. Continuando con lección 4/11: 20251221_03_ComparacionNumeros
         Creando App_ComparacionNumeros.html..."

[Continúa trabajando...]
```

---

*Creado: 2025-12-22*
*Para: Proyecto de Matemáticas de Daniel*
