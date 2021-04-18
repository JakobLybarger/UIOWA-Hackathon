import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import { Line } from "react-chartjs-2";
import './StockChart.css';

class StockChart extends Component {
    render() {
        const data = {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [
                {
                    label: "First dataset",
                    data: [33, 53, 85, 41, 44, 65, 34, 54, 78, 67, 365, 56],
                    fill: true,
                    backgroundColor: "rgba(242, 167, 39, 0.2)",
                    borderColor: "#F2A737"
                }
            ]
        };
        
        return (
        <Paper className="container">
            <Line data={data} />
        </Paper>
        );
    }
};

export default StockChart;
