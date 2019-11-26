<template>
  <div>
    <h1>Configuration</h1>
    <p>Here is some information. This is the configuration page</p>
    <b-row>
      <!-- <b-dropdown id="config-files" text="Available configuration files" class="m-md-2">
        <b-dropdown-item v-for="f in cfiles" :key="f">{{f}}</b-dropdown-item>
      </b-dropdown> -->
      <!-- For some reason, above bootstrap method does not fill dropdown properly-->
      <b-col sm="12">
        <select id="config-files">Select configuration to load:</select>
        <b-button v-on:click="getSelectedConfigText()">Load selected configuration</b-button>
      </b-col>
    </b-row>

    <b-row>
      <b-col sm="12">
        <b-form-textarea
          id="textarea"
          v-model="configtext"
          placeholder="Enter something..."
          rows="8"
        ></b-form-textarea>
      </b-col>
    </b-row>

    <b-row>
      <b-col sm="12">
        <!-- <b-button v-on:click="sendChanges()">Save edited onfiguration as new file</b-button> -->
        <b-button>Save edited onfiguration as new file</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'Configuration', // this is the name of the component
  data () {
    return {
      cfiles: [],
      configtext: ''
    }
  },
  mounted: function () {
    this.grabAllConfigs()
  },
  methods: {
    dummyTest: function () {
      var text = 'TEXT!!!!!'
      console.log(text)
      document.getElementById('textbox').value = text
    },
    grabAllConfigs: function () {
      // ask server for list of all config files
      this.axios.post('/api/listAllConfigs', {
        params: {}
      }).then(response => {
        console.log('Successfully got list of configs')
        console.log(response)
        // this.cfiles = response.data.cfiles
        this.listAllConfigs(response.data.cfiles)
      }).catch(function (error) {
        console.log(error)
      })
    },
    listAllConfigs: function (cfiles) {
      // fill dropdown selection with these files
      this.cfiles = cfiles
      var menu = document.getElementById('config-files')
      for (var i = 0; i < cfiles.length; i++) {
        var newOption = document.createElement('option')
        newOption.innerHTML = cfiles[i]
        menu.appendChild(newOption)
      }
      console.log('Listed all config files')
      console.log(cfiles, this.cfiles)
    },
    getSelectedConfigText: function () {
      // reports which config file user selects from dropdown
      // grabs contents of selected file from server
      // assigns contents to "configtext" global var, which writes automatically to textarea
      var selectedConfig = document.getElementById('config-files').value
      console.log(selectedConfig)
      this.axios.post('/api/getConfigXML', {
        selected: selectedConfig
      }).then(response => {
        this.configtext = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    sendChanges: function () {
      // sends changes to server
      return 0
    }
  }
}
</script>

<style>
.resizable {
  width: 800px;
  height: 400px;
  resize:both;
  overflow:scroll
}
</style>
