<template> <!-- could use CSS grid-->
  <div class="hello">
    <br>
    <h1>VICE++ Control GUI</h1>
    <p>Here is some information. This is the control page.</p>
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

    <div id="FSM" class=column-left style="background-color:#e6f2ff;color:black;padding:10px 5px 10px 5px;">
      <h2>FSM runstate to be placed here</h2>
    </div>

    <div id="Configs" class=column-right style="background-color:#e6f2ff;color:black;padding:10px 5px 10px 5px;">
      <h2 >Quick Configuration:</h2>
      <b-col>
        <select id="config-files">Select configuration to load:</select>
        <p></p>
        <b-button v-on:click="defineConfigurables()">Load selected configuration</b-button>
        <p></p>
      </b-col>

      <div>
        <form id="config-params"></form>
      </div>

      <p></p>
      <b-button v-on:click="submitChanges()">Save changes as new configuration</b-button>
      <b-button >Apply selected configuration</b-button>

      <p><i>Note: refresh page to see newly created configuration</i></p>
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
  mounted: function () {
    this.grabAllConfigs()
  },
  methods: {
    readOptions: function () {
      // reads values of html forms
      console.log('Starting to parse input values')
      var cform = document.getElementById('config-params')
      var newdict = {}
      for (var i = 0; i < 1; i++) {
        var newtag = cform['input' + i].name
        var newval = cform['input' + i].value
        newdict[newtag] = newval
      }
      console.log(newdict)
      return newdict
    },
    submitChanges: function () {
      // sends output of readOptions() to server
      console.log('BASECONFIG ' + document.getElementById('config-files').value)
      console.log('UPDATES ' + this.readOptions())
      axios.post('/api/updateConfigFromParams', {
        baseConfig: document.getElementById('config-files').value,
        updates: this.readOptions()
      }).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    },
    defineConfigurables: function () {
      // recieves dict of parameters being configured
      // dynamically declares editable forms for each parameter
      // clears any previously declared elements
      var editables = document.getElementById('config-params')
      while (editables.hasChildNodes()) {
        editables.removeChild(editables.firstElementChild)
      }
      axios.post('/api/getConfigParams', {
        selectedConfig: document.getElementById('config-files').value
      }).then(function (response) {
        console.log(response.data)
        var params = response.data
        var keys = Object.keys(params)
        console.log(keys)
        var forms = document.getElementById('config-params')
        for (var i = 0; i < keys.length; i++) {
          var label = document.createElement('label')
          label.for = keys[i]
          label.innerText = keys[i] + ': '
          console.log(label.text)
          forms.appendChild(label)

          var p = document.createElement('input')
          p.id = 'input' + i
          p.name = keys[i]
          p.value = params[keys[i]]
          forms.appendChild(p)

          forms.appendChild(document.createElement('br'))
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    grabAllConfigs: function () {
      // ask server for list of all config files
      this.axios.post('/api/listAllConfigs', {
      }).then(response => {
        console.log(response)
        this.fillConfigMenu(response.data.cfiles)
      }).catch(function (error) {
        console.log(error)
      })
    },
    fillConfigMenu: function (cfiles) {
      // fill dropdown selection with list of config files
      var menu = document.getElementById('config-files')
      for (var i = 0; i < cfiles.length; i++) {
        var newOption = document.createElement('option')
        newOption.innerHTML = cfiles[i]
        menu.appendChild(newOption)
      }
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

.column-left {
  float: left;
  width: 49%;
}

.column-right {
  float: right;
  width: 49%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
