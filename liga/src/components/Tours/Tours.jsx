import React, { useEffect, useState } from 'react'
import TourList from './TourList'
import "./styles.css";


export default function Tours({url}) {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/tours/${url}`).
        then(response => response.json()).
        then(response => {
            setData(response)
        })
    }, [])

    return (
        <main className="tours-container">
            {data.map((tour, index) => 
                <div key={index} className="tour">
                    <p>{tour.tour}</p>
                    <div className="matches-wrapper">
                        <TourList data={tour.matches}/>
                    </div>
                </div>
            )}
        </main>
  )
}