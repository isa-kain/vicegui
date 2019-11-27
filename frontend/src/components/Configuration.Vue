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
        <b-button v-on:click="getSelectedConfigText()">Load selected configuration</b-button><br>
      </b-col>
    </b-row>

    <b-row>
      <b-col sm="12">
        <b-form-textarea
          id="textarea"
          v-model="ctext"
          placeholder="Enter something..."
          rows="8"
        ></b-form-textarea>
      </b-col>
    </b-row>

    <b-row>
      <b-col sm="12">
        <b-button v-on:click="sendChanges()">Save edited onfiguration as new file</b-button>
        <!-- <b-button>Save edited onfiguration as new file</b-button> -->
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'Configuration', // this is the name of the component
  data () {
    return {
      ctext: ''
    }
  },
  mounted: function () {
    this.grabAllConfigs()
  },
  methods: {
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
    },
    getSelectedConfigText: function () {
      // reports which config file user selects from dropdown
      // grabs contents of selected file from server
      // assigns contents to "ctext" global var, which writes automatically to textarea
      var selectedConfig = document.getElementById('config-files').value
      console.log(selectedConfig)
      this.axios.post('/api/getConfigXML', {
        selected: selectedConfig
      }).then(response => {
        this.ctext = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    sendChanges: function () {
      // sends changes to server
      var changedText = document.getElementById('textarea').value
      console.log('Pulled text:')
      console.log(changedText)
      this.axios.post('/api/createNewConfig', {
        changedConfig: changedText
      }).then(response => {
        console.log('recieved response')
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
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
