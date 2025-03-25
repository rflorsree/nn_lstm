# Predicción del siguiente número con RNN (LSTM)

Este codigo muestra como usar una **Red Neuronal Recurrente (RNN)** con una arquitectura **LSTM** para predecir el **siguiente número en una secuencia**.

---

## Requisitos

- Python 3.7+
- TensorFlow
- NumPy

---
## Arquitectura del modelo .

1. **Capa LSTM (Long Short-Term Memory)**
   - 32 Neuronas
   - Secuencias de 3 pasos de tiempo, con 1 característica por paso (input_shape=(3, 1))..


2. **Capa Densa**
   - Capa de salida del modelo.
   - Devuelve un único valor como resultado final.
   - Se puede usar para regresión o clasificacion binaria.



Referencias:

-LSTM layer. (2024, junio). TensorFlow. https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM

-Sotelo, J. A. L. (2023, 144). Deep Learning: teoría y aplicaciones. Marcombo.
