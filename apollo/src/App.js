import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import Dasboard from './components/Dashboard';
import Navbar from './components/Navbar';
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {}
    };
  }

  componentDidMount() { 
    
    // const data = {
    //   "name" : "Apple",
    //   "ticker" : "AAPL",
    //   "sector" : "Technology",
    //   "category" : "Information Tech",
    //                 // date string, current price, number of mentions
    //   "data_data" : [["01-05-2020", 420.69, 20],["01-06-2020", 400.69, 15], ["01-07-2020", 430.69, 10]],
    //   "upvote_ratio": 0.78,
    //   //sentiment for that time period, represent it as an emoji on your end
    //   "sentiment" : 0.98,
    // };
    const data = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"],
      datasets: [
          {
              label: "GME",
              data: [33, 53, 85, 41, 44, 65, 34, 54, 78, 67, 365],
              fill: true,
              backgroundColor: "rgba(242, 167, 39, 0.2)",
              borderColor: "#F2A737"
          }
      ]
   };
   this.setState({ data: data });
   console.log(this.state.data);
  }

  render() {
    return (
      <div className="main">
        <Navbar />
        <Box height={150} />
        <Dasboard data={this.state.data}/>
      </div>
    );
  }
};

export default App;
