// src/api.js
import axios from "axios";

// ✅ Detectar entorno automáticamente
const isLocal =
  window.location.hostname === "localhost" ||
  window.location.hostname === "127.0.0.1" ||
  window.location.hostname === ""; // algunos navegadores dev pueden dejarlo vacío

// ✅ URL base según el entorno
const API_URL = isLocal
  ? "http://127.0.0.1:8000/api/" // 🖥️ Backend local (Django corriendo en tu PC)
  : "https://sistema-cursos.onrender.com/api/"; // ☁️ Backend desplegado en Render

// ✅ Crear instancia Axios con configuración común
export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// ✅ Manejo global de errores opcional (útil para debug)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("❌ Error en la API:", error);
    return Promise.reject(error);
  }
);
