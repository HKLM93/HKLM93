<template>
  <div class="home">
    <h1>Popular Movies</h1>
    <div>
      <b-card-group class="center-block">
        <movie-card
          v-for="movieCard in movieCards" 
          :key="movieCard.id" 
          :movieCard="movieCard">
        </movie-card>
      </b-card-group>
    </div> 
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import {mapState} from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created:function(){
    this.$store.dispatch('LoadMovieCards')
  },
  computed:{
    ...mapState(['movieCards'])
  }
}
</script>
