import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import './Interactions.css';

class Interactions extends Component {

    render() {
        return (
            <Paper className="paper">
                <div>
                    <h3 className="h3"><u>Price</u></h3>
                    
                    <h4 className="h3">$100000</h4>
                </div>
                <div>
                    <h3 className="h3"><u>Mentions</u></h3>
                    <h4 className="h3">9657</h4>
                </div>
                <div>
                    <h3 className="h3"><u>Upvote Ratio</u></h3>
                    <h4 className="h3">69420 Likes / 420 Dislikes</h4>
                </div>
            </Paper>
        );
    }
};

export default Interactions;