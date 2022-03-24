<template>
  <div>
    <p></p>
    <div class="list-color">
      <span  @click="updateMovie" :class="{'is-watched':myMovie.isWatched}">{{myMovie.title+' '}}</span>
      <b-button size='sm' @click="deleteMovie">Delete</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name:'MyListItem',
  props:{
    myMovie:Object,
  },
  methods:{
    deleteMovie:function(){
      this.$store.dispatch('deleteMovie',this.myMovie)
    },
    updateMovie:function(){
      this.$store.dispatch('updateMovie',this.myMovie)
    }
  }
}
</script>

<style>
.is-watched{
  color: grey;
  text-decoration: line-through;
}
.list-color{
  background-color:rgb(243, 234, 234);
}

</style>