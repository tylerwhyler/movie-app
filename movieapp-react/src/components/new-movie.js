import React, { Component } from "react";
import axios from "axios";

import App from "./app"

export default class NewMovie extends Component {
    constructor() {
        super()

        this.state = {
            title: "",
            description: "",
            rating: "",
            starrating: "",
            good: false,
            reload: 0
        }
    }

    createTitle(event) {
        this.setState({
            title: event.target.value
        })
    }

    createDescription(event) {
        this.setState({
            description: event.target.value
        })
    }

    createRating(event) {
        this.setState({
            rating: event.target.value
        })
    }

    createStarrating(event) {
        this.setState({
            starrating: event.target.value
        })
        
    }

    submitChange = () => {
        this.setState({
            good: true
        })
        axios.post("http://localhost:5000/movie", {
            title: this.state.title,
            description: this.state.description,
            rating: this.state.rating,
            starrating: this.state.starrating
        }) .then(function (response) {
            console.log(response)
        })
    }

    render() {
        return (
            <form className="create-movie">
                <input 
                type="text"
                placeholder="Title"
                onChange={event => this.createTitle(event)}
                />
                <input 
                type="text"
                placeholder="Description"
                onChange={event => this.createDescription(event)}
                />
                <input 
                type="text"
                placeholder="Parental rating"
                onChange={event => this.createRating(event)}
                />
                <input 
                type="text"
                placeholder="Movie rating"
                onChange={event => this.createStarrating(event)}
                />
                <button onClick={this.submitChange} disabled={this.state.good}>Submit</button>
            </form>
        )
    }
}