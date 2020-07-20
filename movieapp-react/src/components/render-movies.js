import React, { Component } from "react"

import App from "./app"

export default class RenderMovies extends Component {
    render(props) {
        return (
            <div className="movie">
                <div>Title: {this.props.title}</div>
                <div>Description: {this.props.description}</div>
                <div>Rated: {this.props.rating}</div>
                <div>Rating: {this.props.starrating}</div>
            </div>
        )
    }
}