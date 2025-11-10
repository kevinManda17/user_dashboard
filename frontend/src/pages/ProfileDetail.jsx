import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getProfileDetail } from '../services/userService';

const ProfileDetail = () => {
  const { id } = useParams();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    getProfileDetail(id).then(setProfile);
  }, [id]);

  if (!profile) return <p>Chargement...</p>;

  return (
    <div>
      <h2>{profile.username}</h2>
      <p>Email: {profile.email}</p>
    </div>
  );
};

export default ProfileDetail;
