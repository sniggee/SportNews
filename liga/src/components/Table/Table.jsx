import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './style.css';


export default function Table() {
  const [tableData, setTableData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/result/football')
      .then(response => response.json())
      .then(data => {
        setTableData(data);
      })
      .catch(error => console.error('Ошибка загрузки данных:', error));
  }, []);

  return (
    <div className='Table-sections'>
      <div className="container-fluid">
        <h2 className='table__footbal-text'>Футбольная лига</h2>
        <table className='table__common'>
          <thead>
            <tr className='table__tr'>
              <th>#</th>
              <th>Комманда</th>
              <th>И</th>
              <th>В</th>
              <th>Н</th>
              <th>П </th>
              <th>З</th>
              <th>П</th>
              <th>+/-</th>
              <th>О</th>
            </tr>
          </thead>
          <tbody>
            {tableData.map((rowData, index) => (
              <tr key={index}>
                <td width={"50"}>{index + 1}</td>
                <td>
                  <Link to={`/table/${rowData.teamId}`}>
                    <div className="img16">
                      <img loading="lazy" src={rowData.team.image} alt={rowData.team.name}/>
                      <span><p className='mb-0 ps-2'>{rowData.team.name}</p></span>
                    </div>
                  </Link>
                </td>
                <td>{rowData.matches}</td>
                <td>{rowData.wins}</td>
                <td>{rowData.draws}</td>
                <td>{rowData.losses}</td>
                <td>{rowData.goalsFor}</td>
                <td>{rowData.goalsAgainst}</td>
                <td>{rowData.goalDifference}</td>
                <td>{rowData.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
