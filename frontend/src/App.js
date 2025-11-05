// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import FacultadList from "./components/FacultadList";
import CursoList from "./components/CursoList";
import "bootstrap/dist/css/bootstrap.min.css";

function Home() {
  return (
    <div className="text-center mt-5">
      <div className="card shadow-lg border-0 mx-auto" style={{ maxWidth: "600px" }}>
        <div className="card-body p-4">
          <img
            src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png"
            alt="Logo Cursos"
            width="120"
            className="mb-3"
          />
          <h2 className="card-title mb-3 text-primary fw-bold">
            Sistema de Cursos Universitarios
          </h2>
          <p className="card-text text-secondary mb-4">
            Administra fácilmente las facultades y cursos de tu universidad.
            Puedes crear, editar o eliminar registros desde el menú superior.
          </p>
          <div className="d-flex justify-content-center gap-3">
            <Link to="/facultades" className="btn btn-outline-primary">
              🎓 Ver Facultades
            </Link>
            <Link to="/cursos" className="btn btn-primary">
              📘 Ver Cursos
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="container mt-4">
        {/* Navbar */}
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary rounded mb-4 shadow">
          <div className="container-fluid">
            <Link className="navbar-brand fw-bold" to="/">
              Sistema de Cursos
            </Link>
            <div className="navbar-nav">
              <Link className="nav-link" to="/facultades">
                Facultades
              </Link>
              <Link className="nav-link" to="/cursos">
                Cursos
              </Link>
            </div>
          </div>
        </nav>

        {/* Contenido principal */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/facultades" element={<FacultadList />} />
          <Route path="/cursos" element={<CursoList />} />
        </Routes>

        {/* Footer */}
        <footer className="text-center text-muted mt-5 mb-3">
          <small>© 2025 Sistema de Cursos Universitarios – Desarrollado por Alicia</small>
        </footer>
      </div>
    </Router>
  );
}

export default App;
