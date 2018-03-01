<template>
    <div id="swimlanes" class="block">
        <div class="columns">
            <div class="column">
                <div class="box">
                    <h1 class="title">
                        <strong>BackLog</strong>
                    </h1>
                    <div v-if="backlogFish && backlogFish.length">
                        <div v-for="fish of backlogFish">
                            <div v-cloak class="card">
                                <header class="card-header">
                                    <p class="card-header-title">
                                        Fish ID: {{fish.fishId}}
                                    </p>
                                </header>
                                <div class="card-content">
                                    <div v-for="(value, name) in fish.fishDetails">
                                        <h5 class="title is-5">{{name}}: </h5>
                                        <h6 class="subtitle is-6">{{value}}</h6>
                                        <p></p>
                                    </div>
                                </div>
                                <footer class=" card-footer ">
                                    <div class="card-footer-item ">
                                        <button type="button " v-on:click="editCard " class="button is-info ">
                                            <i class="fa fa-edit "></i>
                                        </button>
                                    </div>
                                    <div class="card-footer-item ">
                                        <button type="button " v-clock v-on:click="deleteCard " class="button is-danger ">
                                            <i class="fa fa-times-circle "></i>
                                        </button>
                                    </div>
                                    <div class="card-footer-item ">
                                        <button type="button " v-on:click="moveCardRight " class="button is-primary ">
                                            <i class="fa fa-chevron-circle-right "></i>
                                        </button>
                                    </div>
                                </footer>
                            </div>
                            <br>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column ">
                <div class="box ">
                    <h1 class="title ">
                        <strong>Processing</strong>
                    </h1>
                    <div v-if="fish && fish.length ">
                        <div v-for="f of fish ">
                            <div v-if="f.fishState=='PROCESSING' ">
                                <div v-cloak class="card ">
                                    <div class="card-content ">
                                        <h2 class="title is-4 ">ID: {{f.fishId}} </h2>
                                        <h3 class="subtitle ">Fish Type:
                                            <strong>{{f.fishType}}</strong>
                                        </h3>
                                    </div>
                                    <footer class="card-footer ">
                                        <div class="card-footer-item ">
                                            <button type="button " v-on:click="editCard " class="button is-info ">
                                                <i class="fa fa-edit "></i>
                                            </button>
                                        </div>
                                        <div class="card-footer-item ">
                                            <button type="button " v-clock v-on:click="deleteCard " class="button is-danger ">
                                                <i class="fa fa-times-circle "></i>
                                            </button>
                                        </div>
                                        <div class="card-footer-item ">
                                            <button type="button " v-on:click="moveCardRight " class="button is-primary ">
                                                <i class="fa fa-chevron-circle-right "></i>
                                            </button>
                                        </div>
                                    </footer>
                                </div>
                                <br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column ">
                <div class="box ">
                    <h1 class="title ">
                        <strong>Completed</strong>
                    </h1>
                    <div v-if="fish && fish.length ">
                        <div v-for="f of fish ">
                            <div v-if="f.fishState=='COMPLETED' ">
                                <div v-cloak class="card ">
                                    <div class="card-content ">
                                        <h2 class="title is-4 ">ID: {{f.fishId}} </h2>
                                        <h3 class="subtitle ">Fish Type:
                                            <strong>{{f.fishType}}</strong>
                                        </h3>
                                    </div>
                                    <footer class="card-footer ">
                                        <div class="card-footer-item ">
                                            <button type="button " v-on:click="editCard " class="button is-info ">
                                                <i class="fa fa-edit "></i>
                                            </button>
                                        </div>
                                        <div class="card-footer-item ">
                                            <button type="button " v-clock v-on:click="deleteCard " class="button is-danger ">
                                                <i class="fa fa-times-circle "></i>
                                            </button>
                                        </div>
                                        <div class="card-footer-item ">
                                            <button type="button " v-on:click="moveCardRight " class="button is-primary ">
                                                <i class="fa fa-chevron-circle-right "></i>
                                            </button>
                                        </div>
                                    </footer>
                                </div>
                                <br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      //   backlogFish: [{ fishId: '', details: [] }],
      backlogFish: [],
      processingFish: [],
      completedFish: [],
      fish: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created() {
    axios.defaults.headers['Authorization'] =
      'JWT ' + sessionStorage.getItem('authToken')
    this.token = sessionStorage.getItem('authToken')

    axios
      .get(`http://localhost:8000/fish/`)
      .then(response => {
        // JSON responses are automatically parsed.
        for (var fish of response.data) {
          //   var newFish = {}
          //   var fishDetails = {}
          //   console.log(fish)
          //   if (fish.fishState === 'NEW') {
          //     for (var key in fish) {
          //       console.log(key)
          //       if (fish.hasOwnProperty(key)) {
          //         console.log(fish[key])
          //         fishDetails[key] = fish[key]
          //       }
          //     }
          var fishId = fish.fishId
          var fishDetails = {}
          fishDetails['Date'] = fish.fishDateTime
          fishDetails['Type'] = fish.fishType
          fishDetails['Description'] = fish.fishDetails

          if (fish.fishState === 'NEW') {
            this.backlogFish.push({ fishId, fishDetails })
          } else if (fish.fishState === 'PROCESSING') {
            this.processingFish.push({ fishId, fishDetails })
          } else if (fish.fishState === 'COMPLETED') {
            this.completedFish.push({ fishId, fishDetails })
          }
        }
      })
      .catch(e => {
        this.errors.push(e)
      })

    // async / await version (created() becomes async created())
    //
    // try {
    //   const response = await axios.get(`http://jsonplaceholder.typicode.com/posts`)
    //   this.posts = response.data
    // } catch (e) {
    //   this.errors.push(e)
    // }
  }
}
</script>

<style>

</style>
