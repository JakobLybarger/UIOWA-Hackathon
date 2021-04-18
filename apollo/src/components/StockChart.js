
import React, { Component } from 'react';
// import Paper from '@material-ui/core/Paper';
import { Line } from "react-chartjs-2";
class StockChart extends Component {
    render() {
        const data = {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [
                {
                    label: "First dataset",
                    data: [33, 53, 85, 41, 44, 65],
                    fill: true,
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)"
                },
                {
                    label: "Second dataset",
                    data: [33, 25, 35, 51, 54, 76],
                    fill: false,
                    borderColor: "#742774"
                }
            ]
        };
        
        return (<Line data={data} />);
    }
};

export default StockChart;
