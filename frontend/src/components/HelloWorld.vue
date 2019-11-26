<template> <!-- could use CSS grid-->
  <div class="hello">
    <title>VICE++ Control GUI</title>
    <!-- <h1>{{ msg }}</h1> -->
    <!-- <h2>Essential Links</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul> -->
    <!-- <Navigation name="nav"></Navigation> -->
    <div class="row">
      <div class="column is-half">
        <div class="fsm">
          <section style="background-color:black;color:white;margin:10px 5px 10px 5px;padding:10px 5px 10px 5px;"> <!-- Area for FSM status -- align left-->
            FSM div to be built here
            <div class="columns is-0">
              <div class="Initialized">Initialized</div>
              <div class="Configured">Configured</div>
              <div class="Running">Running</div>
              <div class="Paused">Paused</div>
              <div class="Error">Error</div>
            </div>
          </section>
        </div>
      </div>

      <div class="column is-half">
        <div class="config">
          <section style="background-color:#e6f2ff;color:black;margin:10px 5px 10px 5px;padding:10px 5px 10px 5px;"> <!-- Area for configurables -- align right-->
            Configurables to be placed here
            <section>
                  <form id="numCards">
                    <p><label>Number of VFEs: <input form="numCards" type="number" id="numVFE" maxlength="5" style="width:120px;"></label></p>
                    <p><label>Number of FEs: <input form="numCards" type="number" id="numFE" maxlength="5" style="width:120px;"></label></p>
                  </form>

                  <!-- <button id='clickMe' v-on:click="contactServer()">Click me!</button><br> -->

                  <form>
                    <input type="radio" name='clock' id='clockSource' value="1">Clock Source 1<br>
                    <input type="radio" name='clock' id='clockSource' value="2">Clock Source 2<br>
                  </form><br>

                  <select id='dropSelect'>
                    <option selected disabled>Choose one</option>
                    <option value="a">A</option>
                    <option value="b">B</option>
                    <option value="c">C</option>
                    <option value="d">D</option>
                  </select>

                  <p></p>

                  <button v-on:click="readOptions()">Show selections</button>
                  <button v-on:click="submitChanges()">Update from selection</button>

            </section>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>
<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    readOptions: function () {
      try {
        var selectOpt = document.getElementById('dropSelect').value
        var selectClock = document.querySelector('input[id="clockSource"]:checked').value
        var numVFE = document.getElementById('numVFE').value
        var numFE = document.getElementById('numFE').value
        var selectedOptions = {'Dropdown': selectOpt, 'Clock': selectClock, 'Num VFEs': numVFE, 'Num FEs': numFE}
        console.log(selectedOptions)
        return selectedOptions
      } catch (error) {
        console.log(error)
      }
      // there's probably a readBody() sort of function to read in all options
    },
    submitChanges: function () {
      console.log('submitting selections')
      axios.post('/api/showChanges', {
        msg: 'Submitting',
        params: { // would ideally like to set params = readOptions() but can't figure out correct syntax
          selectOpt: document.getElementById('dropSelect').value,
          selectClock: document.querySelector('input[id="clockSource"]:checked').value
        }
      }).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
// function testFunction () {
//   // load most recent configuration
//   return 0
// }
</script>
<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.column {
  float: left;
  width: 50%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
