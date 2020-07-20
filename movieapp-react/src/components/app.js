import React, { Component } from 'react';
import axios from 'axios';

import RenderMovies from "./render-movies"
import NewMovie from "./new-movie"

export default class App extends Component {
  constructor() {
    super()

    this.state = {
      movies: []
    }
  }

  renderMovies() {
    return this.state.movies.map(movie => {
      return (
        <div key={movie.id}>
          <RenderMovies 
            title={movie.title}
            description={movie.description}
            rating={movie.rating}
            starrating={movie.starrating}
          />
        </div>
      )
    })
  }

  componentDidMount() {
    axios.get("http://localhost:5000/movies")
    .then(res => {
      this.setState({
        movies: res.data
      })
    })
  };

  render() {
    return (
      <div className='app'>
        <h1>Movie App</h1>
        {this.renderMovies()}
        <NewMovie />
      </div>
    );
  }
}
