// src/api.js
import axios from "axios";

// ✅ Detectar si estamos en desarrollo o producción
const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

// ✅ Usa tu API de Render en producción
const API_URL = isLocal
  ? "http://127.0.0.1:8000/api/"
  : "https://sistema-cursos.onrender.com/api/";

export const api = axios.create({
  baseURL: API_URL,
});
