<template>
    <div class='category-detail'>
        <section class='hero is-medium is-dark mb-6'>
            <div class='hero-body has-text-centered'>
                <p class='title mb-6'>
                    {{  }}
                </p>
            </div>
        </section>

        <div class='column is-multiline'>
            <div class='column is-9' v-for='product in categoryDetail' v-bind:key='product.id'>
                <div class='box'>
                    <figure class='image mb-6'>
                        <img v-bind:src="product.get_thumbnail">
                    </figure>

                    <h1 class='title'>{{ categoryDetail.product.name }}</h1>
                    <p><strong>Price: </strong>$ {{ categoryDetail.product.price }}</p>
                    <router-link v-bind:to='categoryDetail.product.get_absolute_url' class='button is-dark mt-4'>View Product</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CategoryDetail',
    data(){
        return {
            categoryDetail: {
                product: []
            },
            
        }
    },
    props: {
        categoryDetail: Object
    },
    mounted(){
        this.getCategoryDetail()
    },
    methods: {
        getCategoryDetail(){
            const categorySlug = this.$route.params.category_slug
            axios
            .get(`http://127.0.0.1:8000/api/v1/products/${categorySlug}`)
            .then(response => {
                this.categoryDetail = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
