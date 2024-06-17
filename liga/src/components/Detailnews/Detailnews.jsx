import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import cheerio from 'cheerio';
import News from '../News/News';


export default function Detailnews() {
  const location = useLocation();
  const article = location.state.article;
  const [news, setNews] = useState('');

  useEffect(() => {
      const fetchData = async () => {
          try {
              const url = `${article.href}`;
              const response = await axios.get(url);
              const $ = cheerio.load(response.data);
              
              // Извлекаем описание из первого <p>
              const description1 = $('div.w610_text.vrez').next('p').text().trim();
              
              // Находим все теги <p>, следующие за нужным div
              let description = '';
              $('div.se-banner').nextAll('p').each((index, element) => {
                  description += $(element).text().trim() + ' ';
              });

              // Объединяем оба описания в одну строку
              const fullDescription = `${description1} ${description}`;

              setNews(fullDescription);
          } catch (error) {
              console.error('Ошибка при загрузке данных:', error);
          }
      };

      fetchData();
  }, []);

  return (
    <News news={news} article={article} />
  );
}
