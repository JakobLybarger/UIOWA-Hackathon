import React, { Component } from 'react';
import Box from '@material-ui/core/Box'
import { Line } from "react-chartjs-2";
import './StockChart.css';

class StockChart extends Component {
    render() {   
        return (
        <Box className="container">
            <Line data={this.props.data} />
        </Box>
        );
    }
};

export default StockChart;
