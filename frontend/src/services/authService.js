import api from './api';

export const loginUser = async (credentials) => {
  const response = await api.post('auth/login/', credentials);
  localStorage.setItem('user', JSON.stringify(response.data.user));
  return response.data;
};

export const logoutUser = () => {
  localStorage.removeItem('user');
};

export const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};
