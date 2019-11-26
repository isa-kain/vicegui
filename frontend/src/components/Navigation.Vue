<template>
  <b-navbar toggleable="md" type="dark" variant="info" fixed="top">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/configuration">Config</b-nav-item> <!-- each item is page-->
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<style>
  .spacing {
    Margin-right: 10px;
  }
</style>
