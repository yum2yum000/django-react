import mapGetters from 'vuex'

export const authComputed={
    ...mapGetters['login/loggedIn']
}