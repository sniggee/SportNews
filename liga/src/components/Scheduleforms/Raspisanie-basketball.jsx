import React, { useEffect, useState } from 'react';
import Schedule from './schedule';
import './style.css'


export default function Raspisanie_basketball() {
    const [data, setData] = useState([]);
  
    useEffect(() => {
      fetch('http://127.0.0.1:8000/schedule/schedule/basketball').
      then(response => response.json()).
      then(response => {
        setData(response);
      });
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
