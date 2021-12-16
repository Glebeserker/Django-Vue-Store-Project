<template>
    <div class='category-detail'>
        
        <section class='hero is-small is-dark mb-6'>
            <div class='hero-body has-text-centered'>
                <p class='title mb-6'>
                    {{ categoryDetail.name }}
                </p>
            </div>
        </section>
        <div class='columns is-multiline '>
        <ProductsArea v-for="product in categoryDetail.products"
        v-bind:key='product.id'
        v-bind:product='product' />
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import ProductsArea from '@/components/ProductsArea'

export default {
    name: 'CategoryDetail',
    components: {
        ProductsArea
    },
    data(){
        return {
            categoryDetail: {
                products: []
            }
        }
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
