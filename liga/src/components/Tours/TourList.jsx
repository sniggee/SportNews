import React from 'react'


export default function TourList({data}) {
    return (
    <>
        {data.map((match, index) => 
            <div key={index} className={"tour-list " + "color" + (index % 4 < 2 ? 1 : 2)}>
                <div className="teams-container">
                    <div className="tour-section">
                        <img src={match.match.first_team.image} />
                        <a>{match.match.first_team.name}</a>
                    </div>

                    <div className="tour-section">
                        <img src={match.match.second_team.image} />
                        <a>{match.match.second_team.name}</a>
                    </div>
                </div>

                <div className="right-block">
                    {match.match.is_ended ? 
                        <>
                            <a>{match.score[0]}</a>
                            <a>{match.score[1]}</a>
                        </> : 
                        <>
                            <a>{match.match.date}</a>
                            <a>{match.match.time}</a>
                        </>
                    }
                </div>
            </div>
        )}
    </>
  )
}
