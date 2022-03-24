<template>
  <div id="app">
    <h1>Pick a Movie</h1>
    <br>
    <b-button @click="showMovie">Pick!</b-button>
      <br>
      <br>
      <div >
        <b-card v-if="pickedMovie"
        :img-src="getMovieImg"
        img-alt="Movie Poster"
        imt-top
        style="max-width: 20rem;"
        class="mb-2 ms-auto me-auto"
        border-variant="dark"
        >
          <b-card-text>
            <p>{{ pickedMovie.title}}</p>
            <p>{{ pickedMovie.overview}}</p>
          </b-card-text>
        </b-card>
        <p v-else> Pick a Movie!!</p>`
      </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import _ from 'lodash'

export default {
  name:'Random',
  data: function () {
    return {
      pickedMovie: null,
    }
  },
  computed: {
    ...mapState([
      'movieCards'
    ]),
    getMovieImg: function () {
      const movieImg = this.pickedMovie.poster_path
      return `https://image.tmdb.org/t/p/w500/${movieImg}`
    }
  },
  methods: {
    showMovie: function () {
      this.pickedMovie = _.sample(this.movieCards)
      console.log(this.pickedMovie)
    },
  }
}
</script>

<style>

</style>