<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <Navigation></Navigation>
    <router-view/>
  </div>
</template>

<script>
import Navigation from './components/Navigation'

export default {
  name: 'App',
  components: {
    'Navigation': Navigation
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<!--style lang="scss">
  $navbar-background-color: $blue;
  $navbar-item-color : $white;
</style-->

<!-- Lifted from H4WEBGUI-->
<!--style lang="scss">
// Import Bulma's core
// @import 'bulma';
@import "~bulma/sass/utilities/_all";
@import '~bulma-checkradio';

// $box-radius: 0;
// $section-padding: 1.5rem 1rem;
$navbar-background-color: $blue;
$navbar-item-color : $white;

// Import Bulma and Buefy styles
@import "bulma";
</style-->
