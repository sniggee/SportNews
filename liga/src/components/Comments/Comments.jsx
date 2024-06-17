import React, { useState, useEffect } from "react";
import "./style.css";
import Comment from "./Comment/Comment";
import TextArea from "antd/es/input/TextArea";
import axios from "axios";
import Alert from "../Alert";


export default function Comments({news_id}){
    const [comments, setComments] = useState([]);
    const [writingComment, setWritingCommet] = useState(false);
    const [user, setUser] = useState(null);
    const [commentText, setCommentText] = useState("");

    const [openWarning, setOpenWarning] = useState(false);

    const handleClose = () => {
        setOpenWarning(false);
    };

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
          fetchUser(token);
        }
    }, []);

    const fetchUser = async (token) => {
        try {
          const response = await axios.get('http://localhost:8000/user/profile/', {
            headers: {
              'Authorization': `Token ${token}`
            }
          });
          setUser(response.data);
        } catch (error) {
          console.error(error);
        }
    }

    useEffect(() => { 
        fetch(`http://127.0.0.1:8000/news/comments/${news_id}`).
        then(response => response.json()).
        then(response => {
            setComments(response);
        }).catch(() => console.log("something went wrong"))
    }, [])

    function sendComment(event){
        event.preventDefault();
        if (user === null){
            setOpenWarning(true);
            return;
        }

        const commentData = {
            user: user.username,
            text: commentText,
            news: news_id
        }

        fetch("http://127.0.0.1:8000/news/comment", {
            method: "post",
            body: JSON.stringify(commentData),
            headers: {
                'Accept': 'application/x-www-form-urlencoded',
                'Content-Type': 'application/x-www-form-urlencoded'
            }})
            .then(response => response.json())
            .then(response => {
                console.log(response);
                setComments([...comments, response])
            })

        setWritingCommet(false);
    }

    return (
        <div className="comments-container">
            <h2>Комментарии: {comments.length}</h2>
            <div className="comments-wrapper">
                {comments.map((comment, index) => <Comment key={index} data={comment} />)}
            </div>

            {writingComment ? (
                <form onSubmit={sendComment}>
                    <p>Введите комментарий</p>

                    <TextArea 
                        onChange={(event) => setCommentText(event.target.value)} 
                        style={{height: "125px" }} 
                        placeholder="текст комментария" 
                    />

                    <input type="submit" value="оставить комментарий" />
                    
                    <Alert 
                        open={openWarning} 
                        severity={"warning"} 
                        handleClose={handleClose} 
                        text={"Войдите в аккаунт для того, чтобы оставить комментарий"} 
                    />
                </form>
            ):(
                <button onClick={() => setWritingCommet(true)} >Оставить комментарий</button>
            )}
        </div>
    )
}