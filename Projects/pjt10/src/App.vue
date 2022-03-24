<template>
  <div id="app">
    <div class="ml-auto" >
      <b-navbar type="dark" variant="dark">
        <b-navbar-nav class="justify-content-end">
          <b-nav-item>
            <router-link to="/">Home</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link to="/random">Random</router-link> 
          </b-nav-item>
          <b-nav-item>  
            <router-link to="/my-movie-list">MyMovieList</router-link>
          </b-nav-item>
        </b-navbar-nav>
      </b-navbar>
    </div>
    <br>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color:rgb(186, 213, 248)
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
html {
  background-color:rgb(186, 213, 248);
}
</style>
