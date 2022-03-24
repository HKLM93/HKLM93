import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  state: {
    movieCards:[],
    myMovies:[],
  },
  mutations: {
    LOAD_MOVIE_CARDS:function(state,results){
      state.movieCards=results
    },
    CREATE_LIST:function(state,movie){
      state.myMovies.push(movie)
    },
    DELETE_MOVIE:function(state,movie){
      const index=state.myMovies.indexOf(movie)
      state.myMovies.splice(index,1)
    },
    UPDATE_MOVIE:function(state,movie){
      state.myMovies=state.myMovies.map(myMovie=>{
        if(myMovie==movie){
          return{
            ...myMovie,
            isWatched:!movie.isWatched
          }
        }else{
          return myMovie
        }
      })
    }
  },
  actions: {
    LoadMovieCards:function({commit}){
      axios({
        methods:'get',
        url:'https://api.themoviedb.org/3/movie/popular',
        params:{
          api_key:'cf85387cb23102d7dcdbb033efadd2e5',
          language:'ko-kr',
        }
      })
        .then((res)=>{
          console.log(res)
          commit('LOAD_MOVIE_CARDS',res.data.results)
        })
    },
    createList:function({commit},movie){
      commit('CREATE_LIST',movie)
    },
    deleteMovie:function({commit},movie){
      commit('DELETE_MOVIE',movie)
    },
    updateMovie:function({commit},movie){
      console.log(movie)
      commit('UPDATE_MOVIE',movie)
    }
  },
  modules: {
  }
})
