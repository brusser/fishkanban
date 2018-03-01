<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">
          <h1 class="title is-2">Welcome to Fish Kanban!</h1>
          <div class="tabs is-centered is-toggle is-medium">
            <ul>
              <li v-bind:class="{ 'is-active': isSignInActive}">
                <a v-on:click="switchToSignIn" id="signin">Sign In</a>
              </li>
              <li v-bind:class="{ 'is-active': isSignUpActive}">
                <a v-on:click="switchToSignUp" id="signup">Sign Up</a>
              </li>
            </ul>
          </div>

          <!-- Sign In Form -->
          <div class="box" v-bind:class="{ 'is-invisible is-overlay': isSignUpActive}" id="signin-form">
            <form v-on:submit.prevent="signIn">
              <div class="field">
                <p class="control has-icons-left">
                  <input class="input" v-model="username" id="username" type="text" placeholder="Name" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
              </div>
              <div class="field">
                <p class="control has-icons-left">
                  <input class="input" v-model="password" id="password" type="password" placeholder="Password" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </p>
              </div>
              <div class="field">
                <p class="control">
                  <button class="button is-primary">
                    Submit
                  </button>
                </p>
              </div>
            </form>
          </div>

          <!-- Sign Up Form -->
          <div class="box" v-bind:class="{ 'is-invisible is-overlay': isSignInActive}" id="signup-form">
            <form v-on:submit.prevent="signUp">
              <div class="field">
                <p class="control has-icons-left">
                  <input class="input" v-model="username" id="username" type="text" placeholder="Name" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
              </div>
              <div class="field">
                <p class="control has-icons-left">
                  <input class="input" v-model="email" id="email" type="email" placeholder="Email" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                </p>
              </div>
              <div class="field">
                <p class="control has-icons-left">
                  <input class="input" v-model="password" id="password" type="password" placeholder="Password" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </p>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <label class="checkbox">
                      <input id="toc" type="checkbox" required> I agree to the
                      <a href="#">terms and conditions</a>
                    </label>
                  </div>
                </div>
              </div>
              <div class="field">
                <p class="control">
                  <button class="button is-primary">
                    Submit
                  </button>
                </p>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserAuth',
  data() {
    return {
      isSignUpActive: false,
      isSignInActive: true,
      email: 'test@test.com',
      username: 'test',
      password: 'test1234'
    }
  },

  methods: {
    switchToSignUp() {
      this.isSignInActive = false
      this.isSignUpActive = true
    },

    switchToSignIn() {
      this.isSignUpActive = false
      this.isSignInActive = true
    },

    signUp() {
      axios
        .post('http://localhost:8000/auth/users/create/', {
          email: this.email,
          username: this.username,
          password: this.password
        })
        .then(response => {
          alert(
            'Your account has been created. You will be signed in automatically'
          )
          this.signIn()
        })
        .catch(e => {
          if (e.response.status === 400) {
            alert(e.message + ' : ' + JSON.stringify(e.response.data))
          } else {
            alert(e.message)
          }
        })
    },

    signIn() {
      const credentials = { username: this.username, password: this.password }

      axios
        .post('http://localhost:8000/auth/jwt/create/', credentials)
        .then(response => {
          sessionStorage.setItem('authToken', response.data.token)
          sessionStorage.setItem('username', this.username)
          this.$router.push('/kanban')
        })
        .catch(e => {
          console.log(e.message + ' : ' + JSON.stringify(e.response.data))
          if (e.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(e.response.data)
            console.log(e.response.status)
            console.log(e.response.headers)
          } else if (e.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(e.request)
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log('Error', e.message)
          }
          console.log(e.config)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
