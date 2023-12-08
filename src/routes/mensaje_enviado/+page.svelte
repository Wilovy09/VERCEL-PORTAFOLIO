<script>
    import Layout from '../../layouts/Layout.svelte';
</script>

<Layout>
    <div class="flex min-h-screen items-center justify-center">
        <div class="rounded-lg bg-gray-50 px-16 py-14 max-w-[350px]">
          <div class="flex justify-center">
            <div class="rounded-full bg-green-200 p-6">
              <div class="flex h-16 w-16 items-center justify-center rounded-full bg-green-500 p-4">
                <svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-8 w-8 text-white">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
              </div>
            </div>
          </div>
          <h3 class="my-4 text-center text-3xl font-semibold text-gray-700">Mensaje enviado!!!</h3>
          <p class="text-center font-normal text-gray-600">Me pondre en contacto contigo lo antes posible</p>
        </div>
      </div>
</Layout>