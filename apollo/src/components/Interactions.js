import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import './Interactions.css';

class Interactions extends Component {

    render() {
        return (
            <Paper className="paper">
                <div>
                    <h3><u>Price</u></h3>
                    
                    <h4>value</h4>
                </div>
                <div>
                    <h3><u>Mentions</u></h3>
                    <h4>value</h4>
                </div>
                <div>
                    <h3><u>Upvote Ratio</u></h3>
                    <h4>value</h4>
                </div>
            </Paper>
        );
    }
};

export default Interactions;