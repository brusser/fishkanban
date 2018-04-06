// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import config from './config'

import fishmodel from './fish_pb'

Vue.config.productionTip = false

// window.wsScheme = window.location.protocol == "https:" ? "wss" : "ws";

window.wsRoot = config.socket

Vue.prototype.$fishmodel = fishmodel

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
