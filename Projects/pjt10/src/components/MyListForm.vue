<template>
  <div>
    <input 
    type="text"
    @keyup.enter="createList"
    v-model.trim="movieTitle">
    <span>' '</span>
    <b-button @click="createList">Add</b-button>
  </div>
</template>

<script>
export default {
  name:'MyListForm',
  data:function(){
    return{
      movieTitle:null,
    }
  },
  methods:{
    createList:function(){
      const myMovie={
        title:this.movieTitle,
        isWatched:false,
        date:new Date().getTime()
      }
      if (myMovie.title){
        this.$store.dispatch('createList',myMovie)
      }
      this.movieTitle=null
    }

  }
}
</script>

<style>

</style>