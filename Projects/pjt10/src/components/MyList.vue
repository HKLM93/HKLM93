<template>
  <div>
    <my-list-item
    v-for="myMovie in myMovies" :key="myMovie.date"
    :myMovie="myMovie"
    >
    </my-list-item>
  </div>
</template>

<script>
import MyListItem from '@/components/MyListItem.vue'
import {mapState} from 'vuex'

export default {
  name:'MyList',
  components:{
    MyListItem
  },
  computed:{
    ...mapState(['myMovies'])
  }
}
</script>

<style>

</style>