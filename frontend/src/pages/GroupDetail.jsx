import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getGroupDetail } from '../services/userService';

const GroupDetail = () => {
  const { id } = useParams();
  const [group, setGroup] = useState(null);

  useEffect(() => {
    getGroupDetail(id).then(setGroup);
  }, [id]);

  if (!group) return <p>Chargement...</p>;

  return (
    <div>
      <h2>{group.name}</h2>
      <p>Membres: {group.members?.length || 0}</p>
    </div>
  );
};

export default GroupDetail;
