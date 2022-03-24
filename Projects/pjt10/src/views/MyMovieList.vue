<template>
  <div class="container">
    <header class="bg-sky">
      <br>
      <h1 class="text-color">My Movie List</h1>
      <my-list-form></my-list-form>
      <br>
    </header>
      <my-list></my-list>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm.vue'
import MyList from '@/components/MyList.vue'

export default {
  name:'MyMovieList',
  components:{
    MyListForm,
    MyList,
  }
}
</script>

<style>
.bg-sky{
  background-color:#2c3e50;
}
.text-color{
  color:honeydew;
}

</style>