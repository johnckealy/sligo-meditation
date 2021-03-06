<template>
  <div>
    <div class="row">
      <q-parallax alt="Image of a landscape scene" src="~assets/Landscape-dimmed.png">
        <div class="q-px-lg">
          <h1 class="text-title text-h1 text-white">
            Sligo Meditation
            <img
              alt="icon of person meditating"
              class="desktop-only"
              style="height: 90px; width:90px;"
              src="~assets/meditating-white.png"
            />
          </h1>
          <h3 class="text-h3 text-white">
            A peaceful meditation practice for all ages, held on Zoom
          </h3>
        </div>
      </q-parallax>
    </div>

    <div class="container">
      <div class="row">
        <div class="col">
          <h3 class="text-h6 text-weight-regular">
            Life has been hard in these times. Bla Bla Bla more content here.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae,
            alias! Sunt, soluta possimus. Libero provident consectetur magni
            deserunt, vel doloremque animi ratione eius. Non, ipsam consectetur
            accusantium hic eum dolore?
          </h3>

          <h3 class="text-h6 text-weight-regular">
            I host meditation sessions, open to all and free of charge. The
            sessions are hosted in Zoom. Below you can find a list of the
            upcoming sessions.
          </h3>

          <event-list />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EventList from "../components/EventList.vue";
export default {
  components: { EventList },
  name: "PageIndex",
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Roboto&display=swap");

.text-title {
  font-family: "Dancing Script", cursive;
}
</style>