import React, {useState, useEffect} from 'react';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';
import { useParams } from 'react-router-dom';
import axios from "axios";
import News from '../components/News/News';


export default function ManualPage_hokey() {
  const { id } = useParams();
  const [newsDetail, setNewsDetail] = useState(null);

  useEffect(() => {
    const fetchFootballNews = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/news/hokey/info/${id}/`);
        setNewsDetail(response.data); // Предполагаем, что данные приходят в формате массива объектов
      } catch (error) {
        console.error('Error fetching football news:', error);
      }
    };

    fetchFootballNews(); // Вызываем функцию при загрузке компонента
  }, []);

  return (
    <>
      <Navbar/>
      {newsDetail !== null ? (
        <News news={newsDetail.description} article={newsDetail} />
      ):(
        <></>
      )}
      <Footer/>
    </>
  )
}
