import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom';
import Navbar from '../components/Navbar/Navbar'
import Footer from '../components/Footer/Footer'
import News from '../components/News/News';
import axios from "axios";


export default function ManualPage_basket() {
  const { id } = useParams();
  const [newsDetail, setNewsDetail] = useState(null);

  useEffect(() => {
    const fetchFootballNews = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/news/basket/info/${id}/`);
        setNewsDetail(response.data);
      } catch (error) {
        console.error('Error fetching football news:', error);
      }
    };

    fetchFootballNews();
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
