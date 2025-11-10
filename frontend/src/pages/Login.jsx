import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const { login } = useContext(AuthContext);
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(credentials);
    navigate('/dashboard');
  };

  return (
    <div className="login-page">
      <h2>Connexion</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Nom d'utilisateur"
          onChange={(e) => setCredentials({ ...credentials, username: e.target.value })} />
        <input type="password" placeholder="Mot de passe"
          onChange={(e) => setCredentials({ ...credentials, password: e.target.value })} />
        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
};

export default Login;
