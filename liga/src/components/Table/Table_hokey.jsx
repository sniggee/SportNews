import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './style.css'


export default function Table_basketball() {
  const [tableData, setTableData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch('http://127.0.0.1:8000/result/hockey').
        then(response => response.json()).
        then(response => {
          setTableData(response);
        })
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className='forms__sections'>
      <div className='Table-sections'>
        <div className="container-fluid">
          <h2 className='table__footbal-text'>Хоккейная лига</h2>
          <table className='table__common'>
            <thead>
              <tr className='table__tr'>
                <th>#</th>
                <th>Комманда</th>
                <th>И</th>
                <th>В</th>
                <th>П</th>
                <th>З</th>
                <th>ПР</th>
                <th>Очки</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, index) => (
                <tr key={index}>
                  <td width={"50"}>{index + 1}</td>
                  <td>
                    <Link to={`/table/${row.teamId}`}>
                      <div className="img16">
                        <img loading="lazy" src={row.team.image} alt={row.team.name}/>
                        <span><p className='mb-0 ps-2'>{row.team.name}</p></span>
                      </div>
                    </Link>
                  </td>

                  <td>{row.matches}</td>
                  <td>{row.wins}</td>
                  <td>{row.looses}</td>
                  <td>{row.goalsFor}</td>
                  <td>{row.goalsMissed}</td>
                  <td>{row.points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
