<template>
  <div>
    <p>Some sample code to make sure Flask-SocketIO works...</p>
    <button v-on:click="testSocket">Create Test Fish</button>
    <Hero/>
    <div class="container">
      <Kanban/>
    </div>
    <div class="container">
      <div id="newFishAndFilter" class="block">
        <div class="tile is-ancestor">
          <div v-cloak class="tile is-parent is-vertical">
            <article class="tile notification is-child is-5">
              <NewFish/>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Hero from './Hero.vue'
import Kanban from './Kanban.vue'
import NewFish from './NewFish.vue'

export default {
  name: 'FishKanban',
  components: {
    Hero,
    Kanban,
    NewFish
  },
  data() {
    return {
      ws: null,
      fish: [],
      isConnected: false,
      socketMessage: ''
    }
  },
  mounted() {
    const ws = new WebSocket(window.wsRoot)

    ws.onmessage = this.receive
    this.ws = ws
  },
  methods: {
    receive(msg) {
      const data = JSON.parse(msg.data)
      console.log(data)
      console.log(this.$fishmodel.fromObject(data))
    },
    testSocket() {
      // Send the "test" action event to the server.
      this.ws.send(JSON.stringify({ action: 'test' }))
      var fishData = new this.$fishmodel.Fish()
      fishData.setId(9876)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
