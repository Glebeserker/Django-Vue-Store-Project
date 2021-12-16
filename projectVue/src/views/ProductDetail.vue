<template>
    <div class='product-detail'>
        <div class="box">
            <div class="columns is-multiline">
                <div class="column is-full-mobile is-full-touch is-three-quarters-desktop">
                    <figure class='image'>
                        <img v-bind:src="product.get_image">
                    </figure>
                </div>
                <div class="column is-one-fourth is-full-mobile is-full-touch has-text-centered">
                    <h1 class="title mb-4 is-size-1">{{ product.name }}</h1>
                    <h3 class="is-size-3 mb-4">Price:  ${{ product.price }}</h3>
                    <h4 class='is-size-3'>Description: </h4>
                    <p class=''>{{product.description}}</p>
                    <button class="button mt-4 is-medium is-dark">Add To Cart</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ProductDetail',
    data() {
        return {
            product: []
        }
    },
    mounted(){
        this.getProduct()
    },
    methods: {
        getProduct(){
            const productSlug = this.$route.params.product_slug
            const categorySlug = this.$route.params.category_slug
            axios
            .get(`http://127.0.0.1:8000/api/v1/products/${categorySlug}/${productSlug}`)
            .then(response => {
                this.product = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
