<template>
  <b-navbar toggleable="md" size="lg" type="dark" variant="info" fixed="top">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item to="/">VICE++ Control GUI</b-nav-item>
        <b-nav-item to="/configuration">Full Configuration</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<style>
  .spacing {
    Margin-right: 10px;
  }
  .navbar-nav
    {
      font-size: large;
      padding-left:15px;
      padding-right:15px;
    }
</style>
