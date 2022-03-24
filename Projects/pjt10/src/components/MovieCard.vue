<template>
  <div>
    <br>
    <div class="container">
      <b-card
        :img-src="getMovieImg"
        img-alt="Movie Poster"
        img-top
        style="max-width: 20rem;"
        class="mb-2"
        border-variant="dark"
      >
        <b-card-text>
          <p><strong>{{ movieCard.title}}</strong></p>
          <b-button v-b-toggle.overview variant="primary">줄거리 보기</b-button>
          <b-collapse id="overview" class="collapse">
            <br>
            <p>{{ movieCard.overview }}</p>
          </b-collapse>
        </b-card-text>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name:'MovieCard',
  props:{
    movieCard:Object,
  },
  computed: {
    getMovieImg: function () {
      const movieImg = this.movieCard.poster_path
      return `https://image.tmdb.org/t/p/w500/${movieImg}`
    }
  }
}
</script>

<style>

</style>