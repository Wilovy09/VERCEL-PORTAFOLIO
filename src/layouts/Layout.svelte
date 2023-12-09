<script>
    import "../app.css";
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
</script>

<section class="max-w-[1680px] w-full">
    <Navbar/>
    <slot/>
    <Footer/>
</section>

<style>
    
</style>

