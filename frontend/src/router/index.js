import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
// import WebguiMain from '@/components/WebguiMain'
import Configuration from '@/components/Configuration'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/configuration',
      name: 'configuration',
      component: Configuration
    }
  ]
})
