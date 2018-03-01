<template>
  <div>
    <p class="title">Add New Fish</p>
    <form v-on:submit.prevent="newFish">
      <div class="field">
        <label class="label">Fish Id</label>
        <p class="control has-icon has-icon-right">
          <input v-model.number="newFishId" type="number" class="input is-success" placeholder="Id input" required />
          <span class="icon is-small">
            <i class="fa fa-check"></i>
          </span>
        </p>
        <p class="help is-success">This ID is available</p>
      </div>

      <div class="field">
        <label class="label">Date</label>
        <p class="control">
          <input v-model="newFishDateTime" type="datetime-local" class="input" required />>
        </p>
      </div>
      <div class="field">
        <label class="label">Fish Type</label>
        <p class="control">
          <span class="select">
            <select v-model="newFishType" required>
              <option value="salmon">Salmon</option>
              <option value="tuna">Tuna</option>
            </select>
          </span>
        </p>
      </div>

      <div class="field">
        <label class="label">Tags</label>
        <p class="control">
          <input v-model.trim="newFishTags" type="text" class="input" placeholder="Tags coma seperated" />
        </p>
        <small>{{ newFishTags }}</small>
      </div>

      <div class="field">
        <label class="label">Details</label>
        <p class="control">
          <textarea v-model="newFishDetails" type="text" class="textarea" placeholder="Text area"></textarea>
        </p>
      </div>

      <div class="field is-grouped">
        <p class="control">
          <button type='submit' class="button is-primary">Submit</button>
        </p>
        <p class="control">
          <button type='reset' v-on:click="clear" class="button is-link">Cancel</button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NewFish',

  data() {
    return {
      newFishId: '123445',
      newFishDateTime: new Date().toISOString().slice(0, 16),
      newFishType: '',
      newFishTags: ['fresh', 'new'],
      newFishDetails: '',
      token: ''
    }
  },
  created() {
    axios.defaults.headers['Authorization'] =
      'JWT ' + sessionStorage.getItem('authToken')
    this.token = sessionStorage.getItem('authToken')
  },
  methods: {
    newFish() {
      axios
        .post('http://localhost:8000/fish/', {
          // headers: {
          //   Authorization: 'JWT ' + sessionStorage.getItem('authToken')
          // },
          fishId: this.newFishId,
          fishDateTime: this.newFishDateTime,
          fishType: this.newFishType.toUpperCase(),
          fishTags: this.newFishTags.toString(),
          fishDetails: this.newFishDetails
        })
        .then(response => {
          alert('Fish Added')
          this.clear()
        })
        .catch(e => {
          if (e.response.status === 400) {
            alert(e.message + ' : ' + JSON.stringify(e.response.data))
          } else {
            alert(e.message)
          }
        })
    },
    clear() {
      this.newFishId = ''
      this.newFishDateTime = new Date().toISOString().slice(0, 16)
      // this.newFishType = ''
      this.newFishTags = []
      this.newFishDetails = ''
    }
  }
}
</script>

<style>

</style>
