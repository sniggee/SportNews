import React, { useState, useEffect } from 'react';
import Schedule from './schedule';
import './style.css';


export default function Scheduleforms() {
  const [gameData, setGameData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [gamesPerPage] = useState(25); // Количество игр на странице

  useEffect(() => {
    try {
      fetch("http://127.0.0.1:8000/schedule/schedule/football").
      then(response => response.json()).
      then(response => {
        setGameData(response);
      })
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  
  }, []);

  // Индекс последней игры на текущей странице
  const indexOfLastGame = currentPage * gamesPerPage;
  // Индекс первой игры на текущей странице
  const indexOfFirstGame = indexOfLastGame - gamesPerPage;
  // Список игр на текущей странице
  const currentGames = gameData.slice(indexOfFirstGame, indexOfLastGame);

  // Функция для переключения страниц
  const paginate = pageNumber => setCurrentPage(pageNumber);

  return (
    <div>
      <div className="forms__sections">
        {currentGames.map(current_matches => 
            <div style={{paddingTop: "30px"}} className="container-fluid raspisanie__sections-container pb-5">
              <p className="date" style={{ marginBottom: "0px"}}>{current_matches.date }</p>
              <Schedule data={current_matches.matches} />
            </div>
        )}
      </div>
    </div>
  );
}
