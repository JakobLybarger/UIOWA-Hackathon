import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import { Typography } from '@material-ui/core';
import './Navbar.css';
import Vector from '../Vector.png';

class Navbar extends Component {
    render() {
        return (
            <AppBar position="Fixed" className="appbar">
                <img className="image" src={Vector} />
                <Typography variant="h3" className="title">
                    Apollo
                </Typography>
                <Typography variang="h6">
                    Sort By: Day | Week | Month | Year
                </Typography>
            </AppBar>
        );
    }
};

export default Navbar;