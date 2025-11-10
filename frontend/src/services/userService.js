import api from './api';

export const getProfiles = async () => {
  const response = await api.get('profiles/');
  return response.data;
};

export const getProfileDetail = async (id) => {
  const response = await api.get(`profiles/${id}/`);
  return response.data;
};

export const getGroups = async () => {
  const response = await api.get('groups/');
  return response.data;
};

export const getGroupDetail = async (id) => {
  const response = await api.get(`groups/${id}/`);
  return response.data;
};
