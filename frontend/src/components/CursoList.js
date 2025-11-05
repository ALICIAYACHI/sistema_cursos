// frontend/src/components/CursoList.js
import React, { useEffect, useState } from "react";
import { api } from "../api"; // 🔹 Usa el cliente axios configurado
import { Button, Form, Modal } from "react-bootstrap";

function CursoList() {
  const [cursos, setCursos] = useState([]);
  const [facultades, setFacultades] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [editingCurso, setEditingCurso] = useState(null);
  const [formData, setFormData] = useState({
    nombre: "",
    docente: "",
    horario: "",
    creditos: "",
    facultad: "",
    portada: null,
  });

  useEffect(() => {
    fetchCursos();
    fetchFacultades();
  }, []);

  const fetchCursos = async () => {
    try {
      const res = await api.get("cursos/");
      setCursos(res.data);
    } catch (err) {
      console.error("❌ Error al cargar cursos:", err);
    }
  };

  const fetchFacultades = async () => {
    try {
      const res = await api.get("facultades/");
      setFacultades(res.data);
    } catch (err) {
      console.error("❌ Error al cargar facultades:", err);
    }
  };

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData({
      ...formData,
      [name]: files && files.length > 0 ? files[0] : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();

    Object.entries(formData).forEach(([key, value]) => {
      if (value) data.append(key, value);
    });

    try {
      if (editingCurso) {
        await api.put(`cursos/${editingCurso.id}/`, data, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      } else {
        await api.post("cursos/", data, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      }

      fetchCursos();
      setShowModal(false);
      setEditingCurso(null);
      setFormData({
        nombre: "",
        docente: "",
        horario: "",
        creditos: "",
        facultad: "",
        portada: null,
      });
    } catch (err) {
      console.error("❌ Error al guardar curso:", err.response?.data || err);
      alert("Error al guardar el curso. Revisa la consola.");
    }
  };

  const handleEdit = (curso) => {
    setEditingCurso(curso);
    setFormData({
      nombre: curso.nombre,
      docente: curso.docente,
      horario: curso.horario,
      creditos: curso.creditos,
      facultad: curso.facultad,
      portada: null,
    });
    setShowModal(true);
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Deseas eliminar este curso?")) {
      try {
        await api.delete(`cursos/${id}/`);
        fetchCursos();
      } catch (err) {
        console.error("❌ Error al eliminar curso:", err);
      }
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-3 text-center">Cursos</h2>
      <Button className="mb-3" onClick={() => setShowModal(true)}>
        ➕ Nuevo Curso
      </Button>

      <table className="table table-bordered text-center align-middle">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Docente</th>
            <th>Créditos</th>
            <th>Horario</th>
            <th>Facultad</th>
            <th>Portada</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {cursos.map((c) => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.nombre}</td>
              <td>{c.docente}</td>
              <td>{c.creditos}</td>
              <td>{c.horario}</td>
              <td>{facultades.find((f) => f.id === c.facultad)?.nombre}</td>
              <td>
                {c.portada_url ? (
                  <img
                    src={c.portada_url}
                    alt={c.nombre}
                    width="80"
                    height="80"
                    style={{
                      objectFit: "cover",
                      borderRadius: "8px",
                      border: "1px solid #ddd",
                    }}
                  />
                ) : (
                  <span className="text-muted">Sin imagen</span>
                )}
              </td>
              <td>
                <Button
                  variant="warning"
                  size="sm"
                  className="me-2"
                  onClick={() => handleEdit(c)}
                >
                  ✏️ Editar
                </Button>
                <Button
                  variant="danger"
                  size="sm"
                  onClick={() => handleDelete(c.id)}
                >
                  🗑️ Eliminar
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Modal Crear / Editar */}
      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>
            {editingCurso ? "Editar Curso" : "Nuevo Curso"}
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-2">
              <Form.Label>Nombre</Form.Label>
              <Form.Control
                name="nombre"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Docente</Form.Label>
              <Form.Control
                name="docente"
                value={formData.docente}
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Créditos</Form.Label>
              <Form.Control
                type="number"
                name="creditos"
                value={formData.creditos}
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Horario</Form.Label>
              <Form.Control
                name="horario"
                value={formData.horario}
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Facultad</Form.Label>
              <Form.Select
                name="facultad"
                value={formData.facultad}
                onChange={handleChange}
              >
                <option value="">Seleccione una facultad</option>
                {facultades.map((f) => (
                  <option key={f.id} value={f.id}>
                    {f.nombre}
                  </option>
                ))}
              </Form.Select>
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Portada</Form.Label>
              <Form.Control type="file" name="portada" onChange={handleChange} />
            </Form.Group>
            <Button type="submit" variant="primary" className="w-100 mt-2">
              💾 Guardar
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </div>
  );
}

export default CursoList;
