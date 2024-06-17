import React, {useState, useEffect} from 'react'
import Navbar from '../components/Navbar/Navbar'
import Footer from '../components/Footer/Footer'
import { useParams } from 'react-router-dom';
import News from '../components/News/News';


export default function ManualPage_Footbal() {
  const { id } = useParams();
  const [newsDetail, setNewsDetail] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/news/info/${id}/`).
    then(response => response.json()).
    then(response => {
      setNewsDetail(response);
    })
  }, [])

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
