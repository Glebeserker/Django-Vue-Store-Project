<template>
    <div id='wrapper'>
        <div class = 'column is-full has-text-centered'>
            <figure class='image is-96x96 is-inline-block'>
                <router-link to='/'><img src="@/assets/logo.png" alt="Main Logo"></router-link>
            </figure>
        </div>

        <div class='navigation'>
            <nav class='navbar is-light' role='navigation' aria-label="main navigation">
                <div class="navbar-brand">
                    <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target='navbar-menu' @click="showMobileMenu = !showMobileMenu">
                        <span aria-hidden='true'></span>
                        <span aria-hidden='true'></span>
                        <span aria-hidden='true'></span>
                    </a>
                </div>

                <div class="navbar-menu" id='navbar-menu' v-bind:class="{'is-active': showMobileMenu}">
                    <router-link to='/about' class='navbar-item'>About Me</router-link>
                    <router-link to='/latest-product' class="navbar-item">Latest Products</router-link>
                    <router-link to='cart' aria-label="shopping-cart" class='navbar-item'>
                        <span class='icon'>
                            <i class='fas fa-shopping-cart'></i>
                        </span>
                    </router-link>
                    <router-link to='/log-in' aria-label='profile' class='navbar-item'>
                        <span class='icon'>
                            <i class='fas fa-user'></i>
                        </span>
                    </router-link>
                </div>
            </nav>
        </div>

        <section class='section'>
            <router-view/>
        </section>

        <footer class='footer'>
            <p class='has-text-centered'>Copyright (c) 2021</p>
        </footer>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showMobileMenu: false,
        }
    },
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.navbar-burger {
    max-width: 500%;
}

.navbar {
    display: flex;
    align-content: center;
    justify-content: center;
}

.navbar .navbar-menu {
    flex-grow: initial;
    flex-shrink: initial;
}

.fa-shopping-cart{
    color: grey;
}

.fa-user {
    color: grey;
}
</style>
