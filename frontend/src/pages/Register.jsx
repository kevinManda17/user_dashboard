import React, { useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post('auth/register/', formData);
    navigate('/');
  };

  return (
    <div className="register-page">
      <h2>Inscription</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Nom d'utilisateur"
          onChange={(e) => setFormData({ ...formData, username: e.target.value })} />
        <input type="email" placeholder="Email"
          onChange={(e) => setFormData({ ...formData, email: e.target.value })} />
        <input type="password" placeholder="Mot de passe"
          onChange={(e) => setFormData({ ...formData, password: e.target.value })} />
        <button type="submit">S'inscrire</button>
      </form>
    </div>
  );
};

export default Register;
