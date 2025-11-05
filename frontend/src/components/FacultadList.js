// frontend/src/components/FacultadList.js
import React, { useEffect, useState } from "react";
import { api } from "../api"; // 🔹 Importa tu cliente axios ya configurado
import { Button, Form, Modal } from "react-bootstrap";

function FacultadList() {
  const [facultades, setFacultades] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [editingFacultad, setEditingFacultad] = useState(null);
  const [formData, setFormData] = useState({
    nombre: "",
    decano: "",
    descripcion: "",
    logo: null,
  });

  useEffect(() => {
    fetchFacultades();
  }, []);

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
      if (editingFacultad) {
        await api.put(`facultades/${editingFacultad.id}/`, data, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      } else {
        await api.post("facultades/", data, {
          headers: { "Content-Type": "multipart/form-data" },
        });
      }

      fetchFacultades();
      setShowModal(false);
      setEditingFacultad(null);
      setFormData({ nombre: "", decano: "", descripcion: "", logo: null });
    } catch (err) {
      console.error("❌ Error al guardar facultad:", err.response?.data || err);
      alert("Error al guardar la facultad. Revisa la consola.");
    }
  };

  const handleEdit = (facultad) => {
    setEditingFacultad(facultad);
    setFormData({
      nombre: facultad.nombre,
      decano: facultad.decano,
      descripcion: facultad.descripcion,
      logo: null,
    });
    setShowModal(true);
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Deseas eliminar esta facultad?")) {
      try {
        await api.delete(`facultades/${id}/`);
        fetchFacultades();
      } catch (err) {
        console.error("❌ Error al eliminar facultad:", err);
      }
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-3 text-center">Facultades</h2>

      <Button className="mb-3" onClick={() => setShowModal(true)}>
        ➕ Nueva Facultad
      </Button>

      <table className="table table-bordered text-center align-middle">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Decano</th>
            <th>Logo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {facultades.map((f) => (
            <tr key={f.id}>
              <td>{f.id}</td>
              <td>{f.nombre}</td>
              <td>{f.decano}</td>
              <td>
                {f.logo_url ? (
                  <img
                    src={f.logo_url}
                    alt={f.nombre}
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
                  onClick={() => handleEdit(f)}
                >
                  ✏️ Editar
                </Button>
                <Button
                  variant="danger"
                  size="sm"
                  onClick={() => handleDelete(f.id)}
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
            {editingFacultad ? "Editar Facultad" : "Nueva Facultad"}
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
              <Form.Label>Decano</Form.Label>
              <Form.Control
                name="decano"
                value={formData.decano}
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Descripción</Form.Label>
              <Form.Control
                as="textarea"
                rows={2}
                name="descripcion"
                value={formData.descripcion}
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>Logo</Form.Label>
              <Form.Control type="file" name="logo" onChange={handleChange} />
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

export default FacultadList;
