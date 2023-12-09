<div class="">
    <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 xl:grid-cols-2">
        
        <div class="py-14 px-4 flex justify-center lg:justify-end">
            <img class="sm:max-w-sm md:max-w-md lg:max-w-md rounded-xl" src="/profile1.webp" alt="Imagen1">
        </div>

        <div class="text-center pt-4 md:my-auto mb-44 xl:-ml-56">
            <h1 class="font-bold text-4xl mb-2 mt-12">Soy <i>Emiliano Maldonado G.</i></h1>
            <p class="text-2xl mb-2">Un desarrollador autodidacta 🇲🇽.</p>
        </div>

    </div>
</div>

<style>
    i{
        --bg-size: 400%;
        --color-one: #26bb80;
        --color-two: #12543a;
        background: linear-gradient(90deg,var(--color-one),var(--color-two),var(--color-one)) 0 0 / var(--bg-size) 100%;
        color: transparent;
        background-clip: text;
        -webkit-background-clip: text;
        animation: move-bg 8s infinite linear;
    }

    @keyframes move-bg {
        to {
            background-position: var(--bg-size) 0;
        }
    }

    @media (prefers-reduced-motion: no-preference) {
        i {
            animation: move-bg 8s linear infinite;
        }
        @keyframes move-bg {
            to {
                background-position: var(--bg-size) 0;
            }
        }
    }
</style>