import React, { useEffect, useState } from 'react';
import { getGroups } from '../services/userService';
import { Link } from 'react-router-dom';

const GroupList = () => {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    getGroups().then(setGroups);
  }, []);

  return (
    <div className="group-list">
      <h2>Liste des groupes</h2>
      <ul>
        {groups.map((g) => (
          <li key={g.id}><Link to={`/groups/${g.id}`}>{g.name}</Link></li>
        ))}
      </ul>
    </div>
  );
};

export default GroupList;
