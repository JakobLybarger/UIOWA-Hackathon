import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import { Typography } from '@material-ui/core';
import Vector from '../Vector.png'
import './Navbar.css';

class Navbar extends Component {

    render() {
        return (
            <AppBar position="Fixed" className="appbar">
                <img src={Vector} alt="rocket" className="image" />
                <Typography variant="h4" className="title">
                    APOLLO
                </Typography>
                <div className="sort_by">
                    <Typography variang="h6">
                        Sort By: Day | Week | Month | Year
                    </Typography>
                </div>

            </AppBar>
        );
    }
};

export default Navbar;