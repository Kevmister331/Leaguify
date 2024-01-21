<script setup>
import { ref } from "vue"
import Button from "primevue/button"
import Dropdown from "primevue/dropdown"
import teemoImage from "@/assets/teemo.jpg"
import items from "@/assets/champions.json"

// const message = ref("")
// // const selectedItem = ref(null) // Ref for the selected item
// // const outputTypes = [
// //   {
// //     name: "Songs",
// //     value: "songs",
// //   },
// //   {
// //     name: "Albums",
// //     value: "albums",
// //   },
// //   {
// //     name: "Artists",
// //     value: "artists",
// //   },
// // ]

// const showMessage = () => {
//   message.value = `Selected Champion: ${selectedItem.value.name}`
// }
</script>

<template>
  <div class="background">
    <div class="container">
      <h2>Leaguify</h2>
      <!-- <Dropdown :options="items" optionLabel="name" v-model="selectedItem" filter>
        <template #item="{ option }">
          <div class="dropdown-item" @click="manualSelect(option)">
            <span>{{ option.name }}</span>
          </div>
        </template>
      </Dropdown> -->
      <div>
        <select v-model="item123">
          <option v-for="item in items" :key="item.name" :value="item.name" @click="manualSelect(option)" >
            {{ item.name }}
          </option>
        </select>
      </div>
      <h3>Select output type</h3>
      <div>
        <select v-model="selectedType">
          <option value="Songs">Songs</option>
          <option value="Albums">Albums</option>
          <option value="Artists">Artists</option>
        </select>
      </div>
      <Button class="button" label="Confirm Selection" @click="submitOptions"></Button>
      <!-- <p>{{ selectedItem ? selectedItem.name : selectedItem }}</p> -->
      <p>{{ selectedType }}</p>
    </div>
    <div class="container"></div>

    <div class="song-list-container">
      <h1>Result</h1>
      <p>Get your top 5 tracks</p>
      <ul class="song-list">
        <li v-for="(song, index) in songs" :key="index" class="song-item">
          <span class="song-rank">{{ index + 1 }}</span>
          <a :href="song.url" class="song-title" target="_blank">{{ song.title }}</a>
          <span class="song-artist">{{ song.artist }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "SongList",
  data() {
    return {
      // This would typically be fetched from an API
      songs: [
        {
          title: "Die For You",
          artist: "Joji",
          url: "https://open.spotify.com/track/your-spotify-track-id",
        },
        {
          title: "1AM FREESTYLE",
          artist: "Joji",
          url: "https://open.spotify.com/track/your-spotify-track-id",
        },
        {
          title: "YEAH RIGHT",
          artist: "Joji",
          url: "https://open.spotify.com/track/your-spotify-track-id",
        },
        {
          title: "SLOW DANCING IN THE DARK",
          artist: "Joji",
          url: "https://open.spotify.com/track/your-spotify-track-id",
        },
        {
          title: "kill u",
          artist: "Cavetown",
          url: "https://open.spotify.com/track/your-spotify-track-id",
        },
        // Make sure to replace the URLs with the actual Spotify song URLs
      ],
    }
  },
  methods: {
    submitOptions() {
      console.log("Submitting options:", this.item123 ? this.item123.value : this.item123, this.selectedType)
      // Here you would make your API call with both selected options.
      // Example using axios:
      // this.makeApiCall(this.selectedOption1, this.selectedOption2);
    },
    manualSelect(option) {
      // This method allows you to manually set selectedItem
      console.log("FFFFFFFFFF");
      this.item123 = option.name;
      // If you need to trigger additional logic, you can do that here
    },
    // Example API call method
    async makeApiCall(option1, option2) {
      try {
        const response = await axios.post("your-api-endpoint", {
          option1: option1,
          option2: option2,
        })
        console.log(response.data)
        // Handle your response
      } catch (error) {
        console.error("API call failed:", error)
      }
    },
  },
}
</script>

<style scoped>
h2 {
  color: #11b981;
  margin: 50px;
}
.background {
  background-image: linear-gradient(#212121, #101010);
  min-width: 100vw;
  min-height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
}
.button {
  margin: 20px;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-top: 4rem;
  margin: 10px;
}

.song-list-container {
  background-color: #6a0dad; /* Purple background */
  color: white;
  padding: 20px;
  padding-left: 50px;
  border-radius: 10px;
  max-width: 60vw; /* Set max width */
  margin: auto; /* Center the container */
}

.song-list {
  list-style-type: none;
  padding: 0;
}

.song-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.song-rank {
  font-weight: bold;
  margin-right: 10px;
}

.next-step {
  background-color: #9b59b6; /* Lighter purple */
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
}

.song-title {
  margin-right: 5px;
  color: inherit; /* The link will use the color inherited from the parent element */
  text-decoration: none; /* Removes the underline from links */
}

.song-title:hover {
  text-decoration: none; /* Ensures the underline does not appear on hover */
}
</style>
