import React from 'react';
import './style.css'


export default function Schedule({data}) {
    return (
        <>
            {data.map((match, index) => (
                <div key={index} className="forms_com-block">
                    <div className="game_link" >
                        <div className="result">
                            <div className="ht">
                                <div className="name">
                                    <div className="img16">
                                        <span className='span-baskets'> 
                                        {match.first_team.name.length > 16
                                        ? match.first_team.name.slice(0, 16) + '...'
                                        : match.first_team.name} </span>
                                        <img className='ms-2 basketball-img16' loading="lazy" src={match.first_team.image} alt={match.first_team.name} />
                                    </div>
                                </div>
                            </div>

                            <div className="time"><span className="size11">{match.time} </span></div>

                            <div className="at ">
                                <div className="name">
                                    <div className="img16">
                                        <img className='me-2 basketball-img16' loading="lazy" src={match.second_team.image} alt={match.second_team.name} />
                                        <span className='span-baskets'>
                                        <p>{match.second_team.name.length > 16
                                        ? match.second_team.name.slice(0, 16) + '...'
                                        : match.second_team.name}</p>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
         
          ))}
        </>
    )
}