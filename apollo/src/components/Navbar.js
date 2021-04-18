import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import { Typography } from '@material-ui/core';
import './Navbar.css';

class Navbar extends Component {

    render() {
        return (
            <AppBar position="Fixed" className="appbar">
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