import React, { useState } from 'react'
import "./style.css";
import Comments from '../Comments/Comments';


export default function News({news, article}) {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleExpand = () => {
        setIsExpanded(true);
    };
  
    const handleCollapse = () => {
        setIsExpanded(false);
    };

    return (
        <div className='newsdetail'>
            <div className="container-fluid newsdetail-sect pt-5 pb-5">
                {article && (
                    <div className='news-detail'>
                        <h2>{article.title}</h2>
                        <p>{article.data}</p>
                        <img src={article.photo} alt="news" />
                        <p className='news-detail-p'>{isExpanded ? news : news.slice(0, 800)}</p>
            {news.length > 60 && !isExpanded && <button className='detail-news_btn' onClick={handleExpand}>Развернуть</button>}
            {isExpanded && <button className='detail-news_btn' onClick={handleCollapse}>Скрыть</button>}
                    </div>
                )}
            </div>

            <Comments news_id={article.id} />
        </div>
    )
}