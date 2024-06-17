import React, { useEffect, useState } from 'react';
import './style.css'


export default function Table_basketball() {
  const [tableData, setTableData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch("http://127.0.0.1:8000/result/basketball").
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
          <h2 className='table__footbal-text'>Баскетбольная лига</h2>
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
                <th>О</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, index) => (
                <tr key={index}>
                  <td width={"50"}>{index + 1}</td>
                  <td>
                    <div className="img16">
                      <img src={row.team.image} alt="Логотип команды" />
                      <a style={{marginLeft: "10px"}}>{row.team.name}</a>
                    </div>
                  </td>

                  <td>{row.matches}</td>
                  <td>{row.wins}</td>
                  <td>{row.looses}</td>
                  <td>{row.goalsFor}</td>
                  <td>{row.goalsMissed}</td>
                  <td>{row.total_points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
