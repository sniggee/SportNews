import React, { useEffect, useState } from 'react';
import Schedule from './schedule';
import './style.css';


export default function Raspisanie_hokey() {
  const [data, setData] = useState([]);

  useEffect(() => {
    try {
      fetch("http://127.0.0.1:8000/schedule/schedule/hockey")
      .then(response => response.json()).
      then(response => {
        setData(response);
      })
    
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }, []);

  return (
    <div className="forms__sections">
      {data.map(current_matches => 
        <div style={{paddingTop: "30px"}} className="container-fluid raspisanie__sections-container pb-5">
          <p className="date" style={{ marginBottom: "0px"}}>{current_matches.date }</p>
          <Schedule data={current_matches.matches} />
        </div>
      )}
    </div>
  );
}
