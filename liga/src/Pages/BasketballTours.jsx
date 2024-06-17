import React from 'react'
import Tours from '../components/Tours/Tours'
import Navbar from '../components/Navbar/Navbar'
import Footer from '../components/Footer/Footer'


export default function BasketballToursPage() {
  return (
    <>
      <Navbar/>
      <Tours url={"basketball"}/>
      <Footer/>
    </>
  )
}