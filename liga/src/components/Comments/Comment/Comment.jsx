import React from "react";
import "./style.css";


export default function Comment({data}){
    return (
        <div className="comment">
            <div className="header">
                <p>{data.user}</p>
                <span className="comment-date">{data.date}</span>
            </div>

            <a>{data.text}</a>
        </div>
    )
}