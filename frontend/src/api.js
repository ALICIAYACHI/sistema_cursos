// frontend/src/api.js
import axios from "axios";

// Detectar entorno
const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

// Usar API correcta según entorno
const API_URL = isLocal
  ? "http://127.0.0.1:8000/api/"
  : "https://sistema-cursos.onrender.com/api/";

// Crear instancia de Axios
export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Manejar subida de archivos (multipart/form-data)
export const apiMultipart = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "multipart/form-data",
  },
});
