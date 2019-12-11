<template>
    <div style="padding:10px 5px 10px 5px;">
        <b-row v-for="key in Object.keys(myelement)" v-bind:key="key">
            <b-col sm="2" v-if="myparentisarray"> <!-- v-if="Array.isArray(myelement)===false" -->
                <label for="`Input-${mykey}`"> {{mykey}}</label>
            </b-col>
            <b-col sm="2" v-else-if="!Array.isArray(myelement[key])"> <!-- v-if="Array.isArray(myelement)===false" -->
                <label for="`Input-${mykey}`"> {{key}}</label>
            </b-col>
            <b-col sm="8" v-if="typeof myelement[key] === 'string'">
                <b-form-input id="Input-${mykey}" v-model="myelement[key]"></b-form-input>
            </b-col>
            <b-col v-if="typeof myelement[key] === 'object'">
                <b-row>
                    <b-col>
                        <br>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col v-if="Array.isArray(myelement[key])">
                        <TagComponent :myelement="myelement[key]" :mykey="key" :myparentisarray="true" id="Tag-${key}"></TagComponent>
                    </b-col>
                    <b-col v-else>
                        <TagComponent :myelement="myelement[key]" :mykey="key" :myparentisarray="false" id="Tag-${key}"></TagComponent>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
    </div>
</template>

<script>
// import TagComponent from 'TagComponent'
export default {
  name: 'TagComponent',
  props: ['myelement', 'mykey', 'myparentisarray'],
  data () {
    return {
    // internalval: this.myelement
    }
  }
//   methods: {
//       updateValue: function (myelement) {
//           this.$emit('input', myelement)
//       }
//   }
}
</script>

<style scoped>

</style>
