import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import StockChart from './StockChart';
import Interactions from './Interactions';
import './Dashboard.css';

class Dashboard extends Component {
    constructor(props) {
        super(props);
        // console.log(this.props.data['name']);
        var arr = this.props.data['data_data'];
        console.log(arr);
        // console.log(this.props.data['data_data'][1])
        // for (let i = 0; i < this.props.data['data_data'].length; i++) {
        //     let val = this.props.data['data_data'][i];
        //     label.push(val[0]);
        //     data.push(val[1]); 
        // }  

        this.state = {
            labels: [],
            dataset: []
        };
        let data = [];
        let label = [];
        // for (let i = 0; i < this.props.data['data_data'].length; i++) {
        //     let val = this.props.data['data_data'][i];
        //     label.push(val[0]);
        //     data.push(val[1]); 
        // }  
        const graph = {
            labels: label,
            datasets: [
                {
                    label: "GameStop Corp",
                    data: data,
                    fill: true,
                    backgroundColor: "rgba(242, 167, 39, 0.2)",
                    borderColor: "#F2A737"
                }
            ]
        };
        this.setState({ dataset: graph });
    }
    render() {
        return (
            <div>
                <h1 className="stock">GameStop Corp</h1>
                <Box display="flex" justifyContent="center">
                    <Box height={700} width={800}>
                        <StockChart data={this.props.data}/>
                        <Interactions />
                    </Box>
                </Box>
            </div>
        );
    }
};

export default Dashboard;