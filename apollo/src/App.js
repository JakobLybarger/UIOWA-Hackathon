import React, { Component } from 'react';
import './App.css';
import Box from '@material-ui/core/Box';
import NavBar from './components/Navbar';
import StockChart from './components/StockChart';
import Interactions from './components/Interactions';

class App extends Component {
  render() {
    return (
      <div>
        <NavBar />
        <Box height={150} />
        <StockChart />
        <Interactions />
      </div>
    );
  }
};

export default App;
