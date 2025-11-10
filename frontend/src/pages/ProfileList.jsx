import React, { useEffect, useState } from 'react';
import { getProfiles } from '../services/userService';
import { Link } from 'react-router-dom';

const ProfileList = () => {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    getProfiles().then(setProfiles);
  }, []);

  return (
    <div className="profile-list">
      <h2>Liste des profils</h2>
      <ul>
        {profiles.map((p) => (
          <li key={p.id}><Link to={`/profiles/${p.id}`}>{p.username}</Link></li>
        ))}
      </ul>
    </div>
  );
};

export default ProfileList;
