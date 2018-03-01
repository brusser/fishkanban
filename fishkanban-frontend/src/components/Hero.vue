<template>
  <!-- Hero -->
  <div id="hero" class=block>
    <div class="hero is-light">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-2">
            Fish Kanban!
          </h1>
          <h2 class="subtitle">
            So Much
            <strong>Fish</strong>!
          </h2>
        </div>
      </div>
      <nav class="navbar">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="field">
              <form v-on:submit.prevent="executeSearch">
                <input type="search" v-model.trim="query" class="input" name="query" v-on:keyup.enter.prevent.stop="executeSearch" placeholder="Search Fish" />
                <button type="submit">
                  Search
                </button>
              </form>
              <div v-cloak>
                <small>Searching for: {{ query }}</small>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      query: ''
    }
  },
  methods: {
    executeSearch() {
      if (this.query) {
        axios
          .get('http://localhost:8000/fish')
          .then(response => {
            this.fish = response.data
          })
          .catch(e => {
            alert(e.message)
          })
      } else {
        alert('Please enter a query')
      }
    }
  }
}
</script>

<style>

</style>
