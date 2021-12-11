<template>
  <div class="home">
    <div class = 'columns is-multiline'>
        
            <div class='column is-one-third' v-for='category in categories' v-bind:key='category.id'>
                <div class='box'>
                    <figure class='image mb-4'>
                        <router-link v-bind:to='category.get_absolute_url'><img v-bind:src='category.get_image'></router-link>
                    </figure>

                    <h3 class='is-size-4'>{{ category.name }}</h3>

                    <router-link v-bind:to='category.get_absolute_url' class='button is-dark mt-4'>View Category</router-link>
                </div>
            </div>
        
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
        categories: []
    }
  },
  props: {
      category: Object
  },
  components: {},
  mounted() {
      this.getCategory()
  },
  methods: {
      getCategory() {
          axios
          .get('http://127.0.0.1:8000/api/v1/products/')
          .then(response => {
              this.categories = response.data
          })
          .catch(error => {
              console.log(error)
          })
      }
  }
}
</script>

<style scoped>
    .image {
        margin-top: -1.25rem;
        margin-left: -1.25rem;
        margin-right: -1.25rem;
    }
</style>